def fizzbuzz(numero):
    """
    Devuelve 'fizz' si el número es divisible por 3, 'buzz' si es divisible por 5,
    'fizzbuzz' si es divisible por ambos, o el número mismo en otro caso.
    """
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 3 == 0:
        return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
        return numero

# Ejemplo de uso:
# for i in range(1, 16):
#     print(fizzbuzz(i)) 