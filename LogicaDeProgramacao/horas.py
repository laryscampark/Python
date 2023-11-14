hora = int(input('Informe a hora: '))
    
if 0<= hora < 11:
        print(f'Bom dia são: {hora} horas') 
elif 12 <= hora < 17:
        print(f'Boa tarde são: {hora} horas')
elif 18 <= hora < 23:
        print(f'Boa noite são: {hora} horas')
else:
    print(f'formato de hora inválido: {hora}')