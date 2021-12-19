from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

ventas = []
# lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
for sale in lifestore_sales:
    refund = sale[4]
    if refund == 1:
        continue
    else:
        ventas.append(sale)


precio = []

for venta in ventas:
    id_sale = venta[0]
    id_product = venta[1]

    for product in lifestore_products:
        idproduct = product[0]
        nameproduct = product[1]
        price = product[2]

        if id_product == idproduct:
            precio.append(product[2])

listsum = sum(precio)
print(listsum)
