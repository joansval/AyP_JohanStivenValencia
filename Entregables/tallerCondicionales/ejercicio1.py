# OBJETIVO: Solicitar al usuario un número que este entre 10 y 50. Si el número es el 30, imprimir “Ganaste un premio” en el caso contrario “Perdiste”. ¿Qué pasaría si el usuario ingresa -10? 
# Bueno, profe, quiero darle como un toque de sesgo hacia típicas estafas en internet jajaja pero en esencia me aseguraré de cumplir el objetivo del ejercicio totalmente hechos a conciencia porque esa es la gracia: aprender!!
#1. solicito entrada de datos 
numero = int(input("Por favor ingresa un número estrictamente entre 10 y 50: "))
#aquí validaría, en primer lugar si está dentro del rango
if 10 <= numero <= 50:
    #validararía si es el número ganador
    if numero == 30:
        print("GANASTE UN PREMIO!! Reclámelo en la siguiente web, se te pedirán los datos de tu tarjeta para verificar tu identidad")
    else: 
        print("PERDISTE, aun asi ingresa los datos de tu tarjeta para tener mas probabilidades de ganar la próxima vez")
else:
     #y si la salida no cumple con el rango (como ingresar ejemplo -10)
     print("Número en el rango no permitido!")
#FIN