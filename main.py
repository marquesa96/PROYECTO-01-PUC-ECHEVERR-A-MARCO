from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import Reviews
import category
import high_sales
import high_search
import Sales
import total_income_year
import totalsale_month

# Este es el Log In para entrar al sistema

# Declaramos las llaves. Sin estas
# no se puede ingresar al sistema.
User_ID = "marq"
Pass_ID = "pyth"

# Agregamos un saludo y seguido a este
# la primera entrada para comparar con la variable User_ID el cual será nuestro usuario.
# print ("Bienvenido al sistema")
username = input("""

Bienvenido al sistema,

Ingresa tu usuario:
""")

# Aquí inicia la comparación de entradas para saber si la persona puede o no acceder al sistema.
while True:
    if username == User_ID:  # Si el usuario es igual al valor de la variable declarada en User_ID, entonces imprime "Usuario correcto"
        print("Usuario correcto")
        # password = input ("Ingresa password: ")
        # if password == Pass_ID:
        # print ("Correcto, entraste al sistema")
        # break #Si ya se entró al sistema, entonces termina el bucle y muestra el mensaje final
        # else:
        # password = input ("Contraseña incorrecta, intenta de nuevo: ")
        break
    else:
        username = input("Usuario incorrecto, intenta de nuevo:  ")

password = input("Ingresa tu password: ")
while True:
    if password == Pass_ID:
        print("Password correcta")
        break
    else:
        password = input("Password incorrecta, intenta de nuevo:  ")
