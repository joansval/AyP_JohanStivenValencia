# Taller de Ciclos - Ejercicio 5: El paseo del borracho

# NOTA PERSONAL: Como el problema dice que el sujeto elige su camino "al azar",
# investigué y descubrí que Python tiene una herramienta integrada para eso.
# Se llama random y toca importarla al principio del codigo para usarla
import random

# El problema dice que arranca en el origen (0, 0) del plano, asi que 
# inicio las variables 'x' y 'y' en cero porque seria como el marco de referencia
x = 0
y = 0

print("🍺 Inicia la caminata. El sujeto sale del bar en la posición (0, 0)...")
print("Por si te preguntas, sí... su mujer lo hizo emborrachar, pero esta vez mucho!")
print("Está empezando a tambalearse, parece un bailarín de folclor...\n")

# Como sabemos que son exactamente 100 intersecciones (pasos), uso un ciclo FOR.
# range(100) hace que el ciclo dé exactamente 100 vueltas, de la 0 a la 99.
for paso in range(100):
    
    # "la clave": random.choice()
    # Esta función escoge una opción aleatoria de la lista que le pongo adentro.
    # Es la forma de simular que toma una decisión sin que yo tenga que escribirla.
    direccion = random.choice(["norte", "sur", "este", "oeste"])
    
    # Empiezo a evaluar para dónde agarró el borracho en este paso.
    # Modificamos las coordenadas simulando un plano cartesiano (X, Y).
    if direccion == "norte":
        y = y + 1  # Eje Y positivo
        
    elif direccion == "sur":
        y = y - 1  # Eje Y negativo
        
    elif direccion == "este":
        x = x + 1  # Eje X positivo
        
    else:
        # Si no fue norte, sur o este, obligatoriamente agarró pal oeste
        x = x - 1  # Eje X negativo

# ESTA PARTE YA ESTA FUERA DEL CICLO
# Imprimo dónde terminó el recorrido después de completar el ciclo de 100 vueltas.
print("... 100 'cuadras' de pura confusión después ...")
print(f"📍 RESCATE: El borracho terminó tirado en la coordenada: ({x}, {y})")

# Calculando la distancia final usando lógica condicional básica.
# Uso valores absolutos manuales (multiplicando por -1 si el número es negativo) 
# para ver cuántas cuadras caminó en total alejándose del bar (0,0).
distancia_x = x if x > 0 else x * -1
distancia_y = y if y > 0 else y * -1
cuadras_totales = distancia_x + distancia_y

print(f"Al final de la noche, quedó a {cuadras_totales} cuadras o pasos de distancia del bar (ni el borracho sabía). ¡Llamen a un taxi o a una ambulancia!\n")

# FIN
# Me pareció muy, muy útil esto de usar la librería random. Al principio no entendía cómo hacer que el 
# programa tomara una decisión por sí solo sin preguntarme con un input, pero con 
# esta función se pueden simular sistemas muy interesantes! y veremos en próximos códigos...
# simplemente, me encantó!