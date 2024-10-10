
#? função soma
'''
def soma (numero1 , numero2):
    return numero1 + numero2
print (soma(5,7))
'''
'''
idades = [18, 25, 36, 22, 21, 24, 17, 30, 32, 31, 28, 29, 16, 15, 54]
idades_maiores = [] 
def verificar_idades(idades):
    if idades>=18:
         return True

    else:
         return False;
     
idades_maiores=list(filter(verificar_idades,idades))
print(idades_maiores)
'''

#?

nomes = []
saldos = []

def criar_conta(nome, saldo=0):
    nomes.append(nome)
    saldos.append(saldo)

def depositar(indice, valor):
    saldos[indice] = saldos[indice] + valor
    print(f"Depósito de R${valor} realizado com sucesso.")

def sacar(indice, valor):
    if saldos[indice] >= valor:
        saldos[indice] = saldos[indice] - valor
        print(f"Saque de R${valor} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

def consultar_saldo(indice):
    print(f"O saldo da conta de {nomes[indice]} é R${saldos[indice]}.")

def acessar_conta(nome, saldo):
    while True:
        print("\nEscolha uma operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Saldo")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        indice = nomes.index(nome)

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            depositar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 2:
            consultar_saldo(indice)
            valor = float(input("Digite o valor do saque: "))
            sacar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 3:
            consultar_saldo(indice)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

def solicita_nome():
    return input("Digite o nome do titular da conta: ")

def solicita_saldo():
    return float(input("Digite o saldo inicial: "))

while True:
    print("\nEscolha uma operação:")
    print("1 - Criar conta")
    print("2 - Acessar a conta")
    print("3 - Sair")
    resposta = int(input())

    if resposta == 1:
        nome = solicita_nome() 
        saldo = solicita_saldo() 
        criar_conta(nome, saldo)
    elif resposta == 2:
        nome = solicita_nome()  
        if nome in nomes: 
            acessar_conta(nome)
        else:
            print("Conta não encontrada.")
    elif resposta == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
