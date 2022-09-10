# 3.Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
# 5. Digitar 0 para SALIR

from itertools import product
import os
os.system ("cls")
i=1
productos=[

]
print("***MENU***")
print("(1) Crear datos del producto")
print("(2) Mostrar listado de productos")
print("(3) Buscar por codigo y editar")
print("(4) Buscar por codigo y eliminar")
print("(0) Terminar")
while(i!=0):
    producto={

    }
    i=int(input("Digita una opcion: "))
    if(i==1):
        print("Crear datos de la producto")
        #append
        producto['codigo']=input("Digita el codigo del producto: ")
        producto['nombre']=input("Digita el nombre del producto: ")
        producto['precio']=int(input(f"Digita el precio del producto: "))
        productos.append(producto)
        print("***MENU***")
        print("(1) Crear datos del producto")
        print("(2) Mostrar listado de productos")
        print("(3) Buscar por codigo y editar")
        print("(4) Buscar por codigo y eliminar")
        print("(0) Terminar")
    elif(i==2):
        print("Mostrar listado de productos")        
        for elemento in productos:           
            print(elemento)
            print("")
        print("***MENU***")
        print("(1) Crear datos del producto")
        print("(2) Mostrar listado de productos")
        print("(3) Buscar por codigo y editar")
        print("(4) Buscar por codigo y eliminar")
        print("(0) Terminar")
    elif(i==3):
        print("Buscar por codigo y editar")
        codigo=input(f"Digita el codigo del producto: ")        
        for elemento in productos:
            if(elemento['codigo'] == codigo):
                print("encontrado")
                print(elemento)
                precioNuevo=int(input(f"Digita el precio del producto: "))
                elemento['precio']=precioNuevo
            else:
                print("NO ESTA")
    elif(i==4):
        print("Buscar por codigo y eliminar")
        codigo=input(f"Digita el codigo del producto: ")        
        for elemento in productos:
            if(elemento['codigo'] == codigo):
                print("encontrado")
                print(elemento)                
                #elemento['codigo'].remove()
                productos['codigo'].remove()
                #elemento.remove(codigo)
                #elemento.remove(productos(codigo))
                #productos.remove(codigo)
                #productos.remove(producto(codigo))               
            else:
                print("NO ESTA")        
    elif(i==0):
        break
    else:
        print("Digite una opcion valida.")
else:
    print("Digite una opcion valida.")