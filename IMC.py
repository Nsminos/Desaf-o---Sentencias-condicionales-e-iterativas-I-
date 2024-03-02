import math
#W : corresponde al peso de la persona en Kg.
#H: corresponde a la altura en metros.
#IMC: EL valor del IMC (indice de masa corporal) en [Kg/m2]

W = "corresponde al peso de la persona en Kg"
H = "corresponde a la altura en metros"
IMC = "EL valor del IMC, en [Kg/m2]"

# Solicitud Inputs
W = float(input("Ingrese el peso de la persona en Kg:\n>"))
H = float(input("Ingrese la altura en metros en metros:\n>"))

# Formula de IMC
IMC = W / H**2

print(f"El indice de masa corporal es de: {math.ceil(IMC)}")

IMC = 
if IMC < 18.5
    print("Bajo Peso")
elif IMC >=18.5 and IMC < 25
    print("Adecuado")
elif IMC >= 25 and IMC < 30
    print("Sobrepeso")
elif IMC >= 30 and IMC < 35
    print("Obesidad Grado I")
elif IMC >= 35 and IMC < 40
    print("Obesidad Grado II")
else IMC >= 40
    print("Obesidad Grado III")

