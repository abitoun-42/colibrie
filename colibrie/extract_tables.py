import random
import fitz

from colibrie.tables import (
    create_table,
    process_table,
    get_tables_candidates
)

from colibrie.intersection import (
    get_intersection_between_horizontal_and_vertical_lines
)

from colibrie.lines import (
    get_lines_fragmented,
    get_horizontal_fragmented_lines,
    get_vertical_fragmented_lines,
    remove_overlaping_horizontal_lines,
    remove_overlaping_vertical_lines,
    generate_missing_horizontal_lines,
    generate_missing_vertical_lines,
    normalize_vertical_lines,
    normalize_horizontal_lines,
)


def extract_tables(filepath, debug_mode=False, preserve_span=True):
    """
        :param: preserve_span: bool
            give a possibility to speed_up the execution
            by not preserving information about text position and only keeping
            the text content, can be useful for those with proper table aligned that
            do not need to do extra work with it
    """

    doc = fitz.Document(filepath)

    tables_lst = []

    for page in doc:

        ####################### GET LINE ######################################

        lines_fragmented = get_lines_fragmented(page)

        vertical_lines = get_vertical_fragmented_lines(lines_fragmented)

        horizontal_lines = get_horizontal_fragmented_lines(lines_fragmented)

        #######################################################################

        ################## REMOVE OVERLAPING LINES ############################

        vertical_lines = remove_overlaping_vertical_lines(vertical_lines)

        horizontal_lines = remove_overlaping_horizontal_lines(horizontal_lines)

        #######################################################################

        if not vertical_lines or not horizontal_lines:
            continue

        #################### NORMALIZE Y X COORDINATE ############################

        vertical_lines = normalize_vertical_lines(vertical_lines, horizontal_lines)

        horizontal_lines = normalize_horizontal_lines(vertical_lines, horizontal_lines)

        ########################################################################

        #################### GET TABLES CANDIDATES #############################
        tables_candidates = get_tables_candidates(vertical_lines, horizontal_lines)
        ########################################################################

        for table_candidate in tables_candidates:

            vertical_lines = get_vertical_fragmented_lines(table_candidate)

            horizontal_lines = get_horizontal_fragmented_lines(table_candidate)

            ########################## CREATE UNEXISTING MISSING LINE ###########

            distinct_y_lst = set([point.y for lines in vertical_lines for point in lines])
            distinct_x_lst = set([point.x for lines in horizontal_lines for point in lines])

            if not distinct_x_lst or not distinct_y_lst:
                continue

            range_y = (min(distinct_y_lst), max(distinct_y_lst))
            range_x = (min(distinct_x_lst), max(distinct_x_lst))

            # If the table does not meet the condition of a minimum size
            # we assume it is a bad table
            if (range_y[1] - range_y[0]) <= 20 and (range_x[1] - range_x[0]) <= 50:
                continue

            horizontal_lines = generate_missing_horizontal_lines(horizontal_lines,
                                                                 vertical_lines,
                                                                 distinct_x_lst,
                                                                 distinct_y_lst)

            vertical_lines = generate_missing_vertical_lines(horizontal_lines,
                                                             vertical_lines,
                                                             distinct_x_lst,
                                                             distinct_y_lst)

            ########################################################################

            ################### GET INTERSECTIONS #################################

            intersections = get_intersection_between_horizontal_and_vertical_lines(
                horizontal_lines, vertical_lines
            )


            if not len(intersections) >= 6:
                continue

            #########################################################################

            ###################### CREATE TABLE LIST ################################
            table = create_table(intersections, horizontal_lines, vertical_lines)
            
            #########################################################################

            #################################FILL TABLE##############################

            table = process_table(page, table, preserve_span, intersections)

            if not table:
                continue

            #########################################################################

            if debug_mode:
                pix = page.get_pixmap()
                table.debug.image = pix.tobytes()

            tables_lst.append(table)

    doc.close()

    return tables_lst
