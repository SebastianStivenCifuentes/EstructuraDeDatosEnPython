# Solicita al usuario que introduzca una frase
frase = input("Por favor, introduzca una frase: ")

# Muestra la longitud de la frase
print("La longitud de la frase es:", len(frase))
print("-------------------------------------------------------")

# Solicita al usuario que introduzca una palabra para buscar en la frase
palabra = input("Por favor, introduzca una palabra para buscar en la frase: ")

# Comprueba si la palabra está en la frase
if palabra in frase:
    print("La palabra", palabra, "está en la frase.")
else:
    print("La palabra", palabra, "no está en la frase.")
print("-------------------------------------------------------")

# Solicita al usuario que introduzca una palabra para reemplazar en la frase
palabra_a_reemplazar = input("Por favor, introduzca la palabra que desea reemplazar en la frase: ")
nueva_palabra = input("Por favor, introduzca la nueva palabra: ")
print("-------------------------------------------------------")

# Reemplaza la palabra y muestra la nueva frase
nueva_frase = frase.replace(palabra_a_reemplazar, nueva_palabra)
print("La nueva frase es:", nueva_frase)
print("-------------------------------------------------------")