# https://www.dtidigital.com.br/blog/como-gerar-graficos-em-python#O-que-e-Matplotlib
num = 7

def isOdd(number):
    if number % 2 == 0:
        return False
    else:
        return True

def math(num):
    numeroMaximo = 0
    while num != 1:
        if isOdd(num) == True:
            num = num * 3 + 1
            if num > numeroMaximo:
                numeroMaximo = num
        else:
            num = num / 2
            if num > numeroMaximo:
                numeroMaximo = num
                
    return numeroMaximo
            
math(num)
print(f"numero max: {math(num)}")