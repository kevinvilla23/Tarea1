num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
if num1>num2:
    mensaje=num1,' es mayor y',num2,' es menor'
elif num1<num2:
    mensaje=num2,' es mayor y',num1,' es menor'
else:
    mensaje='Ambos numeros son iguales'
print(mensaje)