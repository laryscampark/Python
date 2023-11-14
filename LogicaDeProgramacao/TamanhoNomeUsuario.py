nome = input('Informe o nome do usuário: ')

if len(nome)<= 4:
    print(f'Seu nome é curto: {nome}')
elif len(nome) >5 and len(nome)<=6:
    print(f'Seu nome é normal: {nome}')
else:
    print(f'Seu nome é muito grande: {nome}')