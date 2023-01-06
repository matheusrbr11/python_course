notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))
notaC=float(input("Informe a terceira nota: "))
notaD=float(input("Informe a quarta nota: "))

#calcular media
mediafinal = (notaA + notaB + notaC + notaD) / 4

#verificação
if mediafinal >=7.0:
    print("A Média: %.1f - Aprovado "% mediafinal)
else:
    print("A Média: %.1f - Reprovado "% mediafinal)