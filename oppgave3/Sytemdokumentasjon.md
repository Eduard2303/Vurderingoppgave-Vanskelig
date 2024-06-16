# Systemdokumentasjon Oppgave 3

## Problemer og delproblemer.
Etter å ha sett på noen videoer om hvordan du kan bruke dfs for å navigere en maze har jeg kommet fram til noen problemer og del problemer. Oppgaver spør bare om å sjekke om mazen er gyldig eller ikke.

### Problem
Gå gjennom hver av cellene fra start cellen til slutt cellen. Hvis vi kommer oss til slutt cellen så er mazen gyldig.
### Delproblemer
1. Bruke en algoritme som starter på start cellen og sjekker cellene opp, ned, høyre, venstre.
2. Programmet må sjekken om cellen er inn i mazen og hvis cellen ikke er en vegg.
3. Programmet må lagre cellene som har blitt besøket og cellen som skal besøkes.
4. Hvis programmet kommer til slutt cellen så er mazen gyldig. Hvis vi har ingen andre celler å sjekke og vi har ikke kommet til slutt cellen så er maze ikke gyldig.
## Lage flytdiagram
**SE flytskjema oppgave3.png**

## Lage pseudokode
### Først lager vi en funksjon for å finne naboer. og legge dem til en liste.
```python
def besøkenaboer(rad, Kollone): #Tar som arguneter rad og kollone vi er på.
#Vi kan lage noen direction vertorer for opp ned høyre venstre.
    radvektor = [-1, +1, 0, 0] 
    Kollonevektor = [0, 0, +1, -1]  
    for step in range(4): #loop kjører 4 ganger for opp ned høyre venstre.
        radmove = rad + radvektor[step] # lager en move 
        Kollonemove = Kollone + Kollonevektor[step] 

        if 0 <= radmove < len(maze) and 0 <= Kollonemove < len(maze[0]) #sjeker og rad eller colloumm er innafor maze. 
            if graph[radmove][Kollonemove] != 0: #Sjekker om celle er stein.
                if markertmaze[radmove][Kollonemove]: #Sjekker om den er i markert maze.
                    moves.append([radmove, Kollonemove])
    return moves
```
### Så lager vi hoved funksjonen.
```Python
def dfs(maze,rad,kollone):
    if rad == (len(graph) -1) and kollone == (len(graph[0]) -1):
        return True #Sjekker om rad og kollone er slutt kordinatene.
    
    marked_maze[rad][Kollone] = True # Vi lagrer i array en at denne palssen er explored.

    next_paths = find_neighbours(graph, row, column) #Bruker funksjonen for å finne naoboene.  

    
    for path in next_paths: #Går gjennom her eneste vei, hvis det er ingen flere plaser å gå til går vi til bake til forige funksjon i call stacken.(recursivly). Helt til vi har kommet til en annen vei eller til det ikke er noen veier lengere. 
        if dfs(graph, path[0], path[1]): ### Hvis vi har kommet til slutt plasen så er maze gyldig.
            return True 
	#Ellers så er maze ugyldig.
    return False
```

## Beskrive kodeflyt

***Sjekk .py og .c fil ene for komentarer.***