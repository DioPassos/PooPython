class Pessoa:

    # Método inicializador (construtor)
    def __init__(self,idade,nome,rua,cpf):
        self.idade= idade
        self.nome = nome
        self.rua = rua
        self.cpf = cpf


    def perguntar(self):
        return f"Tudo bem, meu nome é {self.nome} e tenho {self.idade} anos e moro na rua {self.rua} em recife PE"


class Cadastro (Pessoa):
    def __init__(self, idade, nome, rua, cpf):
        super().__init__(idade, nome, rua, cpf)

pessoa1 = Pessoa(30,"joão","rua sem nome","123.456")
pessoa2 = Pessoa(20,"Dioeliton","Rua Bartolomeu Marques","04041050413")
cadastro1 = Cadastro(12,"eduardo","rua Ubiratan","040")

    
    

 
# Chamando um método da classe
print(pessoa1.perguntar())
print(pessoa2.perguntar())
print(cadastro1.perguntar())
