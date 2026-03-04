#Ej1
numbre = input("Ingresa tu nombre")
edad = int( input("Ingresa tu nombre"))

print(f"En 10 anos tendras, {edad+10}")

#Ej2 

num1 = int(input("Ingresa el primer numero")) 

num2 = int(input("Ingresa el segundo numero")) 

if num1 & num2 != 0:  

    suma = num1 + num2 

    print("La suma d elos numeros es",suma) 

    resta = num1 - num2 

    print("La resta de los numeros es",resta) 

    multiplicacion = num1 * num2 

    print("La multiplicacion de los numeros es",multiplicacion) 

    division = num1 / num2 

    print("La division de los numeros es",division) 

elif num1 == 0: 

    print("No se permiten 0") 

    num1 = int(input("Ingresa el primer numero")) 

    if(num1 != 0): 

        suma = num1 + num2 

        print("La suma d elos numeros es",suma) 

        resta = num1 - num2 

        print("La resta de los numeros es",resta) 

        multiplicacion = num1 * num2 

        print("La multiplicacion de los numeros es",multiplicacion) 

        division = num1 / num2 

        print("La division de los numeros es",division) 

  

elif num2 == 0: 

    print("No se permiten 0") 

    num2 = int(input("Ingresa el segundo numero")) 

    if(num2 != 0): 

        suma = num1 + num2 

        print("La suma d elos numeros es",suma) 

        resta = num1 - num2 

        print("La resta de los numeros es",resta) 

        multiplicacion = num1 * num2 

        print("La multiplicacion de los numeros es",multiplicacion) 

        division = num1 / num2 

        print("La division de los numeros es",division) 

 

 

#Ej3 

numero = int(input("Ingresa un numero")) 

if numero % 2 == 0: 

    print("Es par") 

else: 

    print("Es impar") 

              

#Ej4 

for i in range(1, 51): 

    if i % 3 == 0: 

        print(i) 

#Ej5  

numeros = [] 

for i in range(5): 

    num = float(input(f"Introduce el número {i+1}: ")) 

    numeros.append(num) 

print("Lista:", numeros) 

mayor = max(numeros) 

menor = min(numeros) 

media = sum(numeros) / len(numeros) 

print("El mayor es:", mayor) 

print("El menor es:", menor) 

print("La media es:", media) 

 

#Ej6 

alumnos = { 

    "nombre": "Marcos", 

    "edad": "20", 

    "ciclo":"DAW" 

} 

for alumno in alumnos.items(): 

    print(alumno) 

 

#Ej7  

num = int(input("Ingresa un numero: ")) 

  

def es_primo(numero): 

    if numero <= 1: 

        return False 

    for i in range(2, numero): 

        if numero % i == 0: 

            return False 

    return True 

  

if es_primo(num): 

    print("Es primo") 

else: 

    print("No es primo") 

 

#Ej8 

texto = input("Escribe una frase:") 

  

texto = texto.lower() 

print(texto) 

contador = 0 

for palabra in texto: 

    if palabra == "a" or palabra == "e" or palabra == "i" or palabra == "o" or palabra == "u": 

        contador+=1 

print(f"La cadena contiene, {contador} , vocales" ) 

 # Ej 9
password = input("Ingresa una password")

while password != "admin123":
    password = input("Ingresa una password")
print(password)
    
#Ej 10
cuadrados = []

# Rellenarla usando un bucle for
for x in range(1, 11):
    cuadrados.append(x**2)

# Mostrar la lista
print(cuadrados)