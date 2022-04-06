
livro = float(12.49)
cd = float(14.99)
barraChorolate = float(0.85)

entradaA = float((cd * 10) / 100)
somaA = float(cd + entradaA)
totalA = float(somaA + barraChorolate + livro)

caixaChocolateImportado = float(10.00)
frascoPerfumeImportado = float(47.50)

entradaB = float((caixaChocolateImportado * 5) / 100)
entradaBB = float((frascoPerfumeImportado * 15) / 100)
somaB = float((entradaB + entradaBB))
totalB = float(caixaChocolateImportado + entradaB + frascoPerfumeImportado + entradaBB)


frascoPerfumeImportadoC = float(27.99)
frascoPerfume = float(18.99)
cartelaAnalgesico = float(9.75)
caixaChocolateImportadoC = float(11.25)


entradaC = float((frascoPerfumeImportadoC * 15) / 100)
somaC = float(frascoPerfumeImportadoC + entradaC)
entradaCC = float((frascoPerfume * 10) / 100)
somaCC = float(frascoPerfume + entradaCC)
entradaCCC = float((caixaChocolateImportadoC * 5) / 100)
somaCCC = float(caixaChocolateImportadoC + entradaCCC)
totalC = float(entradaC + entradaCC + entradaCCC)
valorC = float(somaC + somaCC + somaCCC + cartelaAnalgesico)



print('=========================================================')
print('Saída 1')
print('1 Livro: ${:.2f}'.format(livro))
print('1 CD: ${:.2f}'.format(somaA))
print('1 barra de chocolate: ${:.2f}'.format(barraChorolate))
print('imposto de vendas ${:.2f}'.format(entradaA))
print('Total: ${:.2f}'.format(totalA))



print('=========================================================')
print('Saída 2')
print('1 caixa de chocolates importado: ${:.2f}'.format(caixaChocolateImportado + entradaB))
print('1 frasco de pergume importado: ${:.2f}'.format(entradaBB + frascoPerfumeImportado))
print('imposto sobre vendas: ${:.2f}'.format(somaB))
print('Total: ${:.2f}'.format(totalB))



print('=========================================================')
print('Saída 3')
print('1 frasco de perfume importado: ${:.2f}'.format(somaC))
print('1 frasco de pergume: ${:.2f}'.format(somaCC))
print('1 cartela de analgésicos: ${:.2f}'.format(cartelaAnalgesico))
print('1 caixa de chocolates importados: ${:.2f}'.format(somaCCC))
print('Imposto sobre vendas: ${:.2f}'.format(totalC))
print('Total: ${:.2f}'.format(valorC))
print('=========================================================')
print('''Os Resultados (Saida 2) frasco de perfume importado e
(Saida 3) caixa de chocolates importados não batem porem
o Juros aplicado na saída é superior ao solicitado.''')
print('=========================================================')