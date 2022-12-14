from colibrie.geometry import Point

expected_fragmented_lines_test_1 = [
    (Point(468, 271), Point(468, 288)),
    (Point(71, 306), Point(71, 325)),
    (Point(354, 325), Point(354, 343)),
    (Point(524, 598), Point(524, 616)),
    (Point(468, 325), Point(468, 343)),
    (Point(354, 598), Point(354, 616)),
    (Point(411, 543), Point(411, 561)),
    (Point(524, 325), Point(524, 343)),
    (Point(468, 489), Point(468, 507)),
    (Point(184, 689), Point(184, 707)),
    (Point(524, 379), Point(524, 398)),
    (Point(524, 288), Point(524, 306)),
    (Point(298, 416), Point(298, 434)),
    (Point(354, 288), Point(354, 306)),
    (Point(128, 398), Point(128, 416)),
    (Point(468, 452), Point(468, 470)),
    (Point(71, 525), Point(71, 543)),
    (Point(354, 653), Point(354, 671)),
    (Point(184, 306), Point(184, 325)),
    (Point(298, 343), Point(298, 361)),
    (Point(354, 379), Point(354, 398)),
    (Point(128, 227), Point(128, 271)),
    (Point(524, 183), Point(524, 271)),
    (Point(558, 793), Point(558, 813)),
    (Point(524, 616), Point(524, 634)),
    (Point(128, 288), Point(128, 306)),
    (Point(298, 671), Point(298, 689)),
    (Point(70, 707), Point(298, 707)),
    (Point(354, 616), Point(354, 634)),
    (Point(241, 416), Point(241, 434)),
    (Point(241, 306), Point(241, 325)),
    (Point(184, 489), Point(241, 489)),
    (Point(71, 271), Point(71, 288)),
    (Point(468, 598), Point(468, 616)),
    (Point(354, 361), Point(411, 361)),
    (Point(241, 343), Point(241, 361)),
    (Point(128, 434), Point(128, 452)),
    (Point(298, 525), Point(298, 543)),
    (Point(71, 634), Point(71, 653)),
    (Point(468, 635), Point(468, 653)),
    (Point(128, 183), Point(525, 183)),
    (Point(411, 525), Point(411, 543)),
    (Point(354, 562), Point(411, 562)),
    (Point(128, 361), Point(128, 379)),
    (Point(411, 653), Point(411, 671)),
    (Point(524, 362), Point(524, 379)),
    (Point(298, 306), Point(298, 325)),
    (Point(354, 398), Point(354, 416)),
    (Point(411, 325), Point(411, 343)),
    (Point(411, 343), Point(411, 361)),
    (Point(184, 562), Point(184, 580)),
    (Point(184, 580), Point(184, 598)),
    (Point(468, 653), Point(468, 671)),
    (Point(354, 306), Point(354, 325)),
    (Point(241, 507), Point(241, 525)),
    (Point(241, 525), Point(241, 543)),
    (Point(184, 634), Point(184, 653)),
    (Point(524, 507), Point(524, 525)),
    (Point(298, 634), Point(298, 653)),
    (Point(468, 343), Point(468, 361)),
    (Point(71, 598), Point(71, 616)),
    (Point(241, 227), Point(241, 271)),
    (Point(411, 361), Point(468, 361)),
    (Point(71, 227), Point(71, 271)),
    (Point(298, 616), Point(298, 634)),
    (Point(71, 288), Point(71, 306)),
    (Point(354, 434), Point(411, 434)),
    (Point(524, 562), Point(524, 580)),
    (Point(468, 507), Point(468, 525)),
    (Point(298, 689), Point(298, 707)),
    (Point(354, 507), Point(354, 525)),
    (Point(411, 616), Point(411, 634)),
    (Point(411, 452), Point(411, 470)),
    (Point(558, 793), Point(595, 793)),
    (Point(411, 227), Point(411, 271)),
    (Point(298, 271), Point(298, 288)),
    (Point(128, 271), Point(128, 288)),
    (Point(524, 452), Point(524, 470)),
    (Point(128, 325), Point(128, 343)),
    (Point(468, 288), Point(468, 306)),
    (Point(468, 634), Point(525, 634)),
    (Point(184, 361), Point(184, 379)),
    (Point(411, 562), Point(468, 562)),
    (Point(411, 416), Point(411, 434)),
    (Point(184, 271), Point(184, 288)),
    (Point(524, 183), Point(524, 227)),
    (Point(354, 671), Point(354, 689)),
    (Point(468, 416), Point(468, 434)),
    (Point(354, 689), Point(354, 707)),
    (Point(70, 183), Point(128, 183)),
    (Point(354, 634), Point(411, 634)),
    (Point(128, 634), Point(128, 653)),
    (Point(468, 616), Point(468, 634)),
    (Point(354, 227), Point(354, 271)),
    (Point(-13, 794), Point(122, 794)),
    (Point(241, 580), Point(241, 598)),
    (Point(71, 325), Point(71, 343)),
    (Point(128, 653), Point(128, 671)),
    (Point(241, 653), Point(241, 671)),
    (Point(298, 598), Point(298, 616)),
    (Point(184, 325), Point(184, 343)),
    (Point(71, 489), Point(71, 507)),
    (Point(128, 343), Point(128, 361)),
    (Point(411, 362), Point(411, 379)),
    (Point(354, 470), Point(354, 488)),
    (Point(468, 562), Point(468, 580)),
    (Point(411, 671), Point(411, 689)),
    (Point(411, 689), Point(411, 707)),
    (Point(298, 227), Point(298, 271)),
    (Point(468, 470), Point(468, 488)),
    (Point(468, 435), Point(468, 452)),
    (Point(354, 489), Point(411, 489)),
    (Point(524, 525), Point(524, 543)),
    (Point(298, 452), Point(298, 470)),
    (Point(241, 489), Point(298, 489)),
    (Point(524, 489), Point(524, 507)),
    (Point(184, 288), Point(184, 306)),
    (Point(298, 580), Point(298, 598)),
    (Point(241, 271), Point(241, 288)),
    (Point(411, 507), Point(411, 525)),
    (Point(241, 325), Point(241, 343)),
    (Point(241, 598), Point(241, 616)),
    (Point(411, 634), Point(468, 634)),
    (Point(524, 343), Point(524, 361)),
    (Point(-13, 794), Point(-13, 814)),
    (Point(468, 379), Point(468, 398)),
    (Point(184, 434), Point(184, 452)),
    (Point(128, 543), Point(128, 562)),
    (Point(128, 452), Point(128, 470)),
    (Point(241, 543), Point(241, 562)),
    (Point(468, 671), Point(468, 689)),
    (Point(241, 452), Point(241, 470)),
    (Point(298, 507), Point(298, 525)),
    (Point(-13, 814), Point(122, 814)),
    (Point(524, 470), Point(524, 488)),
    (Point(411, 271), Point(411, 288)),
    (Point(354, 525), Point(354, 543)),
    (Point(298, 653), Point(298, 671)),
    (Point(595, 793), Point(595, 813)),
    (Point(241, 634), Point(241, 653)),
    (Point(184, 653), Point(184, 671)),
    (Point(468, 398), Point(468, 416)),
    (Point(71, 379), Point(71, 398)),
    (Point(128, 598), Point(128, 616)),
    (Point(298, 325), Point(298, 343)),
    (Point(241, 434), Point(241, 452)),
    (Point(411, 398), Point(411, 416)),
    (Point(558, 813), Point(595, 813)),
    (Point(298, 543), Point(298, 562)),
    (Point(354, 635), Point(354, 653)),
    (Point(411, 562), Point(411, 580)),
    (Point(411, 580), Point(411, 598)),
    (Point(468, 362), Point(468, 379)),
    (Point(184, 543), Point(184, 562)),
    (Point(184, 452), Point(184, 470)),
    (Point(71, 183), Point(71, 271)),
    (Point(468, 689), Point(468, 707)),
    (Point(184, 616), Point(184, 634)),
    (Point(524, 398), Point(524, 416)),
    (Point(524, 416), Point(524, 434)),
    (Point(524, 306), Point(524, 325)),
    (Point(354, 562), Point(354, 580)),
    (Point(524, 580), Point(524, 598)),
    (Point(71, 183), Point(524, 183)),
    (Point(71, 562), Point(71, 580)),
    (Point(468, 434), Point(525, 434)),
    (Point(411, 434), Point(468, 434)),
    (Point(354, 580), Point(354, 598)),
    (Point(241, 562), Point(241, 580)),
    (Point(241, 361), Point(241, 379)),
    (Point(241, 470), Point(241, 488)),
    (Point(241, 489), Point(241, 507)),
    (Point(128, 306), Point(128, 325)),
    (Point(298, 434), Point(298, 452)),
    (Point(71, 452), Point(71, 470)),
    (Point(184, 398), Point(184, 416)),
    (Point(524, 271), Point(524, 288)),
    (Point(298, 470), Point(298, 488)),
    (Point(298, 398), Point(298, 416)),
    (Point(354, 416), Point(354, 434)),
    (Point(298, 562), Point(298, 580)),
    (Point(524, 689), Point(524, 707)),
    (Point(468, 525), Point(468, 543)),
    (Point(411, 489), Point(411, 507)),
    (Point(411, 379), Point(411, 398)),
    (Point(298, 489), Point(298, 507)),
    (Point(71, 580), Point(71, 598)),
    (Point(128, 489), Point(128, 507)),
    (Point(241, 671), Point(241, 689)),
    (Point(468, 227), Point(468, 271)),
    (Point(184, 416), Point(184, 434)),
    (Point(71, 507), Point(71, 525)),
    (Point(71, 653), Point(71, 671)),
    (Point(71, 671), Point(71, 689)),
    (Point(411, 635), Point(411, 653)),
    (Point(128, 616), Point(128, 634)),
    (Point(184, 343), Point(184, 361)),
    (Point(241, 379), Point(241, 398)),
    (Point(241, 288), Point(241, 306)),
    (Point(468, 580), Point(468, 598)),
    (Point(184, 507), Point(184, 525)),
    (Point(241, 616), Point(241, 634)),
    (Point(411, 470), Point(411, 488)),
    (Point(128, 416), Point(128, 434)),
    (Point(128, 562), Point(128, 580)),
    (Point(128, 580), Point(128, 598)),
    (Point(354, 543), Point(354, 561)),
    (Point(128, 470), Point(128, 488)),
    (Point(411, 598), Point(411, 616)),
    (Point(71, 543), Point(71, 562)),
    (Point(354, 271), Point(354, 288)),
    (Point(241, 398), Point(241, 416)),
    (Point(128, 489), Point(184, 489)),
    (Point(184, 489), Point(184, 507)),
    (Point(354, 435), Point(354, 452)),
    (Point(128, 507), Point(128, 525)),
    (Point(354, 343), Point(354, 361)),
    (Point(71, 689), Point(71, 707)),
    (Point(468, 361), Point(525, 361)),
    (Point(411, 288), Point(411, 306)),
    (Point(184, 379), Point(184, 398)),
    (Point(524, 227), Point(524, 271)),
    (Point(354, 707), Point(525, 707)),
    (Point(184, 525), Point(184, 543)),
    (Point(298, 379), Point(298, 398)),
    (Point(71, 343), Point(71, 361)),
    (Point(354, 362), Point(354, 379)),
    (Point(71, 616), Point(71, 634)),
    (Point(411, 306), Point(411, 325)),
    (Point(71, 227), Point(524, 227)),
    (Point(71, 271), Point(524, 271)),
    (Point(524, 435), Point(524, 452)),
    (Point(184, 227), Point(184, 271)),
    (Point(-36, 146), Point(368, 146)),
    (Point(71, 183), Point(71, 227)),
    (Point(128, 379), Point(128, 398)),
    (Point(354, 489), Point(354, 507)),
    (Point(71, 470), Point(71, 488)),
    (Point(468, 306), Point(468, 325)),
    (Point(70, 489), Point(128, 489)),
    (Point(128, 525), Point(128, 543)),
    (Point(122, 794), Point(122, 814)),
    (Point(128, 671), Point(128, 689)),
    (Point(468, 543), Point(468, 561)),
    (Point(184, 470), Point(184, 488)),
    (Point(184, 671), Point(184, 689)),
    (Point(128, 689), Point(128, 707)),
    (Point(524, 543), Point(524, 561)),
    (Point(298, 183), Point(298, 226)),
    (Point(71, 416), Point(71, 434)),
    (Point(71, 434), Point(71, 452)),
    (Point(468, 562), Point(525, 562)),
    (Point(184, 598), Point(184, 616)),
    (Point(241, 689), Point(241, 707)),
    (Point(354, 452), Point(354, 470)),
    (Point(71, 398), Point(71, 416)),
    (Point(71, 361), Point(71, 379)),
    (Point(411, 435), Point(411, 452)),
    (Point(411, 489), Point(468, 489)),
    (Point(468, 489), Point(525, 489)),
    (Point(524, 653), Point(524, 671)),
    (Point(524, 671), Point(524, 689)),
    (Point(298, 288), Point(298, 306)),
    (Point(524, 635), Point(524, 653)),
    (Point(298, 361), Point(298, 379)),
]
