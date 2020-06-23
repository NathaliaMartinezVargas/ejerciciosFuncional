
def entero(lista):
    if lista == []:
        return 0
    return entero(voltear[0]) + entero(voltear[1])

def voltear(lista):
    if lista == []:
        return 0
    return lista[::-1]

print(entero([1,2,3,4]))