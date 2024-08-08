def soma(x , y):
    return x + y

def subtracao(x , y):
    return x - y 

def multi(x , y):
    return x * y

def divisao(x , y):
    if y != 0 :
        return x / y
    else:
        return "Não é possível dividir por zero"

def calculadora():
    print("Escolha uma operação : ")
    print("1 Soma")
    print("2 Subtração")
    print("3 Multiplicação")
    print("4 Divisão")

    escolha = input("Escolha um numero relacionado a operação que deseja : ")

    if escolha in ("1" ,"2" , "3" , "4") :
        num1 = float(input("Digite o primeiro número"))
        num2 = float(input("Digite o segundo número"))

    if escolha == "1":
        print("Resultado e", soma(num1 ,num2))
    elif escolha == "2":
        print("resultado é", subtracao(num1 ,num2))
    elif escolha == "3":
        print("Resultado é " , multi(num1 ,num2))
    elif escolha == "4" :
        print("Resultado é ", divisao(num1 ,num2))

while True:
    calculadora()
    continuar = input("Deseja continuar S/N ")
    if continuar.lower() != "s":
        print("calculadora encerrada")
        break

