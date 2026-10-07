# OBJETIVO: Preguntar al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro si es viernes, otro si es sábado o domingo. Si no es ninguno de esos, imprimir otro mensaje.
# pido el dia pero le pondre el lower como nos explicaste en clase
# así nos evitamos problemas si el usuario escribe raro tipo "lUnEs"
dia = input("Por favor ingresa un día de la semana: ").lower()

# validamos cada caso conectando las opciones
if dia == "lunes":
    print("Qué Joaaa! otra semana mas de carga mental y estres, aaaah, esto apenas comienza pero vamos con toda la actitud")
    
elif dia == "viernes":
    # elif por si no fue el de arriba, revisa este
    print("¡Por fin es vierneeees!! Ahora puedes irte de rumba o relajarte totalmente por un buen rato, tómatelo como un premio, porque si no hay  paz mental,  no hay salud mental y terminarás arruinando tu vida :) ")
    
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    # agrupo el fin de semana con un 'or', cubriendo el sábado con y sin tilde por si las moscas
    print("FIN DE SEMANAA! Ahora si a descansar un poco de la semana y dejar los trabajos para última hora :D")
    
else:
     # si no fue ninguno de los anteriores cae acá directo (martes, miércoles, jueves o un teclazo mal dado)
     print("Día de semana común y corriente, a SEGUÍ ESTUDIANDO NO MÁS, dale con toda porque esto claro que  valdrá la pena! Por fa intenta nuevamente otro día de la semana o rectifica que no hayas escrito mal el dia.")
# FIN