#Calculadora Parte 1
print("Menu da Calculadora\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir")
opcao=int(input("Digite sua opção: "))
numero1=float(input("Digite seu primeiro número: "))
numero2=float(input("Digite seu segundo número: "))
soma="1"
sub="2"
multi="3"
dividi="4"
#Código da soma
if opcao==1:
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
elif opcao==2:
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
elif opcao==3:
    print(f"{numero1} * {numero2} = {numero1 * numero2}")
elif opcao==4:
    print(f"{numero1} / {numero2} = {numero1 / numero2}")
