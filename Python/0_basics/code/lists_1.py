parts = ['engine']
print(parts)
parts.append('wheel')
parts.append('gear box')
print(parts)
parts[0] = 'door'
print(parts)

a, b = 0, 1
i = 1
while True:
    print(f'{i} > {a}')
    a, b = b, a + b
    i += 1