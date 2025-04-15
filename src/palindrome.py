def is_palindrome(palabra):
    palabra = palabra.replace(" ", "").lower().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")
    for index in range(len(palabra)):
        if palabra[index] != palabra[-(index + 1)]:
            return False
    return True

palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
resultado = is_palindrome(palabra)
print(f"¿La palabra '{palabra}' es un palíndromo? {'Sí' if resultado else 'No'}")
