###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio = "Hola"):
    print(f"{salutacio}, {nom}")

saludar_a("Juan Miguel")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
   return numero % 2 == 0

print(es_parell(3))

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for i in numeros:
        suma += i
    return suma / len(numeros)

print(mitjana([1, 2, 3, 4, 5]))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(sumar_tot(1, 2, 3, 4, 5))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit = 10):
    for i in range(1, limit + 1):
        mult = numero * i
        print(f"{numero} x {i} = {mult}")

taula_multiplicar(5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom = "Juan", edat = "19", grau = "Primer")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(num):
    i = num
    while i > 1:
         i -= 1
         num *= i
    return num

def max(numeros):
    maxim = numeros[0]
    for i in numeros:
        if i > maxim:
            maxim = i
    return maxim

print(factorial(5))
print(max([1, 23, 45, 2, 100, 5]))