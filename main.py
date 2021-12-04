from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
This is the LifeStore_SalesList data:

lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_searches = [id_search, id product]
""" 
# # Creando un for
# # Creando la variable product.
# # print(type(lifestore_products))
# for prod in lifestore_products:
#     id = prod[0]
#     nombre = prod[1][:10]
#     precio = prod[2]
#     categoria = prod[3]
#     print(categoria)
#     # print('El precio de ', nombre, ' es de ', precio)
#     # print(f'El precio de {nombre} es de {precio}')

# Suma de todos los productos de la categoria 'discos duros'
categoria_buscada = 'discos duros'

# dentro de esta lista vamos a guardar todos los productos que 
# pertenezcan a esta catgroria
categoria_discos_duros = []

for producto in lifestore_products:
    cat_prod = producto[3]
    if cat_prod == categoria_buscada:
        categoria_discos_duros.append(producto)

for prod in categoria_discos_duros:
    print(prod)
  