# 1 Crie um dicionário com as idades de várias pessoas e retorne um novo dicionário que contenha apenas as pessoas maiores de idade (Ex: idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16} deve retornar {'Alice': 22, 'Carol': 19}).

idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}

maiores_de_idade = {nome: idade for nome, idade in idades.items() if idade >= 18}

print(maiores_de_idade)

# 2 Crie duas tuplas e verifique se elas possuem os mesmos elementos, independente da ordem (Ex: tupla1 = (1,3,5) e tupla2 = (5, 1, 3) possuem SIM os mesmos elementos).

tupla1 = (1,3,5)
tupla2 = (5,1,3)

if set(tupla1) == set(tupla2):
  print('As tupla possuem SIM os mesmos elementos.')
else: 
  print('As tuplas NÃO possuem os mesmos elementos')

# 3 Crie uma lista que possua números repetidos e conte a frequência de cada elemento nessa utilizando um dicionário (Ex: lista = [4, 1, 5, 2, 3, 2, 4, 4] deve retornar dicionario = {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}).

lista = [4, 1, 5, 2, 3, 2, 4, 4]

frequencia = {}

for i in lista:
  if i in frequencia:
    frequencia[i] += 1
  else:
    frequencia[i] = 1

frequencia_crescente = dict(sorted(frequencia.items()))
print(frequencia_crescente)

# 4 Crie dois dicionários (com 2 ou mais elementos) e verifique se um é subconjunto de outro.

dic1 = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32,'g':64}
dic2 = {'c':4,'e':16,'g':64}

conjunto1 = set(dic1.items())
conjunto2 = set (dic2.items())

if conjunto1 <= conjunto2:
  print("Dicionário 1 é um subconjunto de dicionário 2.")
else:
  print('Dicionário 1 não é um subconjunto de dicionário 2.')

if conjunto2 <= conjunto1:
  print('Dicionário 2 é um subconjunto de dicionário 1.')
else:
  print('Dicionário 2 não é um subconjunto de dicionário 1.')

#5 Crie um dicionário que mapeia alunos e suas notas e retorne um novo dicionário que classifique os alunos em "Aprovado" (nota >= 7) e "Reprovado" caso contrário (Ex: notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5} deve retornar {'Aprovado': ['Ana', 'Maria'], 'Reprovado': ['Pedro', 'José']}).

alunos = {
  'Ana': [8.5, 7.0, 9.0],
  'Pedro': [6.0, 5.5, 6.5],
  'Maria': [7.5, 8.0, 7.0],
  'José': [5.5, 6.0, 6.5]
}

print(alunos)

def calcular_media(alunos):
  '''Função com a finalidade de calcular a média dos alunos e retornar se cada um deles foram aprovados ou reprovados'''
  aluno, lista_notas = alunos
  media = sum(lista_notas) / len(lista_notas)
  return(aluno, "Aprovado" if media >= 7 else "Reprovado")

resultado = map(calcular_media, alunos.items())

classificacao = {"Aprovado": [], "Reprovado": []}
for aluno, status in resultado:
  classificacao[status].append(aluno)

print(classificacao)

# 6 Crie uma lista (maior que 5 elementos) e encontre os dois números cuja soma seja o mais próximo possível de zero.

lista = [1,2,1,4,5,6,7]

menor_soma = float('inf')
pares = (None, None)

for i in range(len(lista)):
  for u in range(len(lista)):
    if u != i:
      soma = lista[i] + lista[u]
      if abs(soma) < abs(menor_soma):
        menor_soma = soma
        pares = (lista[i], lista[u])

print(f'Os dois números cuja soma é mais próxima de zero são {pares[0]} e {pares[1]}, com soma {menor_soma}')

# 7 Crie um programa que permita ao usuário registrar as notas de uma turma de estudantes. O usuário deve inserir os nomes dos alunos e suas respectivas notas. O programa deve continuar solicitando entradas até que o usuário digite "fim". Após o término, o programa deve exibir os nomes dos alunos junto com suas notas.

alunos = {}

while True:
  aluno = input('Informe o nome do aluno (ou digite "fim" para terminar): ')
  if aluno.lower() == 'fim':
    break
  elif aluno == '':
    print('Por favor, insira um nome válido')
  else:
    notas = []
    while True:
      try:
        nota = input('Informe uma nota do aluno (ou digite "fim" para terminar): ')
        if nota.lower() == 'fim':
          break
        elif nota == '':
          print('Por favor, insira um valor')
        else: 
          notas.append(float(nota))
      except ValueError:
        print( 'Por favor, insira um número válido para a nota.')
    
    alunos[aluno] = notas
    print(f'Aluno {aluno} e suas notas {notas} foram adicionados.')

print('Todos os alunos e suas notas: ')
for aluno, notas in alunos.items():
  print(f'{aluno}: {notas}')

# 8 Número Mágico: Crie um código para adivinhar um número aleatório entre 1 e 20 com um limite de 4 tentativas (ou seja, o programa recebe essas tentativas do usuário e verifica se o número que o usuário escreveu é o número mágico). OBS: Para cada número digitado, informe se ele está abaixo ou acima do número mágico.

import random

numero_magico = random.randint(1,20)
tentativas = 4

print("Você tem 4 tentativas para acertar, o número pode ser um valor de 1 a 20.")

for tentativa in range(tentativas):
  palpite = int(input(f'Tentativa {tentativa+1}: Qual é o seu palpite? '))

  if palpite == numero_magico:
    print("Parabéns, você acertou!")
    break
  elif palpite < numero_magico:
    print("O número secreto é maior.")
  else:
    print('O número secreto é menor.')
  
  if tentativa == range(tentativas):
    print(f'Você não acertou! O número secreto era {numero_magico}')

# 9 Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo. OBS: Non-case sensitive e sem contar os espaços (Ex: "A mala nada na lama" é um palíndromo).

def checar_palindromo(entrada):
  '''Essa função tem como objetivo checar se a palavra ou frase fornecida é um palíndromo (a mesma frase/palavra ao contrário)'''
  frase = entrada.replace(' ','').lower()

  if frase == frase[::-1]:
    return True
  else:
    return False

entrada = input('Digite uma palavra ou frase para checar se é um palíndromo: ')

if checar_palindromo(entrada):
  print('É um palíndromo!')
else:
  print('Não é um palíndromo')

# 10 Crie uma lista de dicionários (de 4 ou mais elementos), em que cada elemento possui o nome e a nota dos alunos e ordene a lista de maneira decrescente por nota. OBS: Faça o exercício utilizando apenas estruturas básicas, sem chamar funções de sort ou algo do tipo.

alunos = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'Pedro', 'nota': 6.0},
    {'nome': 'Maria', 'nota': 7.5},
    {'nome': 'José', 'nota': 5.5},
    {'nome': 'Carlos', 'nota': 9.0}
]

for i in range(len(alunos)):
  for j in range(i+1, len(alunos)):
    if alunos[i]['nota'] < alunos[j]['nota']:
      alunos[i], alunos[j] = alunos[j], alunos[i]

for aluno in alunos:
  print(f'Aluno: {aluno['nome']}, Nota: {aluno['nota']}')

# 11 Crie uma lista (de 4 ou mais elementos) e um programa que permita ao usuário acessar os elementos desta lista. O usuário deve inserir um índice (número inteiro) para obter o elemento correspondente na lista. Trate casos em que o índice inserido está fora do intervalo da lista ou se o usuário inserir algo que não seja um número (Dica: ‘try’, ‘except’). Se ocorrer um erro, informe ao usuário qual o erro e permita que ele tente novamente.

lista = [1,4,5,6,12,1]

def retornar_indice(lista):
  '''Essa função tem como objetivo retornar um índice, escolhido pelo usuário, de uma lista pré-definida'''
  entrada = int(input('Informe o índice desejado (número inteiro): '))

  try: 
    if entrada == '':
      print("Informe um valor")
      retornar_indice(lista)
    elif entrada > len(lista)-1:
      print('O valor informado é maior que o número de itens da lista, favor tentar novamente')
      retornar_indice(lista)
    else:
      print(f'O valor do índice {entrada} é: {lista[entrada-1]}')
  except ValueError:
    print('Você não digitou um número inteiro, por favor, tente novamente')
    retornar_indice(lista)

retornar_indice(lista)

# 12 Joel possui uma barraca na feira e quer dar um presente a um cliente. Crie um programa que receba do usuário uma lista de frutas disponíveis na barraca e as quantidades correspondentes de cada fruta. O programa deve escolher aleatoriamente uma fruta para presentear o cliente. Se o número de quantidades fornecido for maior do que o número de frutas, o programa deve contabilizar apenas até o último índice da lista de frutas. Caso o número de quantidades seja menor do que o número de frutas, o programa deve solicitar ao usuário que reescreva a lista de quantidades (Ex: input do usuário: ‘maçã, banana, laranja’ | ‘10, 5, 8’).

def escolher_fruta():
  '''
    Esta função solicita ao usuário uma lista de frutas e suas respectivas quantidades disponíveis 
    em uma barraca. Em seguida, ela escolhe aleatoriamente uma fruta com base nas quantidades 
    fornecidas e informa ao usuário qual fruta será dada como presente.
    
    O programa garante que:
    - O número de quantidades não exceda o número de frutas, cortando o excesso se necessário.
    - Se o número de quantidades for menor que o número de frutas, o usuário será solicitado a inserir novamente as quantidades.
    - A escolha da fruta é feita com base nas quantidades, com frutas mais abundantes tendo maior chance de serem escolhidas.

    Exemplo de uso:
        escolher_fruta()
    '''
  frutas = input('Digite as frutas disponíveis na barraca (separadas por vírgula): ').split(',')
  frutas = [fruta.strip() for fruta in frutas] #remove espaços

  while True:
    quantidades = input('Digite as quantidades de cada fruta (separadas por vírgulas): ').split(',') 
    quantidades = [quantidade.strip() for quantidade in quantidades]

    if len(quantidades) > len(frutas):
      quantidades = quantidades[:len(frutas)]
      print('O número de quantidades foi ajutado para o número de frutas')
      break
    elif len(quantidades) < len(frutas):
      print('O número de quantidades é menor que o número de frutas. Por favor, insira novamente.') 
    else:
      break

  fruta_escolhida = random.choices(frutas)

  print(f'A fruta escolhida para presentear o cliente é: {fruta_escolhida}')



escolher_fruta()

# 13 Escreva uma função que receba um texto do usuário e printe esse texto.

def receber_e_imprimir_text():
  '''Essa função recebe um texto do usuário e o imprime'''
  texto = input('Digite um texto: ')
  print(texto)

receber_e_imprimir_text()

# 14 Defina uma função chamada ‘dividir’ que recebe dois números e retorna dois outputs: o resultado inteiro da divisão e o resto. Escreva uma docstring para documentar o que a função faz, quais são seus parâmetros, e o que ela retorna.

def dividir(num1, num2):
  '''
  Esta função recebe como parâmetro dois números, que foram inseridos pelo usuário. Com esses dois número, retorna o resultado inteiro e o resto da divisão.

  Parâmetros: 
  num1 (int ou float): o número a ser dividido.
  num2 (int ou float): o número pelo qual o dividendo será dividido

  retorna: 
  tuple: Uma tupla contendo dois valores:
    -O resultado da divisão inteira (parte inteira da divisão).
    -O resto da divisão (o valor do módulo)
  '''
  return num1//num2, num1%num2

num1 = float(input("Insira um valor: "))
num2 = float(input("Insira outr valor: "))

inteiro, resto = dividir(num1, num2)

print(f'A divisão inteira foi: {inteiro}, o resto foi: {resto}')

# 15 Defina uma função que receba um nome e uma idade como argumentos obrigatórios e uma cidade como argumento opcional (valor padrão "Desconhecida"). A função deve imprimir uma mensagem personalizada com essas informações. Ex: "Maria tem 30 anos e mora em São Paulo".

def mensagem_personalizada(nome,idade, cidade='Desconhecida'):
  '''
  Essa função recebe o nome, idade e uma cidade (opcional) e imprime uma mensagem personalizada

  Parâmetros:
  nome (str): O nome da pessoa.
  idade (int): A idade da pessoa.
  cidade (str, opcional): A cidade onde a pessoa mroa. O valor padrão é 'Desconhecida'.

  Retorna:
  Uma mensagem personalizada utilizando os parâmentros
  '''
  print(f'{nome} tem {idade} anos e mora em {cidade}')

mensagem_personalizada("Leandro", 24)
mensagem_personalizada("Leandro", 24, "Tupã")

# 16 Defina uma função chamada calcular_total que receba dois parâmetros: preço e quantidade, onde a quantidade tem o valor padrão de 1. A função deve calcular e retornar o total, multiplicando o preço pela quantidade.

def calcular_total(preco, quantidade=1):
  '''
  Essa função recebo o preço e quantidade (opcional) e retorna o total, multiplicando o preço pela quantidade

  Parâmetros:
  preco (float): O preço do produto.
  quantidade (int, opcional): A quantidade do produto. O valor padrão é 1.

  Retorna:
  float: O valor total (preço * quantidade).
  '''

  return preco * quantidade

total1 = calcular_total(50,3)
total2 = calcular_total(50)
print(f'Total 1: {total1}, Total 2: {total2}')