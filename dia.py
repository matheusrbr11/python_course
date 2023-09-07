dia = 2

if dia >=1 and dia <=7:
    match dia:
    
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case _:
            print("Final de Semana")
else:
    print("Dia Inválido!")
        