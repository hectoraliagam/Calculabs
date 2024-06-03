def promedio_aritmetico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    suma = num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == "=":
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            suma += num
            cant_num += 1
            
    prom_total = suma/cant_num
    return prom_total


def promedio_geometrico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    multi = num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == '=':
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            multi *= num
            cant_num += 1
    
    prom_total = multi**(1/cant_num)
    return prom_total


def promedio_armonico():
    print("Ingresa un numero o '=' para terminar")
    
    while True:
        num = input("Ingresa: ")
        if num.replace('.','',1).isdigit():
            num = float(num)
            break
    
    suma = 1/num
    cant_num = 1
    
    while True:
        num = input("Ingresa: ")
        if num == '=':
            print("------------------")
            break
        elif num.replace('.','',1).isdigit():
            num = float(num)
            suma += 1/num
            cant_num += 1
    
    prom_total = cant_num/suma
    return prom_total
