#1
numero = int(input("ingrese un numero:"))

if numero > 0 :
    print("El numero",numero, "es positivo")
elif numero < 0:
    print("El numero",numero, " es negativo")
else:
    print("El numero es 0")
if numero %2 == 0:
    print("El numero",numero, "es par")
else:
    print("El numero",numero, "es impar")

#2
operacion = input("Introduce una operacion (+, -, *, /): ")
num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce otro numero para realizar la operacion:"))
match operacion:
    case "+": result = num1 + num2
    case "-":  result =num1 - num2
    case "*" : result =num1 * num2
    case "/" if num2 != 0 :  result =num1 / num2
    case "/" :  result ="Cannot divide by zero!"
    case _ :  result ="Invalid operator!"
print(result)

#3
ano = int(input("Introduce un numero:"))

if ano % 4 == 0:
    print("El año",ano,"es bisiesto")
else:
    print("El año",ano,"no es bisiesto")

#4
nota = int(input("Ingresa una nota:"))

if nota < 5 :
    print("Suspendido")
elif nota>=5 and nota < 7:
    print("Aprobado")
elif nota >=7 and nota < 9:
    print("Notable")
elif nota >=9 and nota <= 10:
    print("Sobresaliente")

#5

n = int(input("Introduce un numero:"))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los números del 1 al", n, "es:", suma)
#6
for i in range(10, 0, -1):
    print(i)

#7
frase = input("Ingresa una frase:")
contador = 0
for cadena in frase:
    if cadena == "a" or cadena == "e" or cadena == "i" or cadena == "o" or cadena == "u":
        contador+=1
print("Hay",contador, " vocales en la frase") 

#8
for i in range(1,50):
    if i % 3 == 0:
        print(i)

#9
password = input("Ingrese una contraseña:")
contador = 0
while password != "admin123":
    password = input("Ingrese una contraseña:")

    contador+=1
print("Se ha equivocado",contador,"veces")
#10
while num1 !=0 or num2 !=0:
    num1 = int(input("Ingresa un numero:"))
    num2 = int(input("Ingresa un numero:"))
    suma = num1+num2
    print("Los numeros suman:",suma)

#11
from random import *
numero_random = randint(1,20)
print(numero_random)
numero_usuario = int(input("Ingresa un numero para intentar adivinar el numero del 1 al 10:"))
if numero_usuario != numero_random and numero_usuario < numero_random :
    print("No lo adivinaste, el numero es mayor")
elif numero_usuario != numero_random and numero_usuario > numero_random :
    print("No lo adivinaste, el numero es menor")
else:
    print("Has adivinado el numero")

#12
#Pide 8 números y:Guarda en lista

numeros = []
for i in range(8):
    num = int(input("Introduce un número:"))
    numeros.append(num)
mayor = max(numeros) 

menor = min(numeros) 

media = sum(numeros) / len(numeros) 

print("El mayor es:", mayor) 

print("El menor es:", menor) 

print("La media es:", media) 

#13
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print() 
#14
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]
resultado = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += A[i][k] * B[k][j]

for fila in resultado:
    print(fila)
#15
contactos = []

for i in range(3):
    nombre=input("Ingresa un nombre:")
    telefono= int(input("Ingresa un numero de telefono:"))
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    
    contactos.append(contacto)
print(contactos)
#16
alumnos = {
    "Marcos": 8,
    "Ana": 9,
    "Luis": 7,
    "Sofia": 10,
    "Carlos": 6
}
print(alumnos)
notas = alumnos.values()
media = sum(notas) / len(notas)
mejor = max(alumnos, key=alumnos.get)

peor = min(alumnos, key=alumnos.get)
print("La media de la clase:",media)
print("Mejor alumno:", mejor, "con un", alumnos[mejor])
print("Peor alumno:", peor, "con un", alumnos[peor])

#17

esp = {'Uno': 1, 'Dos': 2}
eng = {'One': 1, 'Two': 2}
for espanol, english in zip(esp, eng):
    print(espanol,"→", english)

#18
lista = [10, 20, 30, 40, 50]

iterador = iter(lista)

while True:
    try:
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        print("saleindo")
        break

#19
lista = ["manzana", "pera", "uva", "naranja"]

for indice, valor in enumerate(lista):
    print(indice, valor)

#20
def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        productos.append({"nombre": nombre, "precio": precio})
    except ValueError:
        print("Precio inválido")

def mostrar_productos(productos):
    if not productos:
        print("No hay productos")
    else:
        for i, producto in enumerate(productos):
            print(i + 1, producto["nombre"], "-", producto["precio"])

def calcular_total(productos):
    total = sum(producto["precio"] for producto in productos)
    print("Total:", total)

def main():
    productos = []
    while True:
        print("\n1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Calcular total")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            calcular_total(productos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

main()