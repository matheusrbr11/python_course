lista = [5,20,10,15,20,10,15,5,5,5,20,10,5,5,10]

mais_frequente = max(set(lista), key=lista.count)
print(mais_frequente)