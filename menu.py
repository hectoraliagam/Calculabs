def menu_opc():
    print("------------------")
    print("Bienvenidos a Calculabs")
    print("He aqui el menu de opciones:")
    print("Salir/Menu -------- 0")
    print("Version ----------- 1")
    print("Menu Oper --------- 2")
    opc = input("Inserta: ")
    if opc.isdigit():
        opc = int(opc)
        return opc
    else:
        return opc


def menu_opc_esp():
    print("------------------")
    print("Volver/Menu_op ---- 0")
    print("Operaciones ------- 1")
    print("Promedio Arit ----- 2")
    print("Promedio Geom ----- 3")
    print("Promedio Armo ----- 4")
    opc_esp = input("Inserta: ")
    if opc_esp.isdigit():
        opc_esp = int(opc_esp)
        return opc_esp
    else:
        return opc_esp
