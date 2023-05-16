# Pedimos al usuario que ingrese del tamaño del diccionario
tamaño = int(input("Ingrese el tamaño del  tamaño del diccionario: "))

# Solicitamos al usuario que introduzca una serie de pares clave-valor para llenar el diccionario
mi_diccionario = {}

for i in range(tamaño):
    print("-------------------------------------------------------")
    clave = input("Por favor, introduzca la clave para el elemento " + str(i + 1) + ": ")
    valor = input("Por favor, introduzca el valor para el elemento " + str(i + 1) + ": ")
    mi_diccionario[clave] = valor
print("-------------------------------------------------------")

# Imprime el diccionario completo
print("Diccionario completo:", mi_diccionario)
print("-------------------------------------------------------")
# Solicita al usuario una clave y muestra el valor correspondiente
clave_a_buscar = input("Por favor, introduzca una clave para buscar su valor correspondiente: ")
if clave_a_buscar in mi_diccionario:
    print("El valor para la clave", clave_a_buscar, "es:", mi_diccionario[clave_a_buscar])
else:
    print("La clave", clave_a_buscar, "no existe en el diccionario")
print("-------------------------------------------------------")

# Solicita al usuario una clave para eliminar del diccionario
clave_a_eliminar = input("Por favor, introduzca una clave para eliminar del diccionario: ")
if clave_a_eliminar in mi_diccionario:
    del mi_diccionario[clave_a_eliminar]
    print("La clave", clave_a_eliminar, "ha sido eliminada. Diccionario actualizado:", mi_diccionario)
else:
    print("La clave", clave_a_eliminar, "no existe en el diccionario")
    print("-------------------------------------------------------")

# Imprime el diccionario completo
print("Diccionario completo:", mi_diccionario)
print("-------------------------------------------------------")