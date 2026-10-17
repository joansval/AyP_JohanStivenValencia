# creamos el diccionario con 5 opciones de comida y precios razonables en pesos
menu = {
    "hamburguesa": 15000,
    "perro caliente": 10000,
    "salchipapa": 12000,
    "pollo frito": 14000,
    "malteada": 8000
}

# lista vacia para guardar todos los platos que el cliente vaya pidiendo
orden = []

# variable para ir sumando la plata de la cuenta
total = 0

# variable para controlar el ciclo while, arranca en "si"
continuar = "si"

print("=== BIENVENIDO A COMIDAS RAPIDAS 'EL INFARTO' ===")
print("donde el sabor supera a la gastritis. este es nuestro menu de hoy:")

# usamos un ciclo for para mostrar cada plato del diccionario y su precio al entrar
for plato in menu:
    print("-", plato, ": $", menu[plato])

# ciclo principal para que el cliente haga multiples pedidos
while continuar == "si":
    # pedimos el plato al cliente
    # usamos .lower() para pasar a minusculas todo y evitar errores por mayusculas
    pedido = input("\nque veneno va a pedir hoy?: ").lower()
    
    # variable vacia para guardar el plato si logramos adivinar cual quiere
    plato_encontrado = ""
    
    # evitamos el error de que el cliente de enter sin escribir nada
    # usamos len() que cuenta las letras, para obligarlo a que escriba al menos 3 letras
    if len(pedido) >= 3:
        # recorremos el menu a ver si lo que escribio coincide con una parte de nuestro plato
        for opcion in menu:
            # si lo que escribio (ej: "hambur") hace parte del nombre ("hamburguesa")
            if pedido in opcion:
                plato_encontrado = opcion
    
    # el rombo principal del diagrama: verificamos si logramos encontrar el plato
    if plato_encontrado != "":
        # usamos .append() para meter el plato real al final de nuestra lista orden
        orden.append(plato_encontrado)
        
        # sumamos el precio buscando el plato en el diccionario
        total = total + menu[plato_encontrado]
        
        print("listo, marchando un(a)", plato_encontrado, "para tapar una arteria. precio: $", menu[plato_encontrado])
        
        # preguntamos si quieren mas
        continuar = input("desea engordar un poquito más? (si/no): ").lower()
        
    else:
        # aca entra si pide algo que no existe (como el sobrino) o lo escribe muy corto
        print("\nay mijo, o usted escribe horrible con mala ortografia, o es que jura que estamos en paris.")
        print("esto es un chuzo de barrio! aqui no tenemos o no entendimos '", pedido, "'.")
        print("lea bien las opciones. se las repito para que pida algo que si tengamos:")
        
        # VOLVEMOS A MOSTRAR EL MENU ACA ADENTRO DEL ELSE USANDO EL MISMO FOR
        for plato in menu:
            print("-", plato, ": $", menu[plato])

# cuando digan que "no" quieren mas, se rompe el ciclo while y mostramos la salida final
print("\n=== FACTURA PARA LLORAR ===")
print("se van a empacar todo esto:", orden)
print("el daño a su sistema digestivo les salio por un total de: $", total)
print("gracias por su dinero, vuelva pronto y comprese aqui al frente un sal de frutas :D!")