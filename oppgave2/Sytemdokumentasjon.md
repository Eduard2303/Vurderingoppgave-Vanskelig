# Systemdokumentasjon Oppgave 1

## Problemer og delproblemer

### Problem
Vi må gå fra første celle i venste hjørne til siste celle venstre hjørne men vi skal kun gå gjennom cellene som går innom de miste cellene.
### Delproblemer
1. Bruke en algoritme som starter på start cellen og sjekker cellene ned, ned venstre og ned høyre.
2. Programmet må lagre veien vi har gått til sånn at vi kan sammenligne de forsjelige veiene får å finne den korteste.
3. Programmet forsetter helt til vi har sjekket alle veiene.
## Lage flytdiagram

**SE flytskjema oppgave1.png**

## Lage pseudokode

```rust
// Hovedfunksjon: Dijkstra's Algoritme
funksjon Dijkstras():
    // Basis tilfelle: Hvis vi er ved slutten
    hvis nåværende_posisjon er slutt:
        hvis nåværende_kostnad < korteste_vei:
            // Lagre nåværende vei som korteste vei
            korteste_vei = nåværende_vei
        return
    
    // Finn naboer til nåværende posisjon
    naboer = finn_naboer(nåværende_posisjon)
    
    for hver nabo i naboer:
        // Legg til naboen til nåværende vei og oppdater kostnaden
        nåværende_vei.append(nabo)
        nåværende_kostnad += kostnad(nabo)
        
        // Kall rekursivt Dijkstra's algoritme
        Dijkstras()
        
        // Etter retur, gå tilbake ved å fjerne naboen fra veien og trekke fra kostnaden
        nåværende_kostnad -= kostnad(nabo)
        nåværende_vei.pop()
    
    // Sjekk om det er flere veier å utforske
    hvis ingen flere veier:
        return korteste_vei


// Funksjon: Finn naboer
funksjon finn_naboer(posisjon):
    naboer = []
    
    // Loop gjennom mulige posisjoner
    for hver vektor_posisjon i vektor_posisjoner:
        // Sjekk om raden og kolonnen er innenfor labyrintens grenser
        hvis rad og kolonne er innenfor labyrintens grenser:
            // Legg raden og kolonnen til naboer-listen
            naboer.append([rad, kolonne])
        
        // Sjekk om loopen er ferdig
        hvis loop er ferdig:
            return naboer
```

## Beskrive kodeflyt

***Sjekk .py og .c fil ene for komentarer.***