class ContaPoupanca():
    def __init__(self,saldo,numero,titular):
        self.saldo=saldo
        self.numero=numero
        self.titular=titular

    def getSaldo(self):
        return self.saldo

    def getNumero(self):
        return self.numero

    def getTitular(self):
        return self.titular

    def sacar(self,valor):
        if(valor>self.saldo):
            print("Valor maior do que o saldo.")
            return -1
        else:
            self.saldo-=valor
            print(f"Valor do Saque: {valor}")
            print("SAQUE FeitO com Sucesso.")


    def deposito(self,valor):
         if(valor>0):
             self.saldo+=valor
             print("DEPOSITO FeitO com Sucesso.")
             return self.saldo
         else:
            print("Valor invalido para Deposito")
            return -1


