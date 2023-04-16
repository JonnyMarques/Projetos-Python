#Atividade 03 : Calculadora simples

valor1 = int(input("Informe o primero número: "))
valor2 = int(input("Informe o segundo número: "))
print("-> Soma : +")
print("-> subtração: -")
print("-> Multiplicação: *")
print("-> divisão: /")
operacao = input("Informe a Operação com os sinais a cima: ")
resultado = 0

# fazendo Operação
if (operacao == '+'):
    resultado = valor1 + valor2
elif (operacao == '-'):
    resultado = valor1 - valor2
elif (operacao == '*'):
    resultado = valor1 * valor2
elif (operacao == '/'):
    resultado = valor1 / valor2
else:
    print(":( Houve algum ERRO!!! Reinicie o programa.")

print(valor1, operacao, valor2, '=', resultado)