Maze = [ 

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


class validateMaze:

    def __init__(self,Maze) -> None:
        
        self.rowes = len(Maze) #Lenght av maze blir antall lister. 
        self.collums = len(Maze[0]) #Finne lengden på en av listene for å finne antall kolonner. (Alle listene er like lange)
        self.mSize = self.rowes*self.collums #Antall plasser i maze.
        self.startRow, self.startCollum = 0, 0 #Start row og start collum.
        self.rowQueue, self.collumQueue = [], [] #lager to forskjeliger queue for row og collums. Bruker bare enlke lister.
        self.maze = Maze
        #move_count = 0 #Lagre hvor mange moves vi har brukt.
        #self.nodes_left_in_layer = 1 
        #self.nodes_in_next_layer = 0 
        self.reached_end = False # bool hvis blir ferdig tidlig.

        self.visited = [] # liste av besøkede plasser

    def explore_neighbours(self,r,c): #funk for å skjekke de narmeste plassene. r, c er nåværende posisjon.
         #Henter global vairblene
        rowVector = [-1, +1, 0, 0] 
        collumVector = [0, 0, +1, -1]    
        for i in range(4): #Sjekker alle 4 fire nærmeste plassene. 0 ned, 1 opp, 2 høyre, 3 venstre
            newRow = r + rowVector[i]   # eks r,c = 0,0 for å go ned bruker vi plass nummer 0 i dr og dc blir 0+-1 og c+0 = 1,0
            newCollum = c + collumVector[i]

            print(newRow,newCollum)
            if [newRow,newCollum] in self.visited: #Hvis er besøket trenger vi ikke å besøke igjen.
                continue
            elif  (self.maze[newRow])[newCollum] == 0: #Hvis er en vegg kan vi ikke besøke den.
                continue
            
            self.rowQueue.append(newRow) #legger radene til slutten av rad queue.
            self.collumQueue.append(newCollum) #legger radene til slutten av collum queue.
            self.visited.append([newRow,newCollum]) #legger radene og collum til radene som er besøket.
            #self.nodes_in_next_layer =+ 1