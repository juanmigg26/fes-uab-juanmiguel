###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador = 10
while comptador > 0:
    print(comptador)
    comptador -= 1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador_2 = 0
suma = 0
while comptador_2 <= 20:
    suma += comptador_2
    comptador_2 += 2
print("La suma es igual a:", suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
enter = int(input("Entra un enter positiu: "))
contador = enter
while contador > 1:
    contador -= 1
    enter *= contador
print(enter)

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = input("Introdueix una contrasenya: ")
while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya valida: ")
print("Contrasenya valida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
comptador_3 = 1
num = int(input("Entra un enter positiu: "))
while comptador_3 <= 10:
    mult = num
    mult *= comptador_3
    print(f"{num} x {comptador_3} = {mult}")
    comptador_3 += 1
    
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
N = int(input("Introdueix un número enter positiu N: "))
numero = 2

while numero <= N:
    divisor = 2
    es_primer = True

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primer = False
            break
        divisor += 1

    if es_primer:
        print(numero)

    numero += 1