from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
This is the LifeStore_SalesList data:

lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]

lifestore_sales = [0 id_sale, 1 id_product,2 score (from 1 to 5), 3 date, 4 refund (1 for true or 0 to false)]
lifestore_searches = [id_search, id product]

"""
###GUIA DE COMO RELACIONAR UN ID DE VENTAS CON EL NOMBRE DE UN PRODUCTO###
nombres= []

for sales in lifestore_sales:
    id_sale= sales [0]
    id_product= sales [1]

    for product in lifestore_products:
        idproduct= product[0]
        nameproduct=product[1]

        if id_product == idproduct:
            nombres.append(nameproduct)

#print(nombres)

for name in nombres:
    print(name)
