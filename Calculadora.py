print('*-------Caculadora-------*')
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"A soma de {num1} com {num2} é igual a {resultado}.")
elif operacao == "-":   
    resultado = num1 - num2
    print(f"A subtração de {num1} por {num2} é igual a {resultado}.")
elif operacao == "*":
    resultado = num1 * num2
    print(f"A multiplicação de {num1} por {num2} é igual a {resultado}.")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"A divisão de {num1} por {num2} é igual a {resultado}.")
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."
print('*--------------------------*')