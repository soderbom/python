#Random för att slumpa fram värden och math för att begränsa antalet decimaler
import random as rd
import math

#Funktionen genererar rätvinkliga trianglar. Värden är justerade om kateten ska beräknas (undviker negativ rot)
def generate_triangle(calc_cat):
    if calc_cat:
        a = rd.randint(1, 21)
        b = rd.randint(1, 21)
        c = round(math.sqrt(a*a + b*b), 1) 
    else:
        a = rd.randint(1, 12)
        c = rd.randint(15, 21)
        b = round(math.sqrt(c*c - a*a), 1)
        
    #Skickar tillbaka kateter, hypotenusa och vilken enhet uppgiften är skriven i
    unit = rd.choice(['mm', 'cm', 'm'])
    return a, b, c, unit


#Funktion för att generera uppgifter där vi ska avgöra om triangeln är rätvinklig eller inte. Vi genererar en triangel och sätter in värden för kateter och hypotenusa i en sträng.
#Strängen och svaret skickas tillbaka för att skrivas till fil
def check_if_right_triangle():
    right_triangle = rd.choice([True, False])
    if right_triangle:
        a, b, c, unit = generate_triangle(True)
        return 'Är triangeln rätvinklig?\n\tKateter: {} {} och {} {}\n\tHypotenusa: {} {}'.format(a, unit, b, unit, c, unit), "Ja, triangeln är rätvinklig."
    else:
        a, b, c, unit = generate_triangle(True)
        b += rd.randint(1,7)        #Förändrar en katets längd för att generera en triangel som inte är rätvinklig
        return 'Är triangeln rätvinklig?\n\tKateter: {} {} och {} {}\n\tHypotenusa: {} {}'.format(a, unit, b, unit, c, unit), "Nej, triangeln är inte rätvinklig."


#Genererar en uppgift där kateterna är kända
#Funktionen skickar tillbaka uppgiften, hypotenusans längd och enheten för uppgiften 
def generate_problem_cathetus():
    a, b, c, unit = generate_triangle(True)
    return 'Beräkna hypotenusan för en triangel med kateterna {} {} och {} {}.'.format(a, unit, b, unit), c, unit


#Genererar en uppgift där hypotenusan och en katet är kända
#Funktionen skickar tillbaka uppgiften, den okända katetens längd och enheten för uppgiften 
def generate_problem_hypotenuse():
    a, b, c, unit = generate_triangle(False)
    return 'Beräkna kateten hos en triangel vars ena katet är {} {} och dess hypotenusa är {} {}.'.format(a, unit, c, unit), b, unit


number_of_questions = 10

#Skapar två filer. Ett uppgiftsblad och ett facit
questions = open("uppgifter.txt", "w")
answers = open("facit.txt", "w")


#Loopen slumpar ordningen frågorna kommer i för att det inte ska bli för repetitivt och skriver dem till uppgiftsbladet och facit
for i in range(1, number_of_questions+1):
    randomizer = rd.randint(1, 3)
    if randomizer == 1:
        question, answer, unit = generate_problem_cathetus()
        questions.write("{}. {}".format(i, question))
        answers.write("{}. Svar: {} {}".format(i, answer, unit))
    elif randomizer == 2:
        question, answer = check_if_right_triangle()
        questions.write("{}. {}".format(i, question))
        answers.write("{}. {}".format(i, answer))
    else:
        question, answer, unit = generate_problem_hypotenuse()
        questions.write("{}. {}".format(i, question))
        answers.write("{}. Svar: {} {}".format(i, answer, unit))

    #Tre mellanslag för att snygga till filen
    questions.write("\n\n\n")
    answers.write("\n\n\n")
    
#Stänger filerna
questions.close()
answers.close()
