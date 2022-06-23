idade = int(input())
ano = int(idade / 365)
mes = int(idade % 365) // 30
dia = int(idade % 365 % 30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
