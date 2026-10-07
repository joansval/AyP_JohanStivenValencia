# OBJETIVO: Permitir al usuario elegir un candidato (A, B o C) e imprimir el partido correspondiente 
# (rojo, verde o azul). Si ingresa otra cosa, mostrar "Opción errónea".

# 1. Pido la opción de voto al usuario. 
# No solo está el lower sino tambien el upper el cual es por si el usuario escribe 'a' minúscula, Python la pase a 'A' mayúscula de una vez.
voto = input("Elija un candidato para votar (A, B ó C): ").upper()

# 2. Empiezo a validar las opciones con la estructura if/elif/else que ya dominamos.
if voto == "A":
    print("Usted ha votado por el partido rojo")
    
elif voto == "B":
    print("Usted ha votado por el partido verde")
    
elif voto == "C":
    print("Usted ha votado por el partido azul")
    
else:
    # Si el usuario metió un número, una letra distinta (como la D) o cualquier otra cosa, cae aquí directo.
    print("Opción errónea")
# FIN