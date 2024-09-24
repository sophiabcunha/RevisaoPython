'''
Título: Revisão de Python
Autor: Sophia
Data: 2024.07.02
'''
# Comentário de linha
# Objetivo: Revisar os Fundamentos  de Programação em Python

print("Hello World")

# Saída --> print ()
print('Profe. Berssa Lindu!') #'string'
print('100 + 100') #'string'
print(100 + 100)  # operação

# Entrada
nome = input('Digite seu nome: ')
print('Você disse:', nome)
valor1 = int(input ('Digite um valor: '))
valor2 = int(input ('Digite outro valor: '))
total = valor1 + valor2
print('Soma dos valores digitados é:', total)

# Variáveis --> espaço de memória que armazena valores temporariamente
# str (string) --> Armazena textos e caracteres
nome = 'soso'
print('A variável nome é do tipo: ', type(nome), ' e tem armazenado o valor: %s'%nome)
# int --> Armazena números inteiros, positivos e negativos
valorX = -81
print('A variável valorX é do tipo: ', type(valorX), ' e tem armazenado o valor: %d' %valorX)
# float --> Armazena números de ponto flutuante positivos e negativos --> NÃO USA , USA . --> 5f == %.2f
pi = 3.14159
print('A variável pi é do tipo: ', type(pi), ' e tem armazenado o valor:%.2f' %pi)
# bool --> Amrmazena True ou False
teste = 10 > 50
print('A variável pi é do tipo: ', type(teste), ' e tem armazenado o valor:', teste)

# Operadores
# Aritméticos --> Calculos +, -, *, //, **, //, %
print(5*5)
print(15/4)  # Resultado float
print(10//3) # Resultado número inteiro
print(10%4) 
# Atribuição
A = 10 # --> = (RECEBE)
A +=1 # __> INCREMENTO SOMA 1
A-= 1 # --> DECREMENTO DIMINUI 1
# Relacionais --> Fazzem comparação e retornam True ou False
A == 10 # == True (igual)
A != 10 # != False (diferente)
# >; <; >=: <=
#Lógicos --> Concatenação de operadores relacionais
# and == e; or ==ou; not == não

# Repetição
# laço for --> Quando eu sei quantas vezes vai repetir
for i in range(11, 102, 10):
  print(i)

palavra = 'Programação'
for letra in palavra:
  print(letra)

#tecla = 1
#while tecla != 0: #__> Repete até a condiçao ser False
  #tecla = int(input('Digite um número: '))
  
# Condição --> if; else; elif
idade = int(input('Digite sua idade: '))
if idade >= 18: #Testa e faz se o resultado True
  print('Pode ir pro Bailão!')
elif idade >= 16: #Faz se o if == False e o elif == True
  print('Vai pro Bailão com a mamãe e o papai!')
else:#Faz se o resultado do if for == a False
  print('Não pode ir pro Bailão! ')

# Funções --> def
def soma(X, Y):
  R = X + Y
  return R

print(soma(10,5))
print(soma(100,50))
A = int(input('Digite um valor: '))
B = int(input('Digite outro valor: '))
print('Soma de %d e %d é igual a %d'%(A, B (soma(A,B))))




