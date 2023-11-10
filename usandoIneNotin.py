nome = input('Informe seu nome: ')
resultado = input('Informe o que deseja encontrar: ')

if resultado in nome: 
    print(f'{resultado} está em {nome}')
else:
    print(f'{resultado} não está em {nome}')