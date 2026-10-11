# Archivo: taller_ejercicio3.py
# Taller de Ciclos - Ejercicio 3: Subcadenas ordenadas por longitud.

# le pido la palabra al usuario. Le pongo .strip() por si mete espacios en blanco sin querer.
palabra = input("Ingrese una palabra corta (ejemplo: 'rum'): ").strip()

# len() me dice cuantas letras tiene la palabra en total.
cantidad_letras = len(palabra)

print(f"\n Aquí están las subcadenas de '{palabra}':")

# CICLO EXTERNO: Controla el TAMAÑO de la subcadena
# Va desde 1 letra hasta el tamaño total de la palabra. (+1 porque Python para antes)
for longitud in range(1, cantidad_letras + 1):
    
    # CICLO INTERNO: Controla DESDE DONDE empiezo a cortar
    # Este limite matematico (cantidad_letras - longitud + 1) evita 
    # que intente cortar letras que ya no existen al final.
    for inicio in range(cantidad_letras - longitud + 1):
        
        # Calculo donde termina el corte
        fin = inicio + longitud
        
        # EL TRUCO ---> SLICING (Rebanado)
        # Nota: Investigando descubri que si pongo variable[inicio:fin],
        # Python me corta exactamente ese pedacito de texto sin tener que hacer
        # otro ciclo súper complejo para sacar letra por letra. Fue muy clave.
        subcadena = palabra[inicio:fin]
        
        # Imprimo el pedacito que acabo de cortar
        print(subcadena)

# FIN del ejercio 3
# Este ejercicio me puso a pensar bastante, pero me pareció
# supremamente interesante y me terminó gustando mucho cuando funcionó.