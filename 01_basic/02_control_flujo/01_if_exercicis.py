###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivell_senyal = float(input("Introdueix el nivell de senyal (dBm): "))

if nivell_senyal >= -50:
    print("Cobertura excel·lent")
elif nivell_senyal >= -67:
    print("Cobertura bona")
elif nivell_senyal >= -75:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")
# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia_optica = float(input("Introdueix la potència òptica rebuda (dBm): "))

if potencia_optica < -27:
    print("Nivell massa baix")
elif potencia_optica <= -8:
    print("Nivell acceptable")
else:
    print("Nivell massa alt")
# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum_dades = float(input("Introdueix el consum de dades en GB: "))

if consum_dades <= 20:
    print("Consum dins del límit")
else:
    print(f"Consum superat en {consum_dades - 20} GB")
# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
indicador_LOS = input("L'indicador LOS del terminal òptic està encès? (sí/no): ")
indicador_Internet = input("L'indicador d'Internet del router està encès? (sí/no): ")

if indicador_Internet == "no":
    print("Comprova el servei del proveïdor")
else:
    print("La connexió sembla funcionar correctament")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
percentatge_bateria = float(input("Introdueix el percentatge de bateria del SAI: "))

if percentatge_bateria < 0 or percentatge_bateria > 100:
    print("Valor fora del rang vàlid (0 % - 100 %)")
elif percentatge_bateria < 20:
    print("Nivell crític")
elif percentatge_bateria < 50:
    print("Nivell baix")
else:
    print("Nivell suficient")

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
latencia = float(input("Entra la latencia en ms: "))
perdua = float(input("Entra el percentatge de paquets perduts: "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Rebutjat")
else:
    if latencia <= 30 and perdua <= 1:
        print("Connexio excellent")
    elif latencia <= 80 and perdua <= 3:
        print("Connexio bona")
    elif latencia <= 150 and perdua <= 5:
        print("Connexio acceptable")
    else:
        print("Connexio deficient")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
tipus_pla = input("Entra el tipus de pla: ")
consum_mensual = float(input("Entra el consum mensual en GB: "))

if tipus_pla == "basic":
        cost_total = 10 + max(0, consum_mensual - 10) * 1.5
elif tipus_pla == "plus":
        cost_total = 20 + max(0, consum_mensual - 20) * 0.75
else:
        print("Tipus de pla desconegut")
        cost_total = None

if cost_total is not None:
        print(f"El cost total es: {cost_total} €")

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compte = input("El compte esta actiu (si/no)?: ")
contrasenya = input("La contrasenya es correcta (si/no)?: ")
codi_doble = input("El codi de doble verificacio es correcte (si/no)?: ")

if compte == "no":
    print("compte desactivat")
elif contrasenya == "no":
    print("contrasenya incorrecta")
elif codi_doble == "no":
    print("codi de doble verificacio incorrecte")
else:
    print("accés permès")

# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router = input("El router esta ences (si/no)?: ")
indicador_LOS = input("L'indicador LOS del terminal optic esta ences (si/no)?: ")
indicador_Internet = input("L'indicador d'Internet del router esta ences (si/no)?: ")

if router == "no":
     print("Cal encendre el router")
elif indicador_LOS == "si":
     print("Cal revisar el cable de fibra")
elif indicador_Internet == "no":
     print("Cal contactar amb el proveidor")
else:
     print("La connexio funciona correctament")

# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
servei_critic = input("La incidencia afecta un servei critic (si/no)?: ")
num_usuaris = int(input("Entra el numero d'usuaris afectats: "))
alternativa = input("Hi ha una alternativa de connexio disponible (si/no)?: ")

if num_usuaris < 0:
     print("Rebutjat")
elif (servei_critic == "si" and alternativa == "no") or (num_usuaris >= 50 and alternativa == "no"):
     print("Prioritat critica")
elif num_usuaris >= 10 or servei_critic == "si":
     print("Prioritat alta")
else:
     print("Prioritat baixa")  