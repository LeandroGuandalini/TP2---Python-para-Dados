# 1
idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}

maiores_de_idade = {nome: idade for nome, idade in idades.items() if idade >= 18}

print(maiores_de_idade)

# 2
tupla1 = (1,3,5)
tupla2 = (5,1,3)

if set(tupla1) == set(tupla2):
  print('As tupla possuem SIM os mesmos elementos.')
else: 
  print('As tuplas NÃO possuem os mesmos elementos')

# 3
lista = [4, 1, 5, 2, 3, 2, 4, 4]

frequencia = {}

for i in lista:
  if i in frequencia:
    frequencia[i] += 1
  else:
    frequencia[i] = 1

frequencia_crescente = dict(sorted(frequencia.items()))
print(frequencia_crescente)

# 4
