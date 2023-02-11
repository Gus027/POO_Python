from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from ContaCorrenteComTaxa import ContaCorrenteCashBack


if __name__ == '__main__':

    print("CRIANDO OBJETO CLIENTE PARA CONTA BANCARIA: ")
    print('-'*50)
    saldo = float(input("Insira o seu saldo:" ))
    numeroConta = int(input("Insira o Seu NumeroDaConta: "))
    nome = str(input("Insira o Seu Nome: "))
    Cli = ContaPoupanca(saldo,numeroConta,nome)
    print('-=-' * 50)
    print("\n1 - Para Sacar\n2 - Para Depositar\n3 - Para Transferir")
    var = int(input("O que gostaria de fazer?: "))
    if(var==1):
        Cli.sacar(float(input("Insira o valor do saque: ")))
        print(f"SALDO ATUAL: {Cli.getSaldo():.2f}")
    elif(var==2):
        Cli.deposito(float(input("Insira o valor do deposito: ")))
   ## elif(var==3):
       ## ContaCorrente.transferencia()
    else:
        print("Numero informado Invalido")


