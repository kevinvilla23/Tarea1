num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3
if suma % 7 == 0:
    print("La suma es " +str(suma)+ " y es múltiplo de 7.")
else:
    print("La suma no es múltiplo de 7.")