###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tecnic = input("Introdueix el nom d'un tecnic: ")
nom_xarxa = input("Introdueix el nom de la xarxa que esta instalant: ")
print(f"Nom del tecnic: {nom_tecnic}; Nom de la xarxa: {nom_xarxa}\n")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
long_enllac = float(input("Entra la longitud d'un enllac de fibra: "))
vel_transmissio = float(input("Entra la velocitat de transmissio: "))
print(f"El temps necessari per transmetre 1 GB de dades és de {8 * long_enllac / vel_transmissio} segons\n")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = int(input ("Introdueix el nombre d'hores de feina: "))
preu_hora = float(input("Entra el preu per hora d'una instalacio de xarxa: "))
preu_material = float(input("Posa el preu del material: "))
print(f"El cost total de la instalacio es: {preu_hora * hores_feina + preu_material}")