def dobra(lst):
    print(lst)
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1
    print(lst)



#programa principal
lista = [6,3,4,5,4,6,7,8]
dobra(lista)