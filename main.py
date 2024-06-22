from functions import *

menuAbierto = True
while menuAbierto:
    mostrarMenu()
    try:
        option = int(input("Ingrese opcion\n"))
        if option == 1:
            limpiarTerminal()
            print("***Grabar persona***")
            registrarPersona()
        elif option == 2:
            print("***Buscar persona***")
            buscarPersona()
        elif option == 3:
            print("***Imprimir Certificado***")
            imprimirCertificado()
        elif option == 4:
            os.system("cls")
            print("****************************")
            print("***Has salido del sistema***")
            print("****************************")
            menuAbierto = False
        else:
            print("opcion inválida")
    except:
        print("Opcion invalida except")
