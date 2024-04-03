#Calculadora Parte 1 - Tópicos
terminar=5
sair=0
soma="1"
sub="2"
multi="3"
dividi="4"
#While 1 - Encerando em caso 0 ou caso não esteja entre as opções
while terminar==5:
    print("----| Menu da Calculadora |----\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir\n 0 - Sair")
    opcao=int(input("Digite sua opção: "))
    if opcao==0:
        print("Encerrando a calculadora...")
        terminar=terminar+1
    elif opcao<0 or opcao>4:
        print(f"Essa opção {opcao} não existe")
        terminar=terminar+1
    elif opcao>0:
        numero1=float(input("Digite seu primeiro número: "))
        numero2=float(input("Digite seu segundo número: "))
#While 2 - Resolvendo as contas e resetando a calculadora
        while opcao>0:
            if opcao==1:
                print(f"{numero1} + {numero2} = {numero1 + numero2}")
                opcao=opcao-1000
            elif opcao==2:
                print(f"{numero1} - {numero2} = {numero1 - numero2}")
                opcao=opcao-1000
            elif opcao==3:
                print(f"{numero1} * {numero2} = {numero1 * numero2}")
                opcao=opcao-1000
            elif opcao==4:
                print(f"{numero1} / {numero2} = {numero1 / numero2}")
                opcao=opcao-1000
