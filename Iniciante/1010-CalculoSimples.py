cod01, peca01, valor01 = input().split()
cod02, peca02, valor02 = input().split()
valor = (float(valor01) * int(peca01)) + (float(valor02) * int(peca02))
print (f'VALOR A PAGAR: R$ {valor:.2f}')
