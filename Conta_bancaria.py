

def depositar(saldo,extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
       saldo += valor
       extrato += f"Depósito: R$ {valor:.2f}\n"
       return saldo,extrato

    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(saldo,extrato,limite):
    valor = float(input("Informe o valor do saque: "))

    if (valor > saldo): 
        
        print("Operação falhou! Você não tem saldo suficiente.")

    elif (valor > limite):
        
        print("Operação falhou! O valor do saque excede o limite.")

    elif (numero_saques >= LIMITE_SAQUES):
        print("Operação falhou! Número máximo de saques excedido.")
    
    elif (valor > 0):
        extrato += f"Saque: R$ {valor:.2f}\n"
        
    return saldo,extrato


def gera_extrato(extrato,saldo):
    print(extrato)
    print("\n================ EXTRATO ================")
    print("Sem movimentacoes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar(saldo,extrato)

    elif opcao == "s":
        sacar(saldo,extrato,limite)

    elif opcao == "e":
        gera_extrato(extrato,saldo)
        print(extrato)

    elif opcao == "q":
        break

        print("Operação inválida, por favor selecione novamente a operação desejada.")