###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
for i in range(2, 21, 2):
    print (i)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
comptador = 0
for i in numeros:
    comptador += i
comptador /= 5
print(comptador)

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
maxim = numeros[0]
for i in numeros:
    if i > maxim:
        maxim = i
print (maxim)

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
cinc_lletres = [paraula for paraula in paraules if len(paraula) > 5]
print(cinc_lletres)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
lletra = input("Entra una lletra: ")
i = len([paraula for paraula in paraules if paraula[0] == lletra.lower()])
print(i)