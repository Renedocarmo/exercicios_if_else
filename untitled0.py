# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uxIvrECELtGPAGyOtUMwopd29u-GhhEa
"""

a = input("Digite o primeiro numero ")# a variavel a esta recebendo o valor digitado pelo input do usuario após escrever uma mensagem
b = input("Digite o segundo numero ")# a variavel b esta recebendo o valor digitado pelo input do usuario após escrever uma mensagem
if b > a: #se o valor de b for maior que o valor de a, faça
 print(b) # escrever o valor de b na tela
elif b == a:#senão se b for igual a `a` então
 print("Os numeros são iguais")# escreve na tela uma mensagem "os numeros sao iguais"
else:# senão (negando que b seja maior que a ou que seja igual a 'a')
  print(a)# escrever na tela o valor de a

a = int(input("digite o primeiro numero" ))
if a > 0:
 print("positivo")
elif a==0:
 print("seu numero e 0")
else:
  print("negativo")

a = input("digite uma letra " )
if a == "M" or a == "m":
 print("sexo masculino")
elif a == "F" or a == "f":
 print("sexo feminino")
else:
  print("sexo invalido")

letra = input("digite uma letra" )
if letra  == "a" or letra == "e" or  letra == "i" or letra == "o" or  letra == "u":
 print("e uma vogal ")
else:
 print("nao e uma vogal ")

parcial1 = int(input("insira a primeira nota: "))
parcial2 = int(input("insira a segunda nota: "))
media = (parcial1 + parcial2)/2
if media == 10:
  print("aprovado com distinção")
elif media == 7 or media > 7:
  print("aprovado")
else:
  print("reprovado")

a = int(input("insira o primeiro numero armazenado  "))
b = int(input("insira o segundo numero armazenado   " ))
c = int(input("insira o terceiro numero armazenado 1"))

if  a > b and a > c:
  print(a)
elif b > a and b > c:
  print(b)
else:
  print(c)

a = int(input("digite o primeiro numero "))
b = int(input("digite o segundo numero "))
c = int(input("digite o terceiro numero "))
maior = 0
menor = 0
if a > b and a > c :
  maior = a
elif b > a and b > c:
  maior = b
elif c > a and c < c:

a = int(input("digite o primeiro numero "))
b = int(input("digite o segundo numero "))
c = int(input("digite o terceiro numero "))
if a > b and a > c and c < a and c < b:
  print(a, b, c)
elif a > b and a > c and c < a and b < c:
    print(a, c, b )
elif b > a and b > c and c < a and c < b
    print(b, a, c)
 elif b > a and b > c and b < a and b < c:
      print(b, c, a)
 elif c > a and c > b and a < b and a < c:
      print(c, b, a)
 elif c > a and c > b and b < a and b < c:
      print(c, a, b)

