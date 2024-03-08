Maze = [ 

[2, 0, 1, 1, 1, 1, 0, 1, 1, 1] ,

[1, 0, 1, 0, 1, 1, 1, 0, 1, 1] ,

[1, 1, 1, 0, 1, 1, 0, 1, 0, 1] ,

[0, 0, 0, 0, 1, 0, 0, 0, 0, 1] ,

[1, 1, 1, 0, 1, 1, 1, 0, 1, 0] ,

[1, 0, 1, 1, 1, 1, 0, 1, 0, 0] ,

[1, 0, 1, 0, 0, 0, 0, 0, 0, 1] ,

[1, 0, 1, 1, 1, 1, 0, 1, 1, 1] ,

[1, 1, 0, 0, 0, 1, 1, 1, 0, 4]

]

rowes = len(Maze) #Lenght av maze blir antall lister. 
collums = len(Maze[0]) #Finne lengden på en av listene for å finne antall kolonner. (Alle listene er like lange)

m = rowes*collums #Antall plasser i maze.

sr, sc = 0, 0 #Start row og start collum.

rq, cq = [], [] #lager to forskjeliger queue for row og collums. Bruker bare enlke lister.

move_count = 0 #Lagre hvor mange moves vi har brukt.
nodes_left_in_layer = 1 
nodes_in_next_layer = 0 

reached_end = False # bool hvis blir ferdig tidlig.

visited = [] # liste av besøkede plasser

def read(r,c):
    Maze[0[0]]


def explore_neighbours(r, c): #funk for å skjekke de narmeste plassene. r, c er nåværende posisjon.
    global visited, rq, cq, Maze, nodes_in_next_layer #Henter global vairblene
    dr = [-1, +1, 0, 0] 
    dc = [0, 0, +1, -1]    
    for i in range(4): #Sjekker alle 4 fire nærmeste plassene. 0 ned, 1 opp, 2 høyre, 3 venstre
        rr = r + dr[i]   # eks r,c = 0,0 for å go ned bruker vi plass nummer 0 i dr og dc blir 0+-1 og c+0 = 1,0
        cc = c + dc[i]

        print(rr,cc, (Maze[rr])[cc])
        if [rr,cc] in visited: #Hvis er besøket trenger vi ikke å besøke igjen.
            continue
        elif  (Maze[rr])[cc] == 0: #Hvis er en vegg kan vi ikke besøke den.
            continue
        
        rq.append(rr) #legger radene til slutten av rad queue.
        rq.append(cc) #legger radene til slutten av collum queue.
        visited.append([rr,cc]) #legger radene og collum til radene som er besøket.
        nodes_in_next_layer =+ 1


explore_neighbours(3,2)