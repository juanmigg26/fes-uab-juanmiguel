# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona", "Madrid", "València", "Sevilla", "Bilbao")
print("Segona ciutat:", ciutats[1])
print("Penúltima ciutat:", ciutats[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1, 2, 3, 4, 3, 5, 3)
print("El número 3 apareix", numeros.count(3), "vegades.")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))

numeros = (5, 2, 8, 1, 9)
print("Tupla ordenada:", ordenar_tupla(numeros))
