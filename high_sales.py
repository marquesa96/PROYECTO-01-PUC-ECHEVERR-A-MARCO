from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
lifestore_searches = [id_search, id_product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
# Primero lo que haremos será quitar aquellas ventas que se devolvieron y las que quedan se introducen en una lista y serán las ventas que usaremos.
ventas = []
for sale in lifestore_sales:
    refund = sale[4]  # La posición que indica que está o no en devolución
    if refund == 1:
        continue
    else:
        ventas.append(sale)

# print(ventas), aquí podemos ver la lista ya limpia

# Será la nueva lista en donde almacenaremos las listas con el ID del producto y de la cantidad de veces que aparece

prod_sales = []

# Se cuenta la cantidad productos en todo el listado de ventas
num_prod = len(ventas)


for id in range(num_prod):  # El rango es de (0,96)
    new_id_prod = id + 1  # Se suma 1 porque las listas empiezan en 0.
    # En una fila de la lista, agregues el ID y su cantidad hasta aquí es 0. No se le ha sumado nada.
    row = [new_id_prod, 0]
    # Se irá agregando a la lista vacía, cada fila con el ID del producto y su cantidad
    prod_sales.append(row)

for sale in lifestore_sales:
    # En cada fila de ventas, el valor del segundo elemento es el ID del producto
    id_product = sale[1]
    prod_sales[id_product - 1][1] = prod_sales[id_product - 1][1] + 1

ordenamiento = sorted(prod_sales, key=lambda x: x[1], reverse=True)
# # #Regresará una lista ordenada a partir de los elementos en iterable.
# # #prod_sales es el objeto a ordenar
# # #lambda es una funcion anónima el cual toma el argumento x y lo devuelve en x[1] o sea el el elemento en el índice 1 en x
# # #Reverse como tal es un booleano el cual si esta como 'True'se mostrarán los elementos en reversa
# # 5 es la cantidad de objetos que te va a regresar
# print(ordenamiento)

# # #Aquí vamos a sacar la relación de la lista con listas de los mejores 5 productos con su nombre en la lista de productos:
for p in range(50):
    k = ordenamiento[p][0]
    indice = k - 1
    #print (lifestore_products[indice][0:2])
    print(
        f'El producto {lifestore_products[indice][1]} tuvo {ordenamiento[p][1]} ventas!')

# print (ordenamiento)
