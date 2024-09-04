def inverter_string(s):
    inverso = ''
    for char in s:
        inverso = char + inverso
    return inverso
string = input("Informe uma palavra: ")
print(f"palavra invertida: {inverter_string(string)}")