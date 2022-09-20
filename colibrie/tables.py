from fitz import Rect, TEXTFLAGS_DICT, TEXT_PRESERVE_IMAGES

from colibrie.geometry import Point
from colibrie.core import Table, Cell, Rotation
from ailist import AIList


def get_tables_candidates(vertical_lines, horizontal_lines):
    interval_tree = AIList()
    [interval_tree.add(line[0].y, line[1].y) for line in vertical_lines]

    vertical_merged_interval = interval_tree.merge(gap=1)
    
    tables_candidate = []
    interval_group = {}

    for vertical_interval in vertical_merged_interval:
        #pprint(vertical_interval)
        interval_group[vertical_interval.start, vertical_interval.end] = []

        for line in vertical_lines:
            if line[0].y >= vertical_interval.start and line[1].y <= vertical_interval.end:
                interval_group[vertical_interval.start, vertical_interval.end].append(line)

        for line in horizontal_lines:
            if line[0].y >= vertical_interval.start and line[1].y <= vertical_interval.end:
                interval_group[vertical_interval.start, vertical_interval.end].append(line)

        # get horizontal interval from each group
        interval_tree = AIList()
        [interval_tree.add(line[0].x, line[1].x) for line in interval_group[vertical_interval.start, vertical_interval.end]]

        horizontal_merged_interval = interval_tree.merge(gap=1)

        for horizontal_interval in horizontal_merged_interval:
            #pprint(horizontal_interval)
            table_candidate = []

            for line in interval_group[vertical_interval.start, vertical_interval.end]:
                #pprint(line)
                if line[0].x >= horizontal_interval.start and line[1].x <= horizontal_interval.end:
                    table_candidate.append(line)
                    
            # We make sure that every table candidate have at least 4 lines
            # Which is the bare minimum to create a single cell
            if len(table_candidate) > 3:
                tables_candidate.append(table_candidate)
            else:
                continue
            
    return tables_candidate


#def get_valid_tables_candidates(intersections):
#    valid_table_candidate_lst = []
#    valid_table_candidate = []
#    current_rect = None
#
#    for intersection in sorted(intersections, key=lambda point: (point.y, point.x)):
#        # intersections[point][0] is always the vertical lines
#        point_a, point_b = intersections[intersection][0]
#        # intersections[point][0] is always the horizontal lines
#        point_c, point_d = intersections[intersection][1]
#
#        if not current_rect:
#            current_rect = Rect(
#                Point(intersection.x - 3, intersection.y - 3),  # top_left
#                Point(point_d.x + 3, point_b.y + 3)  # bottom_right
#            )
#
#        if current_rect.contains(intersection):
#            valid_table_candidate.append(intersection)
#        else:
#            # We do not not take the candidate if it has less than 6 intersection point which represent
#            # the minimal number of point for a single column 2 row (header + value) table
#            # can be tweak if it is proven not working correctly
#            if len(valid_table_candidate) >= 6:
#                valid_table_candidate_lst.append(valid_table_candidate)
#            valid_table_candidate = [intersection]
#            current_rect = Rect(
#                Point(intersection.x - 3, intersection.y - 3),  # top_left
#                Point(point_d.x + 3, point_b.y + 3)  # bottom_right
#            )
#
#    # append the last possible candidate
#    if len(valid_table_candidate) >= 6:
#        valid_table_candidate_lst.append(valid_table_candidate)
#
#    return valid_table_candidate_lst


def create_table(intersections, horizontal_lines, vertical_lines):
    #for index, table_candidate in enumerate(valid_table_candidate_lst):
    intersections = [intersection for intersection in sorted(intersections, key=lambda point: (point.y, point.x))]
    
    table = Table(
        intersections=intersections,
        rect=Rect(intersections[0],
                  intersections[-1]),
        horizontal_lines=horizontal_lines,
        vertical_lines=vertical_lines
    )

    return table


def process_table(page, table, preserve_span, intersections_info):
    """
        tl => top left
        tr => top right
        bl => bottom left
        br => bottom right
    """
    
    #valid_tables = []
    
    #for table in tables:
    rotated_span = {}
    rotated_span[Rotation.unrotated.value] = 0
    rotated_span[Rotation.rotated_90.value] = 0

    if preserve_span:
        text = page.get_text("dict", flags=TEXTFLAGS_DICT & ~TEXT_PRESERVE_IMAGES, clip=table.rect)
    else:
        textpage = page.get_textpage(flags=TEXTFLAGS_DICT & ~TEXT_PRESERVE_IMAGES, clip=table.rect)
        
    # Reconstruct intersection point group by lines height as
    # list of list containing intersections point
    rows = []
    for index, row in table.intersections_df.groupby('y'):
        rows.append(row.to_dict(orient="records"))
        
    for row_index, row in enumerate(rows):
        # Stopping one row before the last row because
        # the last row is always the bottom of the table
        # and can't be used for a cell matching
        if row_index == len(rows) - 1:
            break
            
        tl = None
        for intersection_index, intersection in enumerate(row):
            if intersection_index == len(row) - 1:
                break
                
            if not tl:
                tl = intersection
                
            tr = row[intersection_index + 1]
            tl_intersection_line = intersections_info[tl["x"], tl["y"]]
            tr_intersection_line = intersections_info[tr["x"], tr["y"]]
            
            # if tl and tr point are the same horizontal_line
            if tl_intersection_line[1] == tr_intersection_line[1]:
                bl, br = find_intersection_correspondance(tl, tr, rows, row_index, intersections_info)
            else:
                tl = None
                continue
                
            if not bl and not br:
                continue
                
            cell = Cell(
                rect=Rect(Point(tl["x"], tl["y"]), Point(br["x"], br["y"])),
                row_size=table.row[br["y"]] - table.row[tl["y"]],
                col_size=table.col[br["x"]] - table.col[tl["x"]]
            )
            
            if preserve_span:
                cell.get_text(text)
                for span in cell.spans:
                    try:
                        rotated_span[span['dir']] += 1
                    except KeyError:
                        print(f"missing key for rotation {span['dir']}")
            else:
                cell.text = page.get_textbox(cell.rect, textpage=textpage)
            
            table.cells[row_index].append(cell)
            
            #print(cell, cell.row_size, cell.col_size)
            # to permit the transposition of cells in order to rotate the table if needed
            # we append None value to match the size of sum(col_size) for each row
            for i in range(cell.row_size):
                for j in range(1, cell.col_size):
                    table.cells[row_index + i].append(None)
                    
            tl = None
            
    
    ############## HANDLE BAD TABLE ######################
    total_cell = 0
    empty_cell = 0
    for row in table.cells:
        for cell in row:
            if cell:
                total_cell += 1
                if not cell.text:
                    empty_cell += 1
                    
    empty_cell_ratio = total_cell / max(empty_cell, 1) # prevent division by 0 if empty table
    
    # if there is only empty cell in the table, it is not a valid table
    if empty_cell_ratio == 1:
        return None
    #######################################################
    else:
        table.match_row_size_sum()
        table.rotation = max(rotated_span, key=rotated_span.get)
        table.set_rotation()
        
    return table


def find_intersection_correspondance(tl, tr, intersection_rows, row_index, intersections_info):
    """
        tl => top left
        tr => top right
        bl => bottom left
        br => bottom right
    """
    bl = None
    br = None

    # Starting to search for corresponding bl / br at row_index + 1 because we always 
    # match a row with the row below it
    for row in intersection_rows[row_index + 1:]:
        for intersection in row:

            if tl["x"] <= intersection["x"] < tr["x"] and not bl:
                bl = intersection

            if intersection["x"] == tr["x"] and not br and bl:
                br = intersection

            if br and bl:
                tl_intersection_line = intersections_info[tl["x"], tl["y"]]
                tr_intersection_line = intersections_info[tr["x"], tr["y"]]

                bl_intersection_line = intersections_info[bl["x"], bl["y"]]
                br_intersection_line = intersections_info[br["x"], br["y"]]

                if (
                    bl_intersection_line[1] == br_intersection_line[1] and # if bl and br point are on the same horizontal_line
                    tl_intersection_line[0] == bl_intersection_line[0] and # if tl and bl point are on the same vertical_line
                    tr_intersection_line[0] == br_intersection_line[0] # if tr and br point are on the same vertical_line
                ):
                    return bl, br
                else:
                    bl = None
                    br = None

        # If we cannot find any valid candidate for closing the cell on this row, we need
        # to reset the start / end point value for the next row to None to prevent
        # Mixed row matching
        bl = None
        br = None

    return None, None
