hora = int(input('Informe a hora: '))
    
if hora >= 0 and hora <= 11:
        print(f'Bom dia são: {hora} horas') 
elif hora >= 12 and hora <= 17:
        print(f'Boa tarde são: {hora} horas')
elif hora >= 18 and hora <= 23:
        print(f'Boa noite são: {hora} horas')
else:
    print(f'formato de hora inválido: {hora}')