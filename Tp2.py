# # 1
# idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}

# maiores_de_idade = {nome: idade for nome, idade in idades.items() if idade >= 18}

# print(maiores_de_idade)

# # 2
# tupla1 = (1,3,5)
# tupla2 = (5,1,3)

# if set(tupla1) == set(tupla2):
#   print('As tupla possuem SIM os mesmos elementos.')
# else: 
#   print('As tuplas NÃO possuem os mesmos elementos')

# # 3
# lista = [4, 1, 5, 2, 3, 2, 4, 4]

# frequencia = {}

# for i in lista:
#   if i in frequencia:
#     frequencia[i] += 1
#   else:
#     frequencia[i] = 1

# frequencia_crescente = dict(sorted(frequencia.items()))
# print(frequencia_crescente)

# # 4
# dic1 = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32,'g':64}
# dic2 = {'c':4,'e':16,'g':64}

# conjunto1 = set(dic1.items())
# conjunto2 = set (dic2.items())

# if conjunto1 <= conjunto2:
#   print("Dicionário 1 é um subconjunto de dicionário 2.")
# else:
#   print('Dicionário 1 não é um subconjunto de dicionário 2.')

# if conjunto2 <= conjunto1:
#   print('Dicionário 2 é um subconjunto de dicionário 1.')
# else:
#   print('Dicionário 2 não é um subconjunto de dicionário 1.')

# #5
# alunos = {
#   'Ana': [8.5, 7.0, 9.0],
#   'Pedro': [6.0, 5.5, 6.5],
#   'Maria': [7.5, 8.0, 7.0],
#   'José': [5.5, 6.0, 6.5]
# }

# print(alunos)

# def calcular_media(alunos):
#   '''Função com a finalidade de calcular a média dos alunos e retornar se cada um deles foram aprovados ou reprovados'''
#   aluno, lista_notas = alunos
#   media = sum(lista_notas) / len(lista_notas)
#   return(aluno, "Aprovado" if media >= 7 else "Reprovado")

# resultado = map(calcular_media, alunos.items())

# classificacao = {"Aprovado": [], "Reprovado": []}
# for aluno, status in resultado:
#   classificacao[status].append(aluno)

# print(classificacao)

# # 6
# lista = [1,2,1,4,5,6,7]

# menor_soma = float('inf')
# pares = (None, None)

# for i in range(len(lista)):
#   for u in range(len(lista)):
#     if u != i:
#       soma = lista[i] + lista[u]
#       if abs(soma) < abs(menor_soma):
#         menor_soma = soma
#         pares = (lista[i], lista[u])

# print(f'Os dois números cuja soma é mais próxima de zero são {pares[0]} e {pares[1]}, com soma {menor_soma}')

# # 7
# alunos = {}

# while True:
#   aluno = input('Informe o nome do aluno (ou digite "fim" para terminar): ')
#   if aluno.lower() == 'fim':
#     break
#   elif aluno == '':
#     print('Por favor, insira um nome válido')
#   else:
#     notas = []
#     while True:
#       try:
#         nota = input('Informe uma nota do aluno (ou digite "fim" para terminar): ')
#         if nota.lower() == 'fim':
#           break
#         elif nota == '':
#           print('Por favor, insira um valor')
#         else: 
#           notas.append(float(nota))
#       except ValueError:
#         print( 'Por favor, insira um número válido para a nota.')
    
#     alunos[aluno] = notas
#     print(f'Aluno {aluno} e suas notas {notas} foram adicionados.')

# print('Todos os alunos e suas notas: ')
# for aluno, notas in alunos.items():
#   print(f'{aluno}: {notas}')

# # 8
# import random

# numero_magico = random.randint(1,20)
# tentativas = 4

# print("Você tem 4 tentativas para acertar, o número pode ser um valor de 1 a 20.")

# for tentativa in range(tentativas):
#   palpite = int(input(f'Tentativa {tentativa+1}: Qual é o seu palpite? '))

#   if palpite == numero_magico:
#     print("Parabéns, você acertou!")
#     break
#   elif palpite < numero_magico:
#     print("O número secreto é maior.")
#   else:
#     print('O número secreto é menor.')
  
#   if tentativa == range(tentativas):
#     print(f'Você não acertou! O número secreto era {numero_magico}')

# # 9
# def checar_palindromo(entrada):
#   '''Essa função tem como objetivo checar se a palavra ou frase fornecida é um palíndromo (a mesma frase/palavra ao contrário)'''
#   frase = entrada.replace(' ','').lower()

#   if frase == frase[::-1]:
#     return True
#   else:
#     return False

# entrada = input('Digite uma palavra ou frase para checar se é um palíndromo: ')

# if checar_palindromo(entrada):
#   print('É um palíndromo!')
# else:
#   print('Não é um palíndromo')

# 10