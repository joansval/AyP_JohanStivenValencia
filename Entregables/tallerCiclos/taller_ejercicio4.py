# Diccionario inicial con las notas que nos da el problema
student_scores = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60
}

# Diccionario vacio donde voy a guardar las calificaciones finales en texto
student_grades = {}

# CICLO FOR PARA RECORRER EL DICCIONARIO
# Nota personal: Al hacer un 'for' en un diccionario, la variable 'estudiante' 
# toma automaticamente las LLAVES ("Harry", "Ron", etc) una por una en cada vuelta.
for estudiante in student_scores:
    
    # Extraigo la nota numerica de ese estudiante usando su llave
    nota = student_scores[estudiante]
    
    # Empiezo a evaluar la nota con los rangos que pide el pdf
    if nota >= 91 and nota <= 100:
        calificacion_texto = "Outstandng"
        
    elif nota >= 81 and nota <= 90:
        calificacion_texto = "Exceeds Expectations"
        
    elif nota >= 71 and nota <= 80:
        calificacion_texto = "Acceptable"
        
    else:
        # Si no fue ninguna de las anteriores, es 70 o menos y cae aqui.
        calificacion_texto = "Fail"
        
    # EL PASO FINAL: Agrego la calificacion en texto al nuevo diccionario.
    # Sintaxis logica: nuevo_diccionario[llave_existente] = nuevo_valor
    student_grades[estudiante] = calificacion_texto

# Imprimo el resultado para verificar que quedo bien armado el nuevo diccionario
print(f"El diccionario original era:\n{student_scores}\n")
print(f"El diccionario final de calificaciones es:\n{student_grades}")

# FIN
# usar diccionarios y sacar los valores usando la llave 
# como si fuera un identificador. Realmente no esta tan dificil como pensé
# creo que ya estoy interizando mas esto.