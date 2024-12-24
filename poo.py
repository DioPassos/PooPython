class Pessoa:

    # Método inicializador (construtor)
    def __init__(self,idade,nome,rua,cpf):
        self.idade= idade
        self.nome = nome
        self.rua = rua
        self.cpf = cpf


    def perguntar(self):
        return f"Tudo bem, meu nome é {self.nome} e tenho {self.idade} anos e moro na rua {self.rua} em recife PE"
    
    

    # Criando uma instância de Pessoa
pessoa1 = Pessoa(30,"joão","rua sem nome","123.456")
pessoa2 = Pessoa(20,"Dioeliton","Rua Bartolomeu Marques","04041050413")

# Chamando um método da classe
print(pessoa1.perguntar())
print(pessoa2.perguntar())
# Saída: Olá, meu nome é João e tenho 30 anosp