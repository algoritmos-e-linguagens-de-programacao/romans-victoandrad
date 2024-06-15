valores = [
    [1, 'I'], [4, 'IV'], [5, 'V'], [9, 'IX'], [10, 'X'],
    [40, 'XL'], [50, 'L'], [90, 'XC'], [100, 'C'],
    [400, 'CD'], [500, 'D'], [900, 'CM'], [1000, 'M']
]

def int_to_roman(num):
    resultado = ''
    for i in range(len(valores) -1, -1, -1):
        while num >= valores[i][0]:
            resultado += valores[i][1]
            num -= valores[i][0]
    return resultado

print(int_to_roman(1994))

def roman_to_int(s):
    resultado = 0
    for i in range(len(valores) -1, -1, -1):
        while s.startswith(valores[i][1]):
            resultado += valores[i][0]
            s = s[len(valores[i][1]):]
    return resultado

print(roman_to_int('MCMXCIV'))
