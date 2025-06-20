frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {}.'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra a apareceu na posição {}'.format(frase.rfind('A')+1))


