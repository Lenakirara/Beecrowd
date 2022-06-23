n = float(input())
n += 0.0001
if n > 0 and n < 1000000.00:
    notas_100 = n // 100
    n = n - (notas_100 * 100)

    notas_50 = n // 50
    n = n - (notas_50 * 50)

    notas_20 = n // 20
    n = n - (notas_20 * 20)

    notas_10 = n // 10
    n = n - (notas_10 * 10)

    notas_5 = n // 5
    n = n - (notas_5 * 5)

    notas_2 = n // 2
    n = n - (notas_2 * 2)

    moedas_1 = n // 1.00
    n = n - (moedas_1 * 1.00)
    
    moedas_050 = n // 0.50
    n = n - (moedas_050 * 0.50)

    moedas_025 = n // 0.25
    n = n - (moedas_025 * 0.25)

    moedas_010 = n // 0.10
    n = n - (moedas_010 * 0.10)

    moedas_005 = n // 0.05
    n = n - (moedas_005 * 0.05)

    moedas_001 = n // 0.01
    n = n - (moedas_001 * 0.01)

print('NOTAS:')
print(f'{notas_100:.0f} nota(s) de R$ 100.00')
print(f'{notas_50:.0f} nota(s) de R$ 50.00')
print(f'{notas_20:.0f} nota(s) de R$ 20.00')
print(f'{notas_10:.0f} nota(s) de R$ 10.00')
print(f'{notas_5:.0f} nota(s) de R$ 5.00')
print(f'{notas_2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moedas_1:.0f} moeda(s) de R$ 1.00')
print(f'{moedas_050:.0f} moeda(s) de R$ 0.50')
print(f'{moedas_025:.0f} moeda(s) de R$ 0.25')
print(f'{moedas_010:.0f} moeda(s) de R$ 0.10')
print(f'{moedas_005:.0f} moeda(s) de R$ 0.05')
print(f'{moedas_001:.0f} moeda(s) de R$ 0.01')
