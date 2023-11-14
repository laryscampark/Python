try:
  n = int(input('Informe um número Inteiro: '))
  
  if n % 2 == 0:
      print(f'esse número: {n} é par')
  else:
      print(f'esse número: {n} é impar')  
except:
    print('Não é um número inteiro')