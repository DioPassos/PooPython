class ContaBanco:
    # Método inicializador (construtor)
    def __init__(self, nome, cpf, endereco, idade):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade
        self.saldo = 0.0  # Iniciar com saldo zero
        self.extrato = []  # Iniciar com um extrato vazio

    # Método para ver o saldo
    def ver_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    # Método para sacar dinheiro
    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente para realizar o saque."
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque de R${valor:.2f}")
            return f"Saque de R${valor:.2f} realizado com sucesso."

    # Método para depositar dinheiro
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito de R${valor:.2f}")
        return f"Depósito de R${valor:.2f} realizado com sucesso."

    # Método para ver o extrato
    def ver_extrato(self):
        extrato_str = "Extrato:\n"
        for transacao in self.extrato:
            extrato_str += transacao + "\n"
        extrato_str += f"Saldo atual: R${self.saldo:.2f}"
        return extrato_str

    # Método especial para representação amigável da instância
    def __str__(self):
        return f"ContaBanco(nome={self.nome}, cpf={self.cpf}, endereco={self.endereco}, idade={self.idade}, saldo=R${self.saldo:.2f})"

class Cadastro(ContaBanco):
    def __init__(self, nome, cpf, endereco, idade):
        super().__init__(nome, cpf, endereco, idade)

    
    def cadastrar(self):
        return f"Cadastro:  nome = {self.nome}  cpf = {self.cpf}, endereço =  rua {self.endereco}, idade= {self.idade} anos"







