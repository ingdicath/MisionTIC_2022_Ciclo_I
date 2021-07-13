def tipo_melenudos(melenudos):
    result = list()
    for melenudo in melenudos:
        if melenudo not in result:
            result.append(melenudo)
    return result


def si_son(turnos, melenudos, tipo_melenudo):
    res = list()
    for turno in turnos:
        if melenudos[int(turno)] == tipo_melenudo:
            res.append(turno)
    return res


def no_estan(lista_deiv, lista_james):
    result = list()
    for guest_deiv in lista_deiv:
        if guest_deiv not in lista_james:
            result.append(guest_deiv)
    return result


def uno_y_uno(lista_1, lista_2):
    count_1 = 0
    count_2 = 0
    for item in lista_1:
        if item not in lista_2:
            count_1 += 1
    for item in lista_2:
        if item not in lista_1:
            count_2 += 1
    if count_1 <= count_2:
        return count_1
    elif count_2 < count_1:
        return count_2


# Ejemplo input: jalacables,poguero,jalacables,showsero,poguero,poguero
melenudos = input().split(',')
print(tipo_melenudos(melenudos))

# Ejemplo input turno: 1,3,5,7
# Ejemplo input lista: jalacables,poguero,jalacables,showsero,poguero,poguero,showsero,jalacables
# Ejemplo input tipo: jalacables
turno = input().split(',')
lista_melenudos = input().split(',')
tipo = str(input())
print(si_son(turno, lista_melenudos, tipo))

# Ejemplo input lista_deiv: 1,2,3,5,7,8
# Ejemplo input lista_james: 2,3,7,8
lista_deiv = input().split(',')
lista_james = input().split(',')
print(no_estan(lista_deiv, lista_james))

# Ejemplo input lista_1: 1,2,4,5,7,8
# Ejemplo input lista_2: 2,3,7,8
lista_deiv = input().split(',')
lista_james = input().split(',')
print(uno_y_uno(lista_deiv, lista_james))
