def multiplo(lista):
    if lista == []:
        return []
    return [[x*3 for x in lista[0]]] + multiplo(lista[1:])

def digitos(numero):
    return [int(x) for x in str(numero)]

def listar(lista):
    if lista == []:
        return []
    return [digitos(lista[0])] + listar(lista[1:])

print(multiplo(listar([8,9,4])))
