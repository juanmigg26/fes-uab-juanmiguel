###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Encaminador 1"
ubicacio = "Ni idea"
nombre_ports = 31
esta_ences = "si"

print(f"El {nom_encaminador} esta ubicat a {ubicacio} i te {nombre_ports} ports. Esta ences: {esta_ences}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_inclosos = 10
GB_consumits = 7
print(f"Queden {GB_inclosos - GB_consumits} GBs")
GB_consumits = 9
print(f"Queden {GB_inclosos - GB_consumits} GBs")