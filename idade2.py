import datetime

ano = int(input("Ano do seu nascimento: "))
tempo = datetime.datetime.now()
idade = tempo.year - ano
print(idade)
