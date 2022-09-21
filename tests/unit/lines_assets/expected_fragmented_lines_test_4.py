from colibrie.geometry import Point

expected_fragmented_lines_test_4 = [
    (Point(71, 229), Point(71, 251)),
    (Point(113, 340), Point(113, 369)),
    (Point(191, 458), Point(191, 487)),
    (Point(460, 428), Point(524, 428)),
    (Point(191, 487), Point(191, 517)),
    (Point(163, 606), Point(163, 635)),
    (Point(191, 399), Point(191, 428)),
    (Point(113, 518), Point(113, 547)),
    (Point(361, 208), Point(460, 208)),
    (Point(361, 428), Point(460, 428)),
    (Point(247, 487), Point(247, 517)),
    (Point(460, 487), Point(460, 517)),
    (Point(191, 251), Point(191, 280)),
    (Point(361, 487), Point(361, 517)),
    (Point(523, 665), Point(523, 694)),
    (Point(460, 339), Point(524, 339)),
    (Point(113, 251), Point(113, 280)),
    (Point(113, 280), Point(113, 310)),
    (Point(163, 695), Point(191, 695)),
    (Point(247, 606), Point(247, 635)),
    (Point(361, 458), Point(361, 487)),
    (Point(460, 636), Point(460, 665)),
    (Point(113, 576), Point(163, 576)),
    (Point(361, 399), Point(361, 428)),
    (Point(558, 793), Point(558, 813)),
    (Point(523, 399), Point(523, 428)),
    (Point(460, 577), Point(460, 606)),
    (Point(163, 339), Point(191, 339)),
    (Point(247, 208), Point(361, 208)),
    (Point(163, 428), Point(191, 428)),
    (Point(191, 340), Point(191, 369)),
    (Point(361, 251), Point(361, 280)),
    (Point(460, 458), Point(460, 487)),
    (Point(361, 429), Point(361, 458)),
    (Point(113, 458), Point(113, 487)),
    (Point(71, 518), Point(71, 547)),
    (Point(71, 369), Point(71, 399)),
    (Point(247, 576), Point(361, 576)),
    (Point(113, 187), Point(163, 187)),
    (Point(163, 280), Point(163, 310)),
    (Point(361, 517), Point(460, 517)),
    (Point(71, 310), Point(71, 339)),
    (Point(247, 310), Point(247, 339)),
    (Point(247, 340), Point(247, 369)),
    (Point(191, 606), Point(191, 635)),
    (Point(71, 251), Point(71, 280)),
    (Point(191, 547), Point(191, 576)),
    (Point(361, 340), Point(361, 369)),
    (Point(460, 518), Point(460, 547)),
    (Point(247, 429), Point(247, 458)),
    (Point(113, 547), Point(113, 576)),
    (Point(113, 636), Point(163, 636)),
    (Point(163, 576), Point(191, 576)),
    (Point(523, 229), Point(523, 251)),
    (Point(163, 665), Point(163, 694)),
    (Point(70, 517), Point(113, 517)),
    (Point(191, 636), Point(247, 636)),
    (Point(70, 166), Point(113, 166)),
    (Point(460, 665), Point(460, 694)),
    (Point(460, 695), Point(524, 695)),
    (Point(460, 636), Point(524, 636)),
    (Point(-36, 99), Point(142, 99)),
    (Point(460, 187), Point(523, 187)),
    (Point(361, 230), Point(361, 251)),
    (Point(191, 518), Point(191, 547)),
    (Point(361, 576), Point(460, 576)),
    (Point(113, 399), Point(113, 428)),
    (Point(71, 547), Point(71, 576)),
    (Point(361, 187), Point(460, 187)),
    (Point(361, 636), Point(361, 665)),
    (Point(191, 339), Point(247, 339)),
    (Point(523, 577), Point(523, 606)),
    (Point(558, 793), Point(595, 793)),
    (Point(247, 458), Point(247, 487)),
    (Point(163, 487), Point(163, 517)),
    (Point(361, 166), Point(460, 166)),
    (Point(247, 399), Point(247, 428)),
    (Point(523, 340), Point(523, 369)),
    (Point(163, 399), Point(163, 428)),
    (Point(113, 339), Point(163, 339)),
    (Point(113, 606), Point(113, 635)),
    (Point(113, 166), Point(163, 166)),
    (Point(163, 251), Point(163, 280)),
    (Point(71, 399), Point(71, 428)),
    (Point(-13, 794), Point(122, 794)),
    (Point(523, 310), Point(523, 339)),
    (Point(163, 429), Point(163, 458)),
    (Point(523, 636), Point(523, 665)),
    (Point(113, 487), Point(113, 517)),
    (Point(247, 517), Point(361, 517)),
    (Point(460, 280), Point(460, 310)),
    (Point(191, 636), Point(191, 665)),
    (Point(361, 229), Point(460, 229)),
    (Point(71, 187), Point(113, 187)),
    (Point(163, 340), Point(163, 369)),
    (Point(113, 310), Point(113, 339)),
    (Point(460, 576), Point(524, 576)),
    (Point(247, 577), Point(247, 606)),
    (Point(191, 695), Point(247, 695)),
    (Point(191, 429), Point(191, 458)),
    (Point(523, 251), Point(523, 280)),
    (Point(191, 369), Point(191, 399)),
    (Point(113, 429), Point(113, 458)),
    (Point(163, 517), Point(191, 517)),
    (Point(460, 517), Point(524, 517)),
    (Point(191, 428), Point(247, 428)),
    (Point(70, 695), Point(113, 695)),
    (Point(-13, 794), Point(-13, 814)),
    (Point(71, 665), Point(71, 694)),
    (Point(361, 636), Point(460, 636)),
    (Point(460, 166), Point(524, 166)),
    (Point(71, 606), Point(71, 636)),
    (Point(361, 547), Point(361, 576)),
    (Point(-13, 814), Point(122, 814)),
    (Point(163, 636), Point(163, 665)),
    (Point(595, 793), Point(595, 813)),
    (Point(460, 399), Point(460, 428)),
    (Point(247, 695), Point(361, 695)),
    (Point(71, 339), Point(71, 369)),
    (Point(523, 208), Point(523, 229)),
    (Point(361, 577), Point(361, 606)),
    (Point(71, 187), Point(71, 208)),
    (Point(71, 280), Point(71, 310)),
    (Point(361, 369), Point(361, 399)),
    (Point(523, 547), Point(523, 576)),
    (Point(523, 518), Point(523, 547)),
    (Point(247, 230), Point(247, 251)),
    (Point(558, 813), Point(595, 813)),
    (Point(247, 428), Point(361, 428)),
    (Point(361, 310), Point(361, 339)),
    (Point(460, 310), Point(460, 339)),
    (Point(163, 187), Point(191, 187)),
    (Point(163, 458), Point(163, 487)),
    (Point(71, 166), Point(71, 251)),
    (Point(71, 166), Point(523, 166)),
    (Point(71, 251), Point(523, 251)),
    (Point(523, 429), Point(523, 458)),
    (Point(523, 187), Point(523, 208)),
    (Point(460, 208), Point(523, 208)),
    (Point(523, 369), Point(523, 399)),
    (Point(247, 665), Point(247, 694)),
    (Point(113, 636), Point(113, 665)),
    (Point(460, 340), Point(460, 369)),
    (Point(247, 187), Point(361, 187)),
    (Point(163, 166), Point(191, 166)),
    (Point(460, 251), Point(460, 280)),
    (Point(247, 229), Point(361, 229)),
    (Point(361, 606), Point(361, 635)),
    (Point(361, 518), Point(361, 547)),
    (Point(247, 251), Point(247, 280)),
    (Point(191, 310), Point(191, 339)),
    (Point(247, 280), Point(247, 310)),
    (Point(361, 339), Point(460, 339)),
    (Point(247, 636), Point(247, 665)),
    (Point(523, 487), Point(523, 517)),
    (Point(523, 166), Point(523, 251)),
    (Point(191, 280), Point(191, 310)),
    (Point(523, 458), Point(523, 487)),
    (Point(247, 369), Point(247, 399)),
    (Point(523, 606), Point(523, 635)),
    (Point(460, 547), Point(460, 576)),
    (Point(71, 458), Point(71, 487)),
    (Point(71, 636), Point(71, 665)),
    (Point(113, 665), Point(113, 694)),
    (Point(71, 487), Point(71, 517)),
    (Point(191, 187), Point(247, 187)),
    (Point(71, 428), Point(71, 458)),
    (Point(113, 577), Point(113, 606)),
    (Point(361, 280), Point(361, 310)),
    (Point(163, 636), Point(191, 636)),
    (Point(163, 577), Point(163, 606)),
    (Point(247, 547), Point(247, 576)),
    (Point(247, 518), Point(247, 547)),
    (Point(247, 636), Point(361, 636)),
    (Point(191, 665), Point(191, 694)),
    (Point(113, 517), Point(163, 517)),
    (Point(163, 518), Point(163, 547)),
    (Point(191, 576), Point(247, 576)),
    (Point(163, 369), Point(163, 399)),
    (Point(113, 695), Point(163, 695)),
    (Point(191, 517), Point(247, 517)),
    (Point(163, 310), Point(163, 339)),
    (Point(460, 230), Point(460, 251)),
    (Point(71, 208), Point(71, 229)),
    (Point(247, 209), Point(247, 229)),
    (Point(247, 188), Point(247, 208)),
    (Point(523, 280), Point(523, 310)),
    (Point(71, 167), Point(71, 187)),
    (Point(247, 339), Point(361, 339)),
    (Point(113, 428), Point(163, 428)),
    (Point(460, 209), Point(460, 229)),
    (Point(247, 166), Point(361, 166)),
    (Point(361, 665), Point(361, 694)),
    (Point(122, 794), Point(122, 814)),
    (Point(191, 166), Point(247, 166)),
    (Point(163, 547), Point(163, 576)),
    (Point(460, 429), Point(460, 458)),
    (Point(523, 167), Point(523, 187)),
    (Point(460, 369), Point(460, 399)),
    (Point(191, 577), Point(191, 606)),
    (Point(71, 576), Point(71, 606)),
    (Point(113, 369), Point(113, 399)),
    (Point(361, 695), Point(460, 695)),
    (Point(460, 606), Point(460, 635)),
]
