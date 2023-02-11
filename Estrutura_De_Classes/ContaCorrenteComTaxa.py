from ContaCorrente import ContaCorrente

class ContaCorrenteCashBack(ContaCorrente):
    def __init__(self,saldo,numero,titular):
        ContaCorrente.__init__(self,saldo,numero,titular)


    def transferencia(self, valor, contaTrans):
        if (self.getSaldo() >= valor):
            taxa = ((valor/100)*5)
            self.sacar(taxa)
            contaTrans.deposito(valor)

            print("TAXA DE 1% PELA TRANSIÇÃO")
            return self.saldo
        else:
            print("Transferencia invalida.")
            return -1
