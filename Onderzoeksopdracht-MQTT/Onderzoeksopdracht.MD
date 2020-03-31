# Onderzoeksopdracht - MQTT

## Inhoudstabel

- **Inleiding**
- **Algemene Informatie**
- **Hoe werkt het**
- **Voordelen**
- **Waar wordt het gebruikt**
- **Bronnen**

## Inleiding
Wat is Mqtt? Waar wordt het gebruikt? Hoe werkt het precies? dat zijn allemaal vragen die in deze onderzoeksopdracht beantwoord zullen worden.

## Algemene informatie
MQTT staat voor **M**essage **Q**ueuing **T**elemetry **T**ransport. Het is een internet protocol opgericht door het bedrijf OASIS (Organization for the Advancement of Structured Information Standards), een non-profit organisatie die vooral bezig is met het ontwerpen van open standaarden omtrent heel veel zaken zoals Internet of Things, energie, beveiligingen en zo verder.

De eerste versie van het protocol verscheen in het jaar 1999 en werd toen gebruik om een olie pijplijn te controleren in de woestijn. In 2013 heeft IBM interesse gekregen in het protocol en heeft meegeholpen aan het ontwikkelen ervan.

Het hoofddoel van dit protocol is om toestellen dichter bij elkaar te brengen en meer automatisering mogelijk te maken zodat het gemakkelijker wordt voor de eindgebruiker. Denk maar aan de slimme thermostaten, koelkasten, ... 

## Hoe werkt het?
![hoe het werkt](/photos/Knipsel2.PNG)

De MQTT is een systeem waarmee gebruikers makkelijk commando's kunnen schrijven en berichten kunnen ontvangen door middel van een client. Het is ontworpen voor toestellen met een lage "bandwidth". De bandwidth van een toestel slaat op de maximum data overdrachtsnelheid van een internetverbinding of op hoeveel gegevens er door een specifieke verbinding kan stromen. Doordat het bedoeld is voor toestellen met een lage bandiwdth is het de ideale oplossing voor een applicatie van Internet of Things.

De MQTT is zo simpel mogelijk gemaakt om gemakkelijk communicatie te maken tussen verschillene toestellen door zijn simple messaging protocol.

Een voorbeeld in de praktijk:
> Stel je wilt de temperatuur weten in jouw eigen slimme ijskast. Dit kan door een commando te versturen naar een broker of ontvanger van commando's, die dat op zijn beurt verwerkt en laat uitvoeren. Dan stuurt die broker het gewenste resultaat terug door naar de eindgebruiker.

## Wat kun je er meedoen
Zoals eerder gezegd is de MQTT geschikt voor toestellen die te maken hebben met Internet of Things. Dit doordat het geschikt is voor toestellen met een lage bandwidth. Het is dus zeker bruikbaar voor toestellen binnenshuis maar ook evengoed voor toestellen in de industrie. Je kunt er bijvoorbeeld makkelijk een output controleren (bijvoorbeeld: een lamp) doormiddel van een commando.

De communicatie tussen verschillende toestellen gebeurd via Messages. Deze messages gaan van het ene toestel naar het andere en bevat allerlei informatie zoals commando's of gegevens. Die gegevens kan het toestel dan lezen van bijvoorbeeld een sensor en deze data op zijn beurt weer publiceren of terugsturen naar de eindgebruiker.

Er zijn 4 grote pijlers i.v.m. wat je met de MQTT kunt doen:

### **Publiceren en subscriben**
Hier kan het toestel berichten publiceren via andere toestellen of kan een toestel zich linken op een onderwerp van een ander toestel om zo specifieke berichten te krijgen. Dit vloeit verder voort in de topics.

### **Onderwerpen of Topics**
Bij de topics specifieer je waar je alles wilt publiceren. Als je bijvoorbeeld een lamp wilt aanzetten in je huis maar alleen in de bureau. Dan moet je in een interface daarnaar gemakkelijk kunnen zoeken. Daar komen dus topics bij te pas. Ze zorgen dat alles mooi geordend is en makkelijk te gebruiken.

Zo ziet een Topic er uit:
![Voorbeeld van een Topic](/photos/Knipsel.PNG)

### **Broker**
De Broker ofwel server, is verantwoordelijk voor het ontvangen van alle berichten van de client. Het filtert de berichten en zorgt ervoor dat alle berichten bij de juiste subscribers komt. Een voorbeeld van een Broker is een Mosquitto, geschikt voor de Raspberry Pi.

## Wat zijn de voordelen?
- Er zijn heel wat voordelen aan de MQTT. Omdat het een lightweight protocol is is het heel gemakkelijk om te implementeren in software want het heeft een heel snele data overdracht.
- Het gebruikt weinig netwerk doordat het weinig gegevens doorstuurt.
- Het is energiezuinig waardoor de batterij van het toestel langer meegaat.
- En misschien het belangrijkste, het is real-time.
- Het is sneller dan het HTTP protocol omdat het kleinere data paketten moet doorsturen.
- ...

## Waar wordt het gebruikt
Het MQTT protocol wordt al veel gebruikt in allerlei Internet of Things toestellen. Het is de bedoeling dat dit alsmaar meer en meer wordt gebruikt in de toekomst. De mogelijkheden met het protocol zijn eindeloss, zo kun je bijvoorbeeld een slimme thermostaat notificaties laten sturen naar uw gsm als hij te laag staat of er een error is. 

Een aantal voorbeelden van waar het MQTT protocol wordt gebruikt:
- [Freight Farm](https://blog.heroku.com/freight-farms-on-heroku)
- [IP pinger swarm](https://plumbery.readthedocs.io/en/latest/tutorial.mqtt.pinger.swarm.html)
- [Owntracks location tracking](https://owntracks.org/booklet/guide/whathow/)
- Facebook Messenger

## Bronnen

- Santos, R. (2017) What is MQTT and How It Works. [31.03.2020, randomnerdtutorials: https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/]
- MQTT. (03.06.2013) [31.03.2020, Wikipedia: https://en.wikipedia.org/wiki/MQTT]
- OASIS (organization). (20.07.2006) [31.03.2020, Wikipedia: https://en.wikipedia.org/wiki/OASIS_(organization)]
- AMR. (04.07.2018) mqtt-protocol. [31.03.2020, 1sheeld: https://1sheeld.com/mqtt-protocol/?__cf_chl_jschl_tk__=536191d609e818aabca7b6dabc83a289f6f43c3d-1585681397-0-AZpy7Y0Zr0qpslxq7RybS8E5DMVZiry33conqDUaXN2U4RKZ0XD86VR3cU1X-2XV0KQ1NNwUc8aONELCyGujvNZz1WuqwWvRFdNo5WOE-aASLygIv9BFEMf0yg4Hd_st-cOXBprv7RctDuAyLj1vge28YDnRoHx1Ot2aLiu-Qo1k9pYAt7I0vXmXAK48gNMGSj7ir9fcbCGLbRhyUi7B3e0Gtuht7yWjeBnAkUf9VLexRvRTvXQVWoELizPudUBN-qGiDCZIrs1v2Luu_KgAg0gAs_Uhd_EiSKPeN0VoOn_d]
- Cope, S. (2016) Beginners Guide To The MQTT Protocol. [31.03.2020, steves-internet-guide: http://www.steves-internet-guide.com/mqtt/]





