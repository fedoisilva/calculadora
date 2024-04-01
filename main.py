def somar(n1, n2):
  return n1 + n2

def subtrair(n1, n2):
  return n1 - n2

def multiplicar(n1, n2):
  return n1 * n2

def dividir(n1, n2):
  return n1 / n2

def dividir_inteiro(n1, n2):
  return n1 // n2

def resto_divisao(n1, n2):
  return n1 % n2

def exponenciacao(n1, n2):
  return n1 ** n2

def raiz_quadrada(n1):
  return n1 ** 0.5

print('''
   _____          _      _____ _    _ _               _____   ____  _____                    
  / ____|   /\   | |    / ____| |  | | |        /\   |  __ \ / __ \|  __ \     /\        _   
 | |       /  \  | |   | |    | |  | | |       /  \  | |  | | |  | | |__) |   /  \     _| |_ 
 | |      / /\ \ | |   | |    | |  | | |      / /\ \ | |  | | |  | |  _  /   / /\ \   |_   _|
 | |____ / ____ \| |___| |____| |__| | |____ / ____ \| |__| | |__| | | \ \  / ____ \    |_|  
  \_____/_/    \_\______\_____|\____/|______/_/    \_\_____/ \____/|_|  \_\/_/    \_\    

  1. SOMAR
  2. SUBTRAIR
  3. MULTIPLICAR
  4. DIVIDIR
  5. DIVIDIR INTEIRO
  6. RESTO DA DIVISÃO
  7. EXPONENCIAÇÃO
  8. RAIZ QUADRADA

''')

operacao = int(input('Selecione o número da operação a ser realizada: '))

if operacao == 8:
  n1 = float(input('\nDigite o número: '))
  print(f'\nA raiz quadrada de {n1} é igual a {raiz_quadrada(n1)}')

else:
  n1 = float(input('\nDigite o primeiro número: '))
  n2 = float(input('\nDigite o segundo número: '))
  
  if operacao == 1:
    print(f'\nA soma de {n1} e {n2} é igual a {somar(n1, n2)}')
  
  elif operacao == 2:
    print(f'\nA subtração de {n1} e {n2} é igual a {subtrair(n1, n2)}')
  
  elif operacao == 3:
    print(f'\nA multiplicação de {n1} e {n2} é igual a {multiplicar(n1, n2)}')
  
  elif operacao == 4:
    print(f'\nA divisão de {n1} e {n2} é igual a {dividir(n1, n2)}')
  
  elif operacao == 5:
    print(f'\nA divisão inteira de {n1} e {n2} é igual a {dividir_inteiro(n1, n2)}')
  
  elif operacao == 6:
    print(f'\nO resto da divisão de {n1} e {n2} é igual a {resto_divisao(n1, n2)}')
  
  elif operacao == 7:
    print(f'\nO número {n1} elevado a base {n2} é igual a {exponenciacao(n1, n2)}') 
  
  else:
    print('\nOperação inválida.')

  
  

