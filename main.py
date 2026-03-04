from datetime import datetime
# Diccionario de palabras y puntuaciones

emociones = {
"feliz": 1,
"genial": 2,
"bien": 1,
"excelente": 2,
"triste": -1,
"mal": -2,
"horrible": -2,
"fatal": -1
}
# Colores según emoción
colores = {
"Muy Positivo ": "lightgreen",
"Positivo ": "green",
"Neutro ": "gray",
"Negativo ": "orange",
"Muy Negativo ": "red"

}

print(emociones)
print(colores)
# Entrada de usuario
texto = input("Escribe una frase: ").lower()

# Reto: Completa el programa
# 1. Calcular la puntuación total de la frase
# 2. Determinar el resultado según puntuación
# 3. Guardar la frase y resultado en historial.txt (opcional)
# 4. Generar resultado.html con color dinámico
