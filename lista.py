lista = ['Banana', 'Maça', 'Uva']

def add_fruta(a,b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("Abacate","Sorvete")

def del_fruta():
    lista.pop(0)
    print(lista)

del_fruta()