print("Python")
print("Calculadora")



Menu = """
    Bienvenido a la calculadora 🧮 
    1 - Suma
    2 - Resta
    3 - Multiplicacion
    4 - Division
    
    Elige una opcion: """

opcion = int(input(Menu))

if opcion == 1:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        resultado = num1 + num2
        print('El resultado es:', resultado)
elif opcion == 2:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        resultado = num1 - num2
        print('El resultado es:', resultado)

elif opcion == 3:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        resultado = num1 * num2
        print('El resultado es:', resultado)

elif opcion == 4:
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero:'))
        resultado = num1 / num2
        print('El resultado es:', resultado)
else:
         input('Escribe una opcion correcta: ' + Menu)


        




                
              

    



