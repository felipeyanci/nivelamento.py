#1
'''def soma(a,b):
    return soma()
print(5 + 18)
'''
#2
'''nao sei
'''
#3
'''def maior(a,b):
    return a if a > b else b
print(maior(15 , 6))
'''
#4
'''def par(n):
    return n % 2 == 0
print(par(10))
print(par(7))
'''
#5
'''def media(a, b, c):
    return (a+b+c) / 2
print(f'A media é {media(8,3,5)}')
'''
#6
'''def area_retangulo(l,h):
    return l*h
print(area_retangulo(5,9))
'''
#7
'''def cumprimento(nome):
    return f'Olá, {nome}'
print(cumprimento("felipe"))
'''
#8
'''def dobro(n):
    return n * 2 
print(f'O dobro do numero é {dobro(3)}')
'''
#9
'''def resto_divisao(a,b):
    return a % b
print(resto_divisao(6, 9))
'''
#10
'''def celsius_para_fahrenheit(c):
    return(c * 9/5) + 32
print(celsius_para_fahrenheit(0))
'''
#11
'''import math

def hipotenusa(cat1, cat2):
    return math.hypot(cat1, cat2)
c1 = 9
c2 = 6
hip = hipotenusa(c1, c2)
print(hip)
'''
#12
'''def bissexto(ano):
    return True if (ano % 400 ==0) else False
print(f"1900 é bissexto? {bissexto(1900)}")
'''
#13
'''def fatorial(n):
    if (n == 0) or (n == 1):
        return 1 

    return n * fatorial(n-1)
print(fatorial(0))
'''
#14
'''def contador_vogais(texto):
    vogais = "aeiou"
    result = 0
    for char in texto:
        if char in vogais:
            result = result + 1
    return result

print(contador_vogais("eu sou programador"))
'''
#15
'''def soma_lista(lista):
  return sum(lista)

itens = [1, 3, 5, 7, 9]
resultado = soma_lista(itens)
print(resultado)
'''
#16 
'''nao sei
'''
#17
'''def reverso(texto):
    return texto[::-1]
texto_original = "tatuagem"
texto_invertido = reverso(texto_original)
print(texto_invertido)
'''
#18
'''def imc(peso, altura):
    calc = peso / altura * altura
    return calc

peso = 65
altura = 1.58
meu_imc = imc(peso, altura)
print(meu_imc)
'''
#19
'''def contar_palavras(frase):
    return len (texto)
texto = "Eu quero ser um programador"
numero_de_palavras = contar_palavras(texto)
print(numero_de_palavras)
'''
#20
'''nao sei
'''
