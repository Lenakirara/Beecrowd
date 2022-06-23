a, b, c = map(float, input().split())
pi = 3.14159
tri = (a * c) / 2
cir = (c ** 2) * pi
trap = ((a + b) / 2) * c 
quad = b ** 2
ret = a * b
print(f'TRIANGULO: {tri:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {trap:.3f}')
print(f'QUADRADO: {quad:.3f}')
print(f'RETANGULO: {ret:.3f}')
