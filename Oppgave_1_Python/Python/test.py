import heapq
array = [
[1, 1, 1] ,

[4, 5, 1] ,

[7, 8, 9]
]
global posinf 
posinf = float('inf')
global nodecount
nodecount = 0 

class node:    
    def __init__(self,xpos,ypos):
        self.pos = [xpos,ypos]
        self.distance = posinf        

def create_nodes(array):
    
    for row in range(0, len(array)):
        for collum in range(0, len(array[row])):
            h = node(row,collum)