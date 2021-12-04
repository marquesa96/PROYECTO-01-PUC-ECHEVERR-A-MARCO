from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_searches = [id_search, id product]
""" 

#Aquí vamos a sacar los 5 productos más vendidos 

best_sale = {} #Crea un diccionario 

print ("El num de ventas x producto es:  ")


for sale in lifestore_sales:
    value = sale[:][1] #Se define como una variable el la posición del dato que nos interesa
    if value in best_sale: #Si el ID del producto ya ha pasado por el diccionario sumale 1
        best_sale [value] += 1
    else:
        best_sale [value] = 1 #Si no, se inicializa en uno, por ejemplo la primera vez 

    #print (sale[:][1]) # Accede a todas las listas pero solo al ID del producto de cada lista
print (best_sale) # Obtento la lista con el total de cada producto 
print (len(best_sale))#Devuelve la cantidad de tipos de productos vendidos en el año

best_sale_ID = 1
high_frecuence = lifestore_sales [:][1]

for value in best_sale:
    if best_sale [value] > best_sale_ID:
        high_frecuence = value
        best_sale_ID = best_sale [value]

conteo = best_sale [int (high_frecuence)] + 5
print (f"El mas vendido es {high_frecuence}, encontrado {conteo} veces")