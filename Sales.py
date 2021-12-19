from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# Se limpia la lista para obtener ventas sin reembolso

ventas = []
for sale in lifestore_sales:

    refund = sale[4]
    if refund == 1:
        continue
    else:
        ventas.append(sale)


meses = [
    '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
    '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
]

ventas_por_mes = []
for mes in meses:
    lista_vacia = []
    ventas_por_mes.append(lista_vacia)


for venta in ventas:
    id_venta = venta[0]
    fecha = venta[3]

    contador_de_mes = 0

    for mes in meses:
        if mes in fecha:
            ventas_por_mes[contador_de_mes].append(id_venta)
            continue
        contador_de_mes = contador_de_mes + 1


contador_de_mes = 0

for vxmes in ventas_por_mes:
    #print(f'En el mes de {meses[contador_de_mes]} hubo {len(vxmes)} ventas!')
    contador_de_mes = contador_de_mes + 1

# Calcularemos cuanto se vendio cada mes.

gmensual = []
for vxmes in ventas_por_mes:
    ganancia_del_mes = 0
    for id_venta in vxmes:
        indice_de_venta = id_venta - 1

        info_de_venta = lifestore_sales[indice_de_venta]

        id_prod = info_de_venta[1]
        indice_de_prod = id_prod - 1
        info_del_prod = lifestore_products[indice_de_prod]
        precio_de_prod = info_del_prod[2]
        ganancia_del_mes = ganancia_del_mes + precio_de_prod
    gmensual.append(ganancia_del_mes)

ganancia_mes = []
for mes, ganancia in enumerate(gmensual):
    sublista = [ganancia, mes]
    ganancia_mes.append(sublista)

print(ganancia_mes)
