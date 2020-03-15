import random as rnd                                                                              #Det enda vi behöver är randomfunktionen. Egentligen behövs endast randint()

def write_to_file_func(first_list_of_numbers, second_list_of_numbers, method):
    space = '       '                                                                              #7 tecken för mellanslag och avdelare för att det ska matcha talens längd
    divider = '-------'
    for i in range(len(second_list_of_numbers)):                                                   #Vi skriver ut första raden av täljare
        f.write(first_list_of_numbers[i] + space)
    
    f.write('\n')                                                                                  #Retur för att kunna skriva ut nämnarna

    for i in range(len(second_list_of_numbers)):                                                   #Nedan lägger vi till korrekt räknesätt som första tecknet i strängen som representerar nämnaren. Vi måste splittra strängen till en lista, lägga till tecknet och sedan sätta ihop den igen
        s = list(second_list_of_numbers[i])
        s[0] = method
        second_list_of_numbers[i] = ''.join(s)
        f.write(second_list_of_numbers[i] + space)
    
    f.write('\n')                                                                                  #Retur för att skriva ut linjen

    for i in range(len(second_list_of_numbers)):                                                   #Skriv ut linjen
        f.write(divider + space)

    three_spaces()
    
#Alla funktioner nedan tar två argument och är byggda på samma vis. De kollar om vi vill skriva till en fil och hur många övningar vi vill ha

def create_addition(write_to_file, number_of_excercies):
    first_term = []
    second_term = []
    for i in range(number_of_excercies):
        first_term.append(str(rnd.randint(199, 1999)).rjust(7, ' '))                               #Fyll på listorna med slumpvisa tal, samt justera dessa så de har samma längd så vi får en snygg uppställning. Använd sträng för att förändra positioner
        second_term.append(str(rnd.randint(199, 1999)).rjust(7, ' '))

    if write_to_file:
        write_to_file_func(first_term, second_term, '+')                                           #Om vi vill skriva filen så skickar vi även med korrekt räknesätt
    else:
        return first_term, second_term                                                             #Annars lämnar vi bara tillbaka listorna ifall vi vill göra något annat med dem

    

def create_subtraction(write_to_file, number_of_excercies):
    first_term = []
    second_term = []
    for i in range(number_of_excercies):
        first_term.append(str(rnd.randint(1299, 1999)).rjust(7, ' '))
        second_term.append(str(rnd.randint(199, 1199)).rjust(7, ' '))                              #Justerad nämnare för lite snällare tal

    if write_to_file:
        write_to_file_func(first_term, second_term, '-')
    else:
        return first_term, second_term


def create_multiplication(write_to_file, number_of_excercies):
    first_factor = []
    second_factor = []
    for i in range(number_of_excercies):
        first_factor.append(str(rnd.randint(11, 299)).rjust(7, ' '))
        second_factor.append(str(rnd.randint(2, 99)).rjust(7, ' '))                                 #Justerad nämnare för lite snällare tal

    if write_to_file:
        write_to_file_func(first_factor, second_factor, 'x')
    else:
        return first_factor, second_factor


def create_division(write_to_file, number_of_excercies):
    first_factor = []
    second_factor = []
    for i in range(number_of_excercies):
        first_factor.append(str(rnd.randint(11, 299)).rjust(7, ' '))
        second_factor.append(str(rnd.randint(2, 10)).rjust(7, ' '))                                 #Justerad nämnare för lite snällare tal

    if write_to_file:
        write_to_file_func(first_factor, second_factor, '/')
    else:
        return first_factor, second_factor


def three_spaces():
    f.write('\n')                                                                                  #Retur x3 för att skapa utrymme till nästa rad av tal
    f.write('\n')
    f.write('\n')


f = open("math.txt", "w")                                                                           #Öppnar en fil för att skriva till
number_of_rows = 2
number_of_columns = 5

f.write('ADDITION\n\n')
for n in range(number_of_rows):                             
    create_addition(True, number_of_columns)                                                         #Lägg till addition. Du kan ändra hur många tal du vill generera, 6st passar på en sida

three_spaces()
f.write('SUBTRAKTION\n\n')

for n in range(number_of_rows):
    create_subtraction(True, number_of_columns)                                                       #Subtraktion

three_spaces()
f.write('MULTIPLIKATION\n\n')

for n in range(number_of_rows):
    create_multiplication(True, number_of_columns)                                                     #Multiplikation

three_spaces()
f.write('DIVISION\n\n')

for n in range(number_of_rows):
    create_division(True, number_of_columns)                                                            #Division


f.close()                                                                                               #Stänger filen när allt är klart