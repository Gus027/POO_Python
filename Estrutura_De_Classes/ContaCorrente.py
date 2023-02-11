from ContaPoupanca import ContaPoupanca

class ContaCorrente(ContaPoupanca):
    def __init__(self,saldo,numero,titular):
        ContaPoupanca.__init__(self,saldo,numero,titular)

    def transferencia(self,valor, contaTrans):
        if(self.getSaldo()>=valor):
            self.sacar(valor)
            contaTrans.deposito(valor)

            return self.saldo
        else:
            print("Transferencia invalida.")
            return -1