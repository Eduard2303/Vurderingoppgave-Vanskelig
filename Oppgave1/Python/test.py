import heapq
array = [
[1, 1, 1] ,

[4, 5, 1] ,

[7, 8, 9]
]

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



def getn(array): #Funksjon for å få antall elementer i matrisen
    lines = len(array) #Finne antall linjer
    collums = len(array[0]) #antall coloner
    return lines*collums  #Fordi herver linje har like mange kolonner så kan vi bare mutiplisere linjer og kolloner.

def dijkstra(g, n, s, e): #Jeg bruker Dilkstra shortest path alorithm for å gå gjenom matrisen.
    pass

array_n = getn(array)
array_g = array
array_s = (0,0)
array_e = (3,3)
array1_n = getn(array1)
array1_g = array1
array1_s = (0,0)

infinity = float('inf')
neg_infinity = float('-inf')
