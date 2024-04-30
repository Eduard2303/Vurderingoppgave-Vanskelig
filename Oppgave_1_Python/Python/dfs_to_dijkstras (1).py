from time import sleep

matrix = [
[ 1, 1, 11 ] ,
[ 4, 5, 1 ] ,
[ 7, 8, 9 ]
]

matrix = [
[ 1, 8, 921, 238, 366, 938, 246, 940, 736, 585 ] ,
[ 36, 9, 161, 717, 224, 489, 141, 160, 496, 838 ] ,
[ 389, 22, 766, 19, 498, 655, 727, 130, 279, 392 ] ,
[ 667, 220, 1, 581, 468, 96, 495, 169, 134, 14 ] ,
[ 279, 30, 786, 780, 306, 533, 498, 637, 344, 599 ] ,
[ 896, 224, 521, 948, 467, 208, 791, 371, 739, 48 ] ,
[ 505, 592, 465, 586, 714, 540, 758, 488, 130, 609 ] ,
[ 190, 851, 153, 433, 644, 444, 441, 401, 666, 118 ] ,
[ 432, 662, 497, 926, 646, 686, 722, 196, 60, 854 ] ,
[ 494, 818, 815, 355, 63, 778, 914, 812, 900, 999 ]
]



def draw_maze(maze, row, column, path):
    maze_string = ""

    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            if ( (row == len(maze)-1 and column == len(maze[0])-1) and (i == len(maze)-1 and j == len(maze[0])-1) ) :
                maze_string += f"\033[92m{maze[i][j]}\033[00m, "
            elif (row == i and column == j):
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks current Vertex
            elif [i, j] in path:
                maze_string += f"\033[91m{maze[i][j]}\033[00m, " # Marks already visited vertexes, [IN current path] "See explored_paths.pop()" in dfs()
            elif i == 0 and j == 0:
                maze_string += f"\033[92m{maze[0][0]}\033[00m, " # Marks the starting point 
            else:
                maze_string += f"{maze[i][j]}, "

        maze_string += f"\n"
    

    #print(f"{maze_string}", end='\r')
    #sleep(0.2)
    #for line in maze_string.splitlines():
    #    print("\033[1A", end="\x1b[2K")

    #sleep(0.2)
    print(f"{maze_string}", end='\r')
    print("---------------------")

def find_neighbours(graph, row, column):
    ### Checks if index exists
    ### Row vertecies represents the direction (DOWN) and the column_vertecies the direction (RIGHT)
    ### THEN we return valid_paths AKA all the directions we can move in from the specified vertecy

    row_vertecies = [+1, 0]
    column_vertecies = [0, +1]

    valid_paths = []

    for direction in range(0, 2):
        next_row = row + row_vertecies[direction]
        next_column = column + column_vertecies[direction]

        if ( (0 <= next_row < len(graph)) and (0 <= next_column < len(graph[0])) ):
            valid_paths.append([next_row, next_column])

    return valid_paths

def dijkstras(graph, row, column): ### Row + Collumn representing the vertex 
    global current_cost
    global current_path
    global shortest_path
    
    if row == (len(graph) -1) and column == (len(graph[0]) -1): ### Returns True when last vertex in maze is hit
        if current_cost < shortest_path["cost"]: ### Change from "<" to ">" for highest cost
            shortest_path["path"] = current_path.copy() ### Use copy, OR else shortest_path["path"] will be BOUND to the current_path
            shortest_path["cost"] = current_cost
        return True
    
    next_paths = find_neighbours(graph, row, column)

    
    for path in next_paths: ### Explores every path possible, but if there are no more vertixes to visit go back (recursivly) until you can visit one or if paths are depleted
        current_path.append( [path[0], path[1]] )
        current_cost += graph[current_path[-1][0]][current_path[-1][1]]


        #draw_maze(graph, path[0], path[1], current_path)

        if dijkstras(graph, path[0], path[1]): ### IF last vertex is hit:
            
            current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
            current_path.pop()

    
    try:
        current_cost -= graph[current_path[-1][0]][current_path[-1][1]]
        current_path.pop()
    except:
        return shortest_path
    
    #return True ### This makes the program go back until it finds more paths
            


## if new_path has-less-cost than old path, replace shortest_path
shortest_path = {
    "path": [],
    "cost": 99999 # Change to 0 for highest path
}


explored_paths = []

current_path = []
current_cost = matrix[0][0]

result = dijkstras(matrix, 0, 0)

print(result)
draw_maze(matrix, 0, 0, result["path"])

