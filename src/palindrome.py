def is_palindrome(palabra):
    palabra = palabra.replace(" ", "").lower().replace(".", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "")
