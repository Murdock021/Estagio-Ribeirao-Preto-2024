def inverte_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string


entrada = input("Digite uma string para inverter: ")
resultado = inverte_string(entrada)
print("String original:", entrada)
print("String invertida:", resultado)