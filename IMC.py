print('=-='*35)
print('Calculadora de IMC')
print('=-='*35)

peso = float(input('Qual o seu peso? Kg'))
altura = float(input('Qual a sua altura? Cm'))

valor1 = altura ** 2
valor2 = peso / valor1

resultado = valor2

if resultado <= 18.5:
    print('Seu IMC é de {:.2f} e você está abaixo do peso!'.format(resultado))

elif resultado >= 18.6 and resultado <= 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal!'.format(resultado))

elif resultado >= 25.1 and resultado <= 30:
    print('Seu IMC é de {:.2f} e você está com sobre-peso!'.format(resultado))

elif resultado >= 30.1 and resultado <= 40:
    print('Seu IMC é de {:.2f} e você está com obesidade!'.format(resultado))

elif resultado >= 40.1:
    print('Seu IMC é de {:.2f} e você está com obesidade mórbida!'.format(resultado))

else:
    print('ERRO. Digite um valor válido')

print('TABELA DE IMC')

print(''' IMC	          Resultado

Menos do que 18,5    |    Abaixo do peso
Entre 18,5 e 24,9    |    Peso normal
Entre 25 e 29,9	     |    Sobrepeso
Entre 30 e 34,9	     |    Obesidade grau 1
Entre 35 e 39,9	     |    Obesidade grau 2
Mais do que 40       |    Obesidade grau 3(Obesidade mórbida)''')    