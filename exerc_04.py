import math
ângulo = float(input('digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, seno))