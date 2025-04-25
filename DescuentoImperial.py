#Programa que aplique el descuento a productos selecionado
from os import system

print("BIENVENIDO a DescuentoImperial ")
total_factura=0

#Datos del cliente 
print("¿CUAL ES TU NOMBRE?: ")
cliente=(input(""))
print(f"Listo {cliente}, Vamos a calcular tu total de manera precisa")

continuar= "s"
while continuar=="s":
     
#Secciones
    print("""Seleccione su seccion:
      1. Electrodomesticos🔧
      2. Jugueteria🌈
      3. Instrumentos🎤""")

#Seleccion de interes con bucle en caso de error
    while True:
        try:
            Seccion = int(input("iNGRESE EL NUMERO CORRESPONDIENTE A SU SECCION DE INTERES: "))
            while Seccion > 3 or Seccion < 1:
              Seccion = int(input("iNGRESE EL NUMERO CORRESPONDIENTE A SU SECCION DE INTERES: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    system("clear") 

#Productos de cada seccion

    match Seccion:
     
            case 1: print(""" 
                   a).Licuadora Oster 
                   b).Nevera HP
                   c).Lavadora 
                   d).Televisor LG
                   """)
          
            case 2: print(""" 
                   a).Carro hotwheels 
                   b).Barbie
                   c).Iron Man 
                   d).Peluche""")
              
            case 3: print(""" 
                   a).Bateria
                   b).Piano 
                   c).Flauta
                   d).Microfono""")
        
#Producto a comprar 
    Producto=input("SELECCIONA UNA LETRA CORRESPONDINETE A TU PRODUCTO ESCOGIDO? ")
    while Producto!="a" and Producto!="b" and Producto!="c" and Producto!="d":
        Producto=input("SELECCIONA UNA LETRA CORRESPONDINETE A TU PRODUCTO ESCOGIDO? ")

#Precio del producto 
    while True:
        try:
            Precio = int(input("INGRESA EL PRECIO EN DOLARES?: "))
            while Precio < 1:
                Precio = int(input("INGRESA UN NUMERO VALIDO. "))
            break
        except ValueError:
            print("INGRESA UN NUMERO VALIDO. ")

#Cantidad de productos escogidos
    while True:
        try:
            cantidad= int(input(f"CUANTOS DESEAS COMPRAR? {Producto}: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")  

#Recibo de la compra 
    print(f"\nResumen de la compra:")
    print(f"cliente: {cliente}")
    print(f"Producto: {Producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio por unidad: ${Precio}")
    
    total = Precio * cantidad
    total_factura= total_factura+total

#Preguntar si el usuario desea agregar otro producto
    continuar = input("¿Desea agregar otro producto? s/n: ")
    while continuar != "s" and continuar != "n":
        continuar = input("Por favor ingrese 's' para continuar o 'n' para finalizar: ")

#Descuento aplicado 
while True:
    try:
            descuento =int(input("CUAL ES TU DESCUENTO? : "))
            while descuento < 0 or descuento > 100:
                descuento =int(input("INGRESA UN NUMERO VALIDO. "))
            break
    except ValueError:
            print("INGRESA UN NUMERO VALIDO. ")
    break

#Total de la compra con descuento
total_con_descuento = total_factura* (1 - descuento / 100)

# Mostrar el total
print(f"El total de la compra es: {total}")
print(f"Descuento: {descuento}%")
print(f"Total: ${total_con_descuento:.2f}")


print("¡Gracias por tu compra! ¡Hasta pronto!")


