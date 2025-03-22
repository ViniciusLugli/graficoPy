# https://www.dtidigital.com.br/blog/como-gerar-graficos-em-python#O-que-e-Matplotlib
import matplotlib.pyplot as plt

num = [3, 5, 7, 10, 2, 40, 15, 24]
numeroMaximo = 0

def isOdd(number):
    return number % 2 != 0  # Retorna True se for ímpar, False se for par

def math(num):
    global numeroMaximo  # Informa que estamos usando a variável global
    numerosGerados = []
    while num != 1:
        if isOdd(num):
            num = num * 3 + 1
            numerosGerados.append(num)
                
        else:
            num = num / 2
            numerosGerados.append(num)
        
        
for i in num: 
    math(i)
    
    

print(f"numero max: {numeroMaximo}")  # Exibe o maior número alcançado
