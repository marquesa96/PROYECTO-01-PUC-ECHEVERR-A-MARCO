from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
This is the LifeStore_SalesList data:

lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_busqueda_por_categoria = [id_search, id product]
"""

###Enlistamos las categorias que tenemos en nuestra base de datos###
categoria_buscada = ['discos duros', 'procesadores',
                     'tarjetas de video', 'tarjetas madre',
                     'memoria USB', 'pantallas',
                     'bocinas', 'audifonos', ]

busqueda_por_categoria = []
for categoria in categoria_buscada:
    empty_list = []
    busqueda_por_categoria.append(empty_list)

for search in lifestore_searches:
    id_search = search[0]
    id_product = search[1]

    # contador de categorias
    contador_de_cat = 0
    searchs = []

    for product in lifestore_products:
        idproduct = product[0]
        nameproduct = product[1]
        cat = product[3]

        if id_product == idproduct:
            searchs.append(categoria)

for categoria in categoria_buscada:
    if categoria == cat:
        busqueda_por_categoria[contador_de_cat].append(product)
        continue
    contador_de_cat = contador_de_cat + 1


contador_de_cat = 0
print(busqueda_por_categoria)
# for s in busqueda_por_categoria:
#     print(s)

##Se crean nuevas listas vacías para cada categoría, en donde se almacenarán los productos que le correspondan##
# cat_processors = []
# catHDD = []
# cat_MB = []
# cat_GPU = []
# cat_USB = []
# cat_screen = []
# cat_speaks = []
# cat_headp = []

# for srch in busqueda_por_categoria:
#     cat_prod = srch[3]
#     if cat_prod == categoria_buscada[0]:
#         catHDD.append(srch)
#     elif cat_prod == categoria_buscada[1]:
#         cat_processors.append(srch)
#     elif cat_prod == categoria_buscada[2]:
#         cat_GPU.append(srch)
#     elif cat_prod == categoria_buscada[3]:
#         cat_MB.append(srch)
#     elif cat_prod == categoria_buscada[4]:
#         cat_USB.append(srch)
#     elif cat_prod == categoria_buscada[5]:
#         cat_screen.append(srch)
#     elif cat_prod == categoria_buscada[6]:
#         cat_speaks.append(srch)
#     elif cat_prod == categoria_buscada[7]:
#         cat_headp.append(srch)

# ###SE SUMAN LOS PRODUCTOS DE UNA MISMA CATEGORÍA PARA IDENTIFICAR CUAL HA SIDO EL QUE MENOS VENTAS TUVO###


#Se imprimen las listas por categoría y debajo de ellas los productos que se vendieron de esta###
for categorias in categoria_buscada:
    print(
        f'De la categoría {categoria_buscada[contador_de_cat]} se realizaron {(len(categorias))} búsquedas, los productos son: ')

    summary_sales = []
    for product in lifestore_products:
        # variable temporal, nos servirá para hacer match y saber cuantas veces se hace match.
        aux = 0
        for hd in categoria_buscada:
            # Se debe indicar el elemento de la lista, por eso debe de ir el 0.
            if product[3] == categoria_buscada[0]:
                aux += 1
        if aux != 0:
            summary_sales.append([product[1], aux])

    for summary in summary_sales:
        print(
            f'El producto {summary[0]}, se vendió {summary[1]} veces')


# for catHD in catHDD:
#     print(catHD[1][:25])
# print(
#     f'De la categoría {categoria_buscada[1]} se realizaron {(len(cat_processors))} búsquedas, los productos son: ')
# for catp in cat_processors:
#     print(catp)
# print(
#     f'De la categoría {categoria_buscada[2]} se realizaron {(len(cat_GPU))} búsquedas, los productos son: ')
# for catg in cat_GPU:
#     print(catg)
# print(
#     f'De la categoría {categoria_buscada[3]} se realizaron {(len(cat_MB))} búsquedas, los productos son: ')
# for mb in cat_MB:
#     print(mb)
# print(
#     f'De la categoría {categoria_buscada[4]} se realizaron {(len(cat_USB))} búsquedas, los productos son: ')
# for usb in cat_USB:
#     print(usb)
# print(
#     f'De la categoría {categoria_buscada[5]} se realizaron {(len(cat_screen))} búsquedas, los productos son: ')
# for screen in cat_screen:
#     print(screen)
# print(
#     f'De la categoría {categoria_buscada[6]} se realizaron {(len(cat_speaks))} búsquedas, los productos son: ')
# for spk in cat_speaks:
#     print(spk)
# print(
#     f'De la categoría {categoria_buscada[7]} se realizaron {(len(cat_headp))} búsquedas, los productos son: ')
# for hp in cat_headp:
#     print(hp)
