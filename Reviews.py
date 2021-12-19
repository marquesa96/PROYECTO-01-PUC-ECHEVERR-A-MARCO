from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# NO SE LIMPIA LA LISTA DE REVIEWS PUESTO QUE PUEDEN HABER
# PRODUCTOS EN DEVOLUCIÓN QUE HAYAN SIDO CALIFICADOS
review_of_products = []
for producto in lifestore_products:
    id_producto = producto[0]
    # hacemos un esqueleto donde irán la suma de reviews y el numero de ventas del prod
    int_list = [id_producto, 0, 0]
    review_of_products.append(int_list)

for sale in lifestore_sales:
    id_prod = sale[1]
    review = sale[2]

    index = id_prod - 1
    # Aquí lo que se hace es sumar todas las reviews de un producto
    review_of_products[index][1] += review
    # Aquí se suman todas las ventas que tenga el producto
    review_of_products[index][2] += 1

# Aqui limpiamos todos aquellos productos que no tuvieron ventas
# puesto que al no tener compras es un hecho que no recibieron reviews
new_review_of_products = []
for rop in review_of_products:
    idprod = rop[0]
    suma_de_reviews = rop[1]
    suma_de_ventas = rop[2]

    if suma_de_ventas == 0:
        continue
    else:
        new_review_of_products.append(rop)


# Aqui vamos a sacar el promedio de reviews por cada producto

for nrop in new_review_of_products:
    nrop[1] = nrop[1] / nrop[2]
   # print(nrop)

print(f'////////////////////////////////////////////////////////////////////////////////')
print(f'Mejores calificados: ')
orden = sorted(new_review_of_products, key=lambda x: x[1], reverse=True)[:5]
for j in orden:
    print(j)
for p in range(5):
    k = orden[p][0]
    indice = k - 1
    print(
        f'El producto {lifestore_products[indice][1]} tuvo {orden[p][1]} en promedio de reviews y {orden[p][2]} ventas')
print(f'////////////////////////////////////////////////////////////////////////////////')
print(f'Peores calificados: ')
orden = sorted(new_review_of_products, key=lambda x: x[1])[:5]
for j in orden:
    print(j)
for p in range(5):
    k = orden[p][0]
    indice = k - 1
    print(
        f'El producto {lifestore_products[indice][1]} tuvo {orden[p][1]} en promedio de reviews y {orden[p][2]} ventas')
