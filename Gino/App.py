import Funciones
import random

numero_random = random.randint(100000,199999)

while True:
    print("Menu principal")
    print("1. Registrar consumo")
    print("2. Listar todos los consumos")
    print("3. Imprimir hoja de consumo")
    print("4. Buscar un consumo ID")
    print("5. Salir del programa")

    menu_opc = input("Ingrese una de las opciones utilizando numeros del 1 al 5: ")
    while True:
        if menu_opc == "1":
                while True:
                        while True:
                         nombre = input("Ingresa un Nombre: ")
                         if len(nombre) in range(4,1000) and nombre.isalpha():
                           print("El Nombre ingresado es valido")
                           break
                         else:
                             print("Nombre no valido")

                        edad = int(input("Ingrese la edad: "))
                        if edad <= 0:
                            print("El edad ingresado es valido")
                            break
                        else:
                            print("El edad ingresado no es valido, por favor intentelo nuevamente")
                            break
                equipo = int(input("Seleccione a que equipo pertenece: \n1. Los Genios de la garrafa\n2. Los Compiladores Despiertos \n3. Codigo Borracho\n4. Los programadores perezosos\n5. Ctrl+Alt+Derrota\n"))
                cafe_viernes = int(input("Ingrese las tazas de cafe que consumio el dia viernes: "))
                cafe_sabado = int(input("Ingrese las tazas de cafe consumidas el sabado: "))
                cafe_domingo = int(input("Ingrese las tazas de cafe consumidas el domingo: "))
                break
                
            
        elif menu_opc == "2":
            print(f"ID Consumo    Jugador           Edad    Equipo            Viernes     Sabado     Domingo")
            print(f" {numero_random}       {nombre}               {edad}       {equipo}                  {cafe_viernes}           {cafe_sabado}           {cafe_domingo}")
            break
        



        




        

        



