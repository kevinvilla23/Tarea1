num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

promedio=int((num1+num2+num3)/3)
if promedio % 2 == 0:
    print("el promedio es ", promedio," y es par")
else:
    print("El promedio es ", promedio," y es inpar")
