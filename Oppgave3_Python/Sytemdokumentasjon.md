# Systemdokumentasjon Oppgave 3

## Problemer og delproblemer.
Etter å ha sett på noen videoer om hvordan du kan bruke en algorthme for å navigere en maze har jeg kommet fram til noen problemer og del problemer. Oppgaver spør bare om å skjekke om mazen er gyldig eller ikke.

### Problem
Gå gjenom hver av cellene fra start cellen til slutt cellen. Hvis vi kommer oss til slutt cellen så er mazen gyldig.
### Delproblemer
1. Bruke en algorythme som starter på start cellen og sjekker cellene opp, ned, høyre, venstre.
2. Programmet må sjekken om cellen er innafor maze-en og hvis cellen ikke er en vegg.
3. Programmet fordi programmet skal ikke bare vandre til første celle til finner så legger vi cellene i en queue. Cellene som ble funnet først er cellene som vi skal gå til før vi går til de nyfunnet cellene (SE TENGNING).
4. Hvis programmet kommer til slutt cellen så er mazen gyldig. Hvis vi har ingen andre celler å sjekke og vi har ikke kommet til slutt cellen så er maze ikke gyldig.
### Lage flytdiagram
**SE flyktskjema oppgave3.png**
### Lage pseudokode
```
#Finne ut hvor mange rader og kolloner vi har.

radder = lenght(maze)
colonner = lenght(maze[rad 0])
antallceller = radder * colonner

startrad = 0  
startkollone = 0
#lage queue for rad og for kollone. Bruker bare Lister.
radqueue = []  
kollonequeue = []

#lage en funksjon for å besøke naboer.

def besøkenaboer(rad, Kollone): #Tar som arguneter rad og kollone vi er på.

#Vi kan lage noen direction vertorer for opp ned høyre venstre.
    radvektor = [-1, +1, 0, 0] # rekkefølge spiller ingen rolle. 
    collonevektor = [0, 0, +1, -1]  
    for step in range(4): #loop kjører 4 ganger for opp ned høyre venstre.
        radmove = rad + radvektor[step] # lager en move 
        collonemove = collone + collonevektor[step] 

        if: radmove in visited: #betyr at vi har alerede bøsked denne cellen.
            continue #Forsetter på neste step i loopen
        elif Maze[radmove][collonemove] = 0: #sjekker collonen er en vegg.
            continue #legget ikke til og forsetter.
        elif 
```     

### Beskrive kodeflyt

***Sjekk .py fil ene for komentarer.***