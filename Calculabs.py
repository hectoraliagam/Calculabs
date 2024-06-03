from menu import menu_opc , menu_opc_esp 
from salir import opc_exit_menu , opc_exit_menu_esp
from calcular_operaciones import operacion
from calcular_promedios import promedio_aritmetico , promedio_geometrico , promedio_armonico


while True:
    
    opc = menu_opc()
    if opc == 0:
        opc = opc_exit_menu()
        if opc_exit_menu() == -1:
            break
        else:
            continue
    
    elif opc == 1:
        print("------------------")
        print("Version: 1.6.6")
        opc = opc_exit_menu()
        
    elif opc == 2:
        
        while True:
            
            opc_esp = menu_opc_esp()
            if opc_esp == 0:
                opc_esp = opc_exit_menu_esp()
            elif opc_esp == -1:
                opc = menu_opc()
                break
                
            elif opc_esp == 1:
                print(f"La respuesta es {operacion()}")
                opc_esp = opc_exit_menu_esp()
                
            elif opc_esp == 2:
                print(f"La respuesta es {promedio_aritmetico()}")
                opc_esp = opc_exit_menu_esp()
            
            elif opc_esp == 3:
                print(f"La respuesta es {promedio_geometrico()}")
                opc_esp = opc_exit_menu_esp()
                
            elif opc_esp == 4:
                print(f"La respuesta es {promedio_armonico()}")
                opc_esp = opc_exit_menu_esp()
                
            else:
                opc_esp = menu_opc_esp()

#Hay un problema que ocurre cada vez que luego de haber colocado en el segundo menu la tecla 0 y despues colocado la v para volver, pasa que si el usuario ingresa cualquier tecla, el programa me envia al menu secundario :/
