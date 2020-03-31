# Onderzoeksopdracht - MQTT

## Inhoudstabel

- **Inleiding**
- **Algemene Informatie**
- **Hoe werkt het**
- **Waar wordt het gebruikt**
- **Bronnen**

## Inleiding
Wat is Mqtt? Waar wordt het gebruikt? Hoe werkt het precies? dat zijn allemaal vragen die in deze onderzoeksopdracht beantwoord zullen worden.

## Algemene informatie
MQTT staat voor **M**essage **Q**ueuing **T**elemetry **T**ransport. Het is een internet protocol opgericht door het bedrijf OASIS (Organization for the Advancement of Structured Information Standards), een non-profit organisatie die vooral bezig is met het ontwerpen van open standaarden omtrent heel veel zaken zoals Internet of Things, energie, beveiligingen en zo verder.

De eerste versie van het protocol verscheen in het jaar 1999 en werd toen gebruik om een olie pijplijn te controleren in de woestijn. In 2013 heeft IBM interesse gekregen in het protocol en heeft meegeholpen aan het ontwikkelen ervan.

## Hoe werkt het?
De MQTT is een systeem waarmee gebruikers makkelijk boodschappen kunnen publiceren en ontvangen door middel van een client. Het is ontworpen voor toestellen met een lage "bandwidth". De bandwidth van een toestel slaat op de maximum data overdrachtsnelheid van een internetverbinding of op hoeveel gegevens er door een specifieke verbinding kan stromen. Doordat het bedoeld is voor toestellen met een lage bandiwdth is het de ideale oplossing voor een applicatie van Internet of Things.

De MQTT is zo simpel mogelijk gemaakt om gemakkelijk communicatie te maken tussen verschillene toestellen door zijn simple messaging protocol.

## Wat kun je er meedoen
Zoals eerder gezegd is de MQTT geschikt voor toestellen die te maken hebben met Internet of Things. Dit doordat het geschikt is voor toestellen met een lage bandwidth. Je kunt er bijvoorbeeld makkelijk een output controleren (bijvoorbeeld: een lamp) doormiddel van een commando.

De communicatie tussen verschillende toestellen gebeurd via Messages. Deze messages gaan van het ene toestel naar het andere en bevat allerlei informatie zoals commando's of gegevens. Die gegevens kan het toestel dan lezen van bijvoorbeeld een sensor en deze data op zijn beurt weer publiceren.

Er zijn 4 grote pijlers i.v.m. wat je met de MQTT kunt doen:

### **Publiceren en subscriben**
Hier kan het toestel berichten publiceren via andere toestellen of kan een toestel zich linken op een onderwerp van een ander toestel om zo specifieke berichten te krijgen. Dit vloeit verder voort in de topics.

### **Onderwerpen of Topics**
Bij de topics specifieer je waar je alles wilt publiceren. Als je bijvoorbeeld een lamp wilt aanzetten in je huis maar alleen in de bureau. Dan moet je in een interface daarnaar gemakkelijk kunnen zoeken. Daar komen dus topics bij te pas. Ze zorgen dat alles mooi geordend is en makkelijk te gebruiken.

Zo ziet een Topic er uit:
![Voorbeeld van een Topic](/photos/Knipsel.PNG)

### **Broker**
De Broker is verantwoordelijk voor het ontvangen van alle berichten van de client. Het filtert de berichten en zorgt ervoor dat alle berichten bij de juiste subscribers komt. Een voorbeeld van een Broker is een Mosquitto, geschikt voor de Raspberry Pi.

## Waar wordt het gebruikt?

