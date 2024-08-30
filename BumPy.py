def checkForBUM(tal, bumtal):
    if tal % bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False

bum = int(input('Vælg et bumtal: '))

tur = 1

for i in range(1, 51):
    valg = input('Tal eller bum? ')

    if checkForBUM(i, bum):
        korrekt = 'bum'
    else:
        korrekt = str(i)

    # Kontroller spillerens indtastning
    if valg == korrekt:
        print('Korrekt!')
    else:
        print('Forkert!')

    # Skift spiller
    if tur == 1:
        tur = 2
    else:
        tur = 1
