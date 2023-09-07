preco = int(input("Informe o preço do produto: "))
cupom = str(input("Vc tem um cupom de desconto? (sim ou nao)"))

if cupom == 'sim':
    preco = (preco - 10)
    print('O preço final do produto é: {}'.format(preco))
elif cupom == 'nao':
    print('O preço final do produto é: {}'.format(preco))