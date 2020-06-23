def mayor(lista1, lista2):
    if lista1 and lista2 == []:
        return []
    if lista1[0]>lista2[0]:
        return lista1[0]
    if lista2[0]>lista1[0]:
        return lista2[0]
    return lista1[0]

def mayorn(lista1, lista2):
    if lista1 and lista2 == []:
        return []
    if lista1[1:]>lista2[1:]:
        return lista1[1:]
    if lista2[1:]>lista1[1:]:
        return lista2[1:]
    return lista1[1:]

def menor(lista1, lista2):
    if lista1 and lista2 == []:
        return []
    if lista1[0]<lista2[0]:
        return lista1[0]
    if lista2[0]<lista1[0]:
        return lista2[0]
    return lista1[0]

def menorn(lista1, lista2):
    if lista1 and lista2 == []:
        return []
    if lista1[1:]<lista2[1:]:
        return lista1[1:]
    if lista2[1:]<lista1[1:]:
        return lista2[1:]
    return lista1[1:]

def suma(lista1,lista2):
    if lista1 and lista2 == []:
        return 0
    return(mayor([1,2,3], [2,3,5]) + menor([3,2,3], [2,3,5]))

def suman(lista1,lista2):
    if lista1 and lista2 == []:
        return 0
    return(mayorn([1,2,3], [2,3,5]) + menorn([3,2,3], [2,3,5]))

def tupla():
    return (mayor([1,2,3], [2,3,5]), menor([1,2,3], [2,3,5]), mayor([1,2,3], [2,3,5]) + menor([3,2,3], [2,3,5]))

def tupla2():
    return (mayorn([1,2,3], [2,3,5]), menorn([1,2,3], [2,3,5]), mayorn([1,2,3], [2,3,5]) + menorn([3,2,3], [2,3,5]))

print("mayor ", mayor([1,2,3], [2,3,5]))
print("mayor1 ", mayorn([1,2,3], [2,3,5]))
print("menor ", menor([1,2,3], [2,3,5]))
print("menor1 ", menorn([1,2,3], [2,3,5]))
print("Suma: ", suma([1,2,3], [2,3,5]))
print("Suma1: ", suman([1,2,3], [2,3,5]))
print("tupla", tupla())
print("tupla2", tupla2())
