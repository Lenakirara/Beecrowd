tempo = int(input())
hora = int(tempo / (60 * 60))
minutos  = int((tempo / 60) - (hora * 60))
segundos = int(tempo - ((hora * 60 * 60) + (minutos * 60)))

print(f'{hora}:{minutos}:{segundos}')
