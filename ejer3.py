# Parte 1

class Venta:
    
    contador = 0
    total_acumulado = 0
    historial = []
    
    def __init__(self, persona, precio):
        self.persona = persona
        self.precio = precio
        
        Venta.contador += 1
        Venta.total_acumulado += precio
        Venta.historial.append(self)


v1 = Venta("Carlos", 150)
v2 = Venta("Lucia", 200)
v3 = Venta("Andrea", 75)
v4 = Venta("Miguel", 320)


print("Se registraron", Venta.contador, "ventas en total.")
print("El dinero ingresado suma:", Venta.total_acumulado)

print("\nListado completo:")
for elemento in Venta.historial:
    print(elemento.persona, "pagó", elemento.precio)



# Parte 2

class Persona:
    
    numero_personas = 0
    
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion
    
    def mejorar(self):
        self.puntuacion += 1
    
    def situacion(self):
        if self.puntuacion >= 5:
            return "Aprobado"
        else:
            return "Suspenso"
    
    @classmethod
    def sumar_persona(cls):
        cls.numero_personas += 1
    
    @staticmethod
    def comprobar(valor):
        return 0 <= valor <= 10


p1 = Persona("Raul", 1)
p2 = Persona("Elena", 4)
p3 = Persona("Sergio", 9)

p2.mejorar()

print(p1.situacion())
print(p2.situacion())

Persona.sumar_persona()
print("Personas contadas:", Persona.numero_personas)

print(comprobar := Persona.comprobar(8))
print(Persona.comprobar(-1))