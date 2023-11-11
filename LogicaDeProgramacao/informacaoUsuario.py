nome = input('Informe seu nome: ')
idade = input('Informe sua idade: ')

if nome and idade: 
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
        
    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é:  {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[-1]}')

else: 
    print('Desculpe você digitou campos vazios')
