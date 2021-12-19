from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
This is the LifeStore_SalesList data:

lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_searches = [id_search, id product]
"""

high_search = []

num_searchs = len(lifestore_searches)

# Para agregar a una lista nueva, listas que contengan el ID de la búsqueda sin el monto de esa búsqueda
for id in range(num_searchs):  # El rango es de (0,1033)
    new_id_prod = id + 1  # Se suma 1 porque las listas empiezan en 0.
    # En una fila de la lista, agregas el ID y su cantidad hasta aquí es 0. No se le ha sumado nada.
    row = [new_id_prod, 0]
    # Se irá agregando a la lista vacía, cada fila con el ID del producto y su cantidad
    high_search.append(row)

for search in lifestore_searches:
    # En cada fila de ventas, el valor del segundo elemento es el ID del producto
    id_product = search[1]
    high_search[id_product - 1][1] = high_search[id_product - 1][1] + 1

###LIMPIEMOS LA LISTA PARA OBTENER SOLO LOS PRODUCTOS QUE OBTUVIERON BUSQUEDAS###
searchs = []
for hs in high_search:
    empty = hs[1]  # La posición que indica que está o no sin búsqueda
    if empty == 0:
        continue
    else:
        searchs.append(hs)

#print (searchs)
ordenamiento = sorted(searchs, key=lambda x: x[1], reverse=True)

# print(ordenamiento)

print(f'Los 10 productos más búscados son:')
for p in range(10):
    k = ordenamiento[p][0]
    indice = k - 1
    print(f' {lifestore_products[indice]} con {ordenamiento[p][1]} búsquedas')
