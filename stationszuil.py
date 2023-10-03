import datetime
import random

def strftime():

    #haalt de tijd van vandaag op
    vandaag = datetime.datetime.today() 

    #haalt de tijd van nu op
    rn = datetime.datetime.now() 

    #%H: uren, %M: minuten, %S: seconden
    tijd = rn.strftime("%H:%M:%S") 

    #%a dag, %d datum, %b maand, %y jaar
    s = vandaag.strftime("%a %d %b %Y") 
    return s, tijd
    
def bericht():

    #allebij apart aangeroepen omdat er anders haakjes om de uitkomst komen(chaptgpt hulp)
    nu, tijd = strftime() 

    #lijst met treinstations voor de random functie
    treinstations = ['Amsterdam Centraal', 'Rotterdam Centraal', 'Utrecht Centraal', 'Den Haag Centraal', 'Eindhoven Centraal', 'Groningen', 'Maastricht', 'Hoofddorp']
    aantal_keuzes = 1

    #kies een random uit de lijst
    willekeurige_stations = random.sample(treinstations, aantal_keuzes)
    station = willekeurige_stations[0]

    #vraag om een naam
    naam = input('Vul uw naam in (Niet verplicht): ')
    if naam == "":

        #als de naam leeg wordt gelaten dan wordt er Anoniem weergegeven op de display
        naam = 'Anoniem'

    #vraag voor feedback
    message = input('Geef uw feedback: ')

    #de feedback mag max 140 tekens zijn
    if len(message) > 140:
        print('Uw bericht mag niet meer dan 140 tekens zijn')
    else:
        
        #open de file en voeg er iets aan toe
        with open('stationszuil.txt', 'a') as infile:
            infile.write(f'{nu} {tijd}, Station: {station}, {naam}, {message}\n')
            print('Uw feedback wordt weergegeven op de display')

strftime()
bericht()
