def operacion():
    print("Operaciones disponibles: suma '+', resta '-', multiplicacion '*', division '/',")
    print("                         potenciacion '**', radicacion '*/', terminar '='")
    
    while True:
        resultado = input("Ingresa un numero: ")
        if resultado.replace(".","",1).isdigit():
            resultado = float(resultado)
            break
    
    while True:
        operacion = input("Ingresa una operacion: ")
        if operacion in ['+', '-', '*', '/', '**', '*/', '=']:
            if operacion == '=':
                break

            while True:
                num = input("Ingresa un numero: ")
                if num.replace(".","",1).isdigit():
                    num = float(num)
                    if operacion == '/' and num == 0:
                        print("Division por cero")
                        continue
                    break
            
            if operacion == '+':
                resultado += num
            elif operacion == '-':
                resultado -= num
            elif operacion == '*':
                resultado *= num
            elif operacion == '/':
                resultado /= num
            elif operacion == '**':
                resultado **= num
            elif operacion == '*/':
                resultado **= 1/num
            
    print("------------------")
    return resultado
