temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

def celsius_para_fahrenheit(c): return (c * 9/5) + 32
def celsius_para_kelvin(c): return c + 273.15
def fahrenheit_para_celsius(f): return (f - 32) * 5/9
def kelvin_para_celsius(k): return k - 273.15

if origem == "F":
    temp_c = fahrenheit_para_celsius(temp)
elif origem == "K":
    temp_c = kelvin_para_celsius(temp)
else:
    temp_c = temp

if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = celsius_para_fahrenheit(temp_c)
elif destino == "K":
    resultado = celsius_para_kelvin(temp_c)

print(f"Temperatura convertida: {resultado:.2f} {destino}")