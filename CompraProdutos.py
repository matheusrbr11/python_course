total=0
valor=float(input("Informe o valor do produto: R$"))

while valor !=0:
    
    if valor<0:
        print("Valor inválido!")
    else: 
        total=total+valor
    valor=float(input("Informe o valor do produto: R$"))

if total>1000:
    print("Subtotal: R$",total)
    total-=total*0.1
    print("Total a pagar: R$", total)
else:
    print("Subtotal: R$",total)
    print("Total a pagar: R$", total)