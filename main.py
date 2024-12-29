from poobanco import ContaBanco
from poobanco import Cadastro 

conta = ContaBanco("João Silva", "123.456.789-00", "Rua Sem Nome, 123", 30)
cadastro1= Cadastro("Pedro", "123.456.789", "Rua  123", 40)

# Chamando métodos da classe
print(conta.depositar(1500))
print(conta.ver_saldo())
print(conta.sacar(200))
print(conta.ver_saldo())
print(conta.ver_extrato())
print(conta)
print(cadastro1.cadastrar())


