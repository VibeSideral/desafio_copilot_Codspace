number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
choose = input("Digite a operação desejada: - para subtração, + para adição, * para multiplicação e / para divisão: ")

if choose == "+":
    print("A soma dos números é: ", number1 + number2)
elif choose == "-":
    print("A subtração dos números é: ", abs(number1 - number2))
elif choose == "*":
    print("A multiplicação dos números é: ", number1 * number2)
elif choose == "/":
    print("A divisão dos números é: ", number1 / number2)
else:
    print("Operação inválida.")