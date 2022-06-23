a, b, c = map(int, input().split())
maior_numero = (a + b + abs(a - b)) / 2
resultado = (maior_numero + c + abs(maior_numero - c)) / 2
print(f'{resultado:.0f} eh o maior')
