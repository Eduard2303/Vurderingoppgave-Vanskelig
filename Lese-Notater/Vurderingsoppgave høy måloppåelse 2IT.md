Du skal levere svar på oppgavene i minst to programmeringsspråk. Du kan levere med besvarelser med flere.

Merk: Systemdokumentasjon jeg ønsker for løsningene er begrenset til.

- Beskrive problem og delproblemer
- Lage flytdiagram
- Lage pseudokode
- Beskrive kodeflyt

**Du vil bli hørt muntlig for forståelse av løsning etter innlevering. Det er forståelsen av løsningen som er grunnlag for karakter, ikke innlevert kode.**

**Oppgave 1)** 20 poeng Lag et program som beveger seg fra første element i første rad i en matrise til siste element i siste rad i en matrise. Du kan bare bevege deg nedover og til høyre i matrisen.

array = [

[1, 1, 1] ,

[4, 5, 1] ,

[7, 8, 9]

]

a) Finn den veien som ved å summere alle tall du går innom gir den laveste summen.

b) Finn den veien som ved å summere alle tall du går innom gir den høyeste summen .

Lag systemdokumentasjon

Vis resultat for disse matrisene

array1 = [

[1, 8, 921, 238, 366, 938, 246, 940, 736, 585] ,

[36, 9, 161, 717, 224, 489, 141, 160, 496, 838] ,

[389, 22, 766, 19, 498, 655, 727, 130, 279, 392] ,

[667, 220, 1, 581, 468, 96, 495, 169, 134, 14] ,

[279, 30, 786, 780, 306, 533, 498, 637, 344, 599] ,

[896, 224, 521, 948, 467, 208, 791, 371, 739, 48] ,

[505, 592, 465, 586, 714, 540, 758, 488, 130, 609] ,

[190, 851, 153, 433, 644, 444, 441, 401, 666, 118] ,

[432, 662, 497, 926, 646, 686, 722, 196, 60, 854] ,

[494, 818, 815, 355, 63, 778, 914, 812, 900, 999]

]

array2= [

[272, 362, 965, 995, 603, 909, 758, 390, 709, 693] ,

[665, 600, 806, 201, 905, 688, 294, 860, 6, 501] ,

[362, 454, 902, 479, 632, 78, 469, 255, 650, 755] ,

[337, 927, 535, 858, 839, 236, 813, 457, 360, 482] ,

[153, 742, 367, 793, 749, 870, 413, 81, 961, 165] ,

[937, 88, 291, 35, 325, 580, 912, 15, 777, 779] ,

[813, 638, 641, 918, 140, 758, 755, 522, 745, 12] ,

[902, 978, 273, 9, 80, 498, 850, 863, 651, 123] ,

[262, 104, 32, 735, 780, 177, 327, 175, 667, 128] ,

[45, 344, 622, 627, 349, 184, 802, 400, 701, 550]

]

array3= [

[101, 892, 495, 633, 59, 331, 216, 352, 49, 49] ,

[925, 288, 737, 224, 734, 94, 361, 35, 826, 710] ,

[712, 133, 609, 927, 908, 725, 626, 601, 878, 773] ,

[325, 708, 968, 940, 877, 416, 115, 434, 594, 890] ,

[58, 617, 813, 127, 176, 20, 784, 565, 863, 178] ,

[405, 352, 545, 795, 216, 814, 491, 355, 516, 423] ,

[239, 776, 654, 433, 453, 644, 708, 113, 354, 404] ,

[663, 571, 0, 532, 842, 520, 874, 988, 322, 576] ,

[630, 469, 879, 609, 37, 965, 888, 277, 975, 87] ,

[337, 260, 79, 110, 428, 410, 963, 898, 517, 735]

]

array4= [

[70, 562, 376, 993, 689, 354, 369, 519, 981, 786] ,

[539, 756, 364, 445, 650, 23, 456, 901, 955, 83] ,

[259, 967, 396, 745, 810, 218, 986, 593, 360, 415] ,

[601, 479, 670, 406, 321, 845, 667, 420, 34, 853] ,

[796, 204, 548, 162, 355, 583, 611, 23, 227, 882] ,

[498, 796, 258, 851, 339, 847, 378, 330, 107, 46] ,

[548, 48, 746, 356, 115, 48, 503, 213, 80, 519] ,

[285, 260, 162, 644, 885, 916, 771, 657, 622, 92] ,

[472, 336, 931, 257, 798, 881, 911, 486, 736, 664] ,

[107, 248, 52, 958, 596, 133, 191, 960, 785, 776]

]

array5= [

[239, 493, 26, 156, 588, 424, 88, 914, 921, 494] ,

[90, 681, 600, 338, 620, 689, 149, 245, 739, 686] ,

[854, 261, 14, 761, 929, 671, 349, 615, 626, 10] ,

[965, 125, 938, 900, 764, 939, 766, 182, 274, 714] ,

[538, 288, 941, 251, 903, 80, 807, 879, 616, 891] ,

[411, 546, 273, 575, 419, 682, 357, 63, 397, 541] ,

[266, 599, 402, 972, 156, 180, 639, 83, 19, 618] ,

[62, 289, 436, 67, 29, 720, 38, 543, 775, 969] ,

[229, 316, 707, 537, 48, 297, 989, 469, 895, 191] ,

[106, 538, 652, 624, 308, 722, 17, 885, 497, 490]

]

array6= [

[571, 7, 514, 699, 399, 94, 407, 153, 941, 638] ,

[296, 39, 622, 601, 341, 986, 605, 47, 596, 543] ,

[549, 26, 117, 770, 258, 259, 433, 381, 698, 764] ,

[350, 359, 182, 344, 396, 51, 169, 418, 248, 865] ,

[827, 678, 449, 808, 176, 256, 149, 688, 561, 585] ,

[634, 999, 158, 774, 383, 274, 651, 731, 449, 660] ,

[158, 190, 985, 696, 634, 279, 484, 287, 648, 732] ,

[400, 412, 957, 317, 376, 244, 664, 732, 463, 691] ,

[544, 831, 523, 299, 149, 198, 964, 863, 502, 954] ,

[497, 793, 915, 58, 573, 120, 491, 776, 728, 291]

]

**Oppgave 2)** 30 poeng Lag et program som beveger seg fra et element i første liste til et element i siste liste. Du kan bare bruke ett tall per liste, og tallet må ha samme plass, plassen før eller plassen etter det tallet du brukte i listen over. Eks. Velger du tall 3 i liste 5 kan du bruke tall 2, 3 eller 4 i liste 6.

a) Finn den veien som ved å summere alle tall du går innom gir den laveste summen.

b) Finn den veien som ved å summere alle tall du går innom gir den høyeste summen.

Lag systemdokumentasjon

liste1 = (0)

liste2 = (2, 4 )

liste3 = (0, 5, 6 )

liste4 = (7, 2, 9, 10 )

liste5 = (25, 11, 1, 0, 5 )

liste6 = (1, 88, 51, 88, 61, 4 )

liste7 = (93, 12, 73, 36, 71, 65, 34 )

liste8 = (233, 5, 2, 1, 6, 7, 55, 1 )

liste9 = (16, 111, 213, 9, 23, 433, 1, 34, 13 )

liste10 =(5, 23, 453, 789, 123, 200, 212, 345, 556, 99 )

**Oppgave 3)** 50 poeng Finn en vei fra første tall i første tall i første rad i matrisen til siste tall i siste rad i matrisen. Du kan bare bevege deg på plasser som har tallet 1.

a) Lag et program som sjekker om maze er gyldig, og rapporterer om maze er gyldig eller ugyldig

Lag systemdokumentasjon

**Tallet 1 er der du kan gå, mens 0 representerer en vegg.**

maze = [

[1, 0, 1, 1, 1, 1, 0, 1, 1, 1] ,

[1, 0, 1, 0, 1, 1, 1, 0, 1, 1] ,

[1, 1, 1, 0, 1, 1, 0, 1, 0, 1] ,

[0, 0, 0, 0, 1, 0, 0, 0, 0, 1] ,

[1, 1, 1, 0, 1, 1, 1, 0, 1, 0] ,

[1, 0, 1, 1, 1, 1, 0, 1, 0, 0] ,

[1, 0, 1, 0, 0, 0, 0, 0, 0, 1] ,

[1, 0, 1, 1, 1, 1, 0, 1, 1, 1] ,

[1, 1, 0, 0, 0, 1, 1, 1, 0, 1]

]