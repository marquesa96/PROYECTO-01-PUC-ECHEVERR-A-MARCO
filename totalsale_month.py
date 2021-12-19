from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

###SE LIMPIA LA LISTA###
ventas = []

for sale in lifestore_sales:
    refund = sale[4]

    if refund == 1:
        continue

    else:
        ventas.append(sale)

# Aquí ventas ya no incluye reembolsos

meses = [
    '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
    '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
]

ventas_por_mes = []
#####Aquí hacemos un for en donde se agregarán las listas de los meses ######
# Dice que por cada mes dentro de meses, cree una lista vacía
for mes in meses:
    # Es la lista que estará dentro de la lista que regresa los IDs de las ventas
    lista_vacia = []
    ventas_por_mes.append(lista_vacia)

# print (ventas_por_mes) si imprimimos aqui saldran vacíos

for venta in ventas:
    id_venta = venta[0]
    id_prod = venta[1]
    fecha = venta[3]

    # Clasificar en mes
    # Comienzo en el mes 0 ('/01/')
    contador_de_mes = 0
    names = []
    ids = []
    sales = 0

    for product in lifestore_products:
        idproduct = product[0]
        nameproduct = product[1]
        price = product[2]

        # if id_prod == idproduct:  # Se comparan los ids en las listas y si son iguales se agregan a una nueva lista los nombres
        #     names.append(nameproduct)

        if id_prod == idproduct:  # Nos puede servir para calcular cuantos de cada producto se vendieron en el mes sin tener que desplegar todos
            ids.append(venta)
    for mes in meses:
        if mes in fecha:
            # aqui se cambia la variable segun requiramos en la lista
            # No se porque el append sale en blanco
            ventas_por_mes[contador_de_mes].append(ids)
            continue
        contador_de_mes = contador_de_mes + 1


contador_de_mes = 0

# Se imprime cuantos productos se vendieron por cada mes y cuales fueron:
for venta_mensual in ventas_por_mes:

    print('////////////////////////////////////////////////////////////////////////////////////////')
    print(
        f'En el mes de {meses[contador_de_mes]} hubieron {len(venta_mensual)} ventas:')
    summary_sales = []
    for product in lifestore_products:
        # variable temporal, nos servirá para hacer match y saber cuantas veces se hace match.
        aux = 0
        for ven in venta_mensual:
            # Se debe indicar el elemento de la lista, por eso debe de ir el 0.
            if product[0] == ven[0][1]:
                aux += 1
        if aux != 0:
            summary_sales.append([product[1:3], aux])

    for summary in summary_sales:
        print(
            f'El producto {summary[0]}, se vendió {summary[1]} veces')

    # debe de ir abajo para que vaya incrementando el numero del mes

    contador_de_mes = contador_de_mes + 1
#  precio = precio + product[2]
#     print(f'Con un total de: ${precio}')
# Se intento sacar el precio de cada mes con lo que se tiene en este archivo pero no se logró
# Se tuvo que hacer manual
