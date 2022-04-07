print('Sexta de compras 01 ')
print('Sexta de compras 02 ')
print('Sexta de compras 03 ')
print('Sexta de compras 04 ')



livro = float(12.49)
cd = float(14.99)
barraChorolate = float(0.85)

caixaChocolateImportado = float(10.00)
frascoPerfumeImportado = float(47.50)

frascoPerfumeImportadoC = float(27.99)
frascoPerfume = float(18.99)
cartelaAnalgesico = float(9.75)
caixaChocolateImportadoC = float(11.28)



entradaA = float((cd * 10) / 100)
somaA = float(cd + entradaA)
totalA = float(somaA + barraChorolate + livro)

entradaB = float((caixaChocolateImportado * 5) / 100)
entradaBB = float((frascoPerfumeImportado * 15) / 100 )
somaB = float((entradaB + entradaBB))
totalB = float(caixaChocolateImportado + entradaB + frascoPerfumeImportado + entradaBB)


entradaC = float((frascoPerfumeImportadoC * 15) / 100)
somaC = float(frascoPerfumeImportadoC + entradaC)
entradaCC = float((frascoPerfume * 10) / 100)
somaCC = float(frascoPerfume + entradaCC)
entradaCCC = float((caixaChocolateImportadoC * 5) / 100)
somaCCC = float(caixaChocolateImportadoC + entradaCCC)
totalC = float(entradaC + entradaCC + entradaCCC)
valorC = float(somaC + somaCC + somaCCC + cartelaAnalgesico)


a = int(input('Digite Sua Escolha '))

if a == 1:
    um = 0
    while um != 4:
        print('''
        [ 1 ] livros
    [ 2 ] cd
    [ 3 ] BarraChorolat
    [ 4 ] Finalizar''')

    um = int(input('Qual é o kit '))

    if um == 1:
        print("========================================")
        print('1 Livro: ${:.2f}'.format(livro))

    elif um == 2:
        print('1 CD: ${:.2f}'.format(somaA))
    elif um == 3:
        print('1 barra de chocolate: ${:.2f}'.format(barraChorolate))
    elif um == 4:
        print("========================================")
        print('       Obrigado pela compra!')
        print("========================================")
        print('========================================')

    elif a == 2:
        dois = 0
        while dois != 3:
            print('''
            [ 1 ] caixa de chocolates
            [ 2 ] frasco de pergume importado
            [ 3 ] Finalizar''')

        dois = int(input('Qual é o kit '))

if dois == 1:

    print('1 caixa de chocolates importado: ${:.2f}'.format(caixaChocolateImportado + entradaB))

elif dois == 2:
    print('1 frasco de pergume importado: ${:.2f}'.format(entradaBB + frascoPerfumeImportado))

elif dois == 3:

    print("========================================")
    print('       Obrigado pela compra!')
    print("========================================")
    print('========================================')

elif a == 3:
    tres = 0
    while tres != 4:
        print('''
            [ 1 ] livros/CD/BarraChorolat
         [ 2 ] cd
         [ 3 ] BarraChorolat
         [ 4 ] Finalizar''')

tres = int(input('Qual é o kit '))

if tres == 1:
    print('1 frasco de perfume importado: ${:.2f}'.format(somaC))
elif tres  == 2:
    print('1 frasco de pergume: ${:.2f}'.format(somaCC))
elif tres  == 3:
    print('1 cartela de analgésicos: ${:.2f}'.format(cartelaAnalgesico))
elif tres  == 4:
    print('1 caixa de chocolates importados: ${:.2f}'.format(somaCCC))

elif tres  == 5:
    print("========================================")
    print('       Obrigado pela compra!')
    print("========================================")

elif a == 4:
    print("========================================")
    print('       Obrigado pela compra!')
    print("========================================")



