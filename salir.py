def opc_exit_menu():
    while True:
        print("------------------")
        opc_exit = input("¿Desea continuar? (salir 'e', menu principal 'p'): ")
        if opc_exit == 'e':
            print("------------------")
            print("Gracias por utilizar el programa, vuelva pronto! :D")
            print("------------------")
            return -1
        elif opc_exit == 'p':
            opc = 0
            return opc
        else:
            continue

def opc_exit_menu_esp():
    while True:
        print("------------------")
        opc_exit_esp = input("¿Desea continuar? (volver 'v', menu math 's'): ")
        if opc_exit_esp == 'v':
            opc_esp = -1
            return opc_esp
        elif opc_exit_esp == 's':
            opc_esp = 0
            return opc_esp 
        else:
            continue
