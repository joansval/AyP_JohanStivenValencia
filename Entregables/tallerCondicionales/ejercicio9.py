# NOTA: Como le comenté en Classroom, este ejercicio final me costó muchisimo la parte lófica
# pero aquí dejo documentado cómo fui entendiendo el despiece de los datos paso a paso.
# OBJETIVO: Sistema para el instituto de inglés. Pide fecha y evalua cosas distintas 
# dependiendo de si es lunes, martes, miercoles, jueves o viernes.

# 1. Pido la entrada y le meto el .lower() de una para no complicarnos con las mayúsculas.
entrada = input("Ingrese la fecha (ejemplo: lunes, 15/04): ").lower()

# 2. SEPARAR LOS DATOS (Acá vienen cosas nuevas e interesantes!)
# Voy a usar la función .split(), entendí que, literal funciona como unas "tijeras".
# Adentro de los paréntesis le digo por qué símbolo quiero que corte el texto.
# Si pongo split(","), me parte el texto en dos donde encuentre la coma.
partes = entrada.split(",") 

# partes[0] me guarda la primera mitad (el dia). .strip() borra si quedaron espacios vacios por ahi.
dia_semana = partes[0].strip() 
fecha_numeros = partes[1].strip() # partes[1] guarda la segunda mitad (los numeros "15/04")

# Ahora uso la misma tijera pero con la barra '/' para separar el numero del dia y el numero del mes
numeros = fecha_numeros.split("/")
dia = int(numeros[0]) # convierto a int para poder usar operadores matamáticos despues
mes = int(numeros[1])

# 3. FILTRO DE ERRORES (como lo pide el taller)
# Creo una lista con los dias permitidos (agrego miercoles sin tilde porsiacaso)
dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]

# Evaluo si metieron algun dato como no valido (>31 o >12, menores a 1, o un dia raro)
if dia_semana not in dias_validos or dia < 1 or dia > 31 or mes < 1 or mes > 12:
    print("Se produjo un error")

else:
    # 4. SI PASÓ LA VALIDACIÓN, ARRANCAMOS CON LA LOGICA DE LOS DIAS
    
    # LUNES, MARTES O MIERCOLES (Inicial, intermedio y avanzado piden exactamente lo mismo)
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miércoles" or dia_semana == "miercoles":
        
        # Agregué este pequeño bloque visual para que el programa confirme en qué nivel entró
        if dia_semana == "lunes":
            print("--> Nivel Inicial")
        elif dia_semana == "martes":
            print("--> Nivel Intermedio")
        else:
            print("--> Nivel Avanzado")

        # El taller pide preguntar si hubo examenes
        hubo_examen = input("¿Se tomaron exámenes hoy? (si/no): ").lower()
        
        if hubo_examen == "si" or hubo_examen == "sí":
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            reprobados = int(input("Ingrese la cantidad de alumnos que no aprobaron: "))
            
            # Proceso matematico basico para sacar el pocentaje
            total_alumnos = aprobados + reprobados
            if total_alumnos > 0: # esto lo pongo para que no me de error dividiendo por cero 
                porcentaje = (aprobados * 100) / total_alumnos
                print(f"El porcentaje de aprobados es: {porcentaje}%")
        else:
            # Si escriben que "no", simplemente sale este mensaje y el diagrama queda fácil de dibujar
            print("Entendido, hoy fue una clase normal sin exámenes.")
    
    # JUEVES (Práctica hablada)
    elif dia_semana == "jueves":
        print("--> Clase de Práctica Hablada")
        # uso 'int' normalito para el porcentaje
        asistencia = int(input("Ingrese el porcentaje de asistencia a clase (ej: 55): "))
        
        if asistencia > 50:
            print("asistió la mayoría")
        else:
            print("no asistió la mayoría")
            
    # VIERNES (Inglés para viajeros)
    elif dia_semana == "viernes":
        print("--> Clase de Inglés para Viajeros")
        # Si el dia fue 1 del mes 1, o el dia 1 del mes 7...
        if (dia == 1 and mes == 1) or (dia == 1 and mes == 7):
            print("Comienzo de nuevo ciclo")
            cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            
            # Para la plata uso 'float' que es un primo de 'int' pero permite guardar numeros con decimales 
            arancel = float(input("Ingrese el arancel (precio) en $ por cada alumno: "))
            
            ingreso_total = cant_alumnos * arancel
            print(f"El ingreso total en $ es: {ingreso_total}")
        else:
            print("Hoy es una clase de ciclo regular.")
            
# FIN!!!