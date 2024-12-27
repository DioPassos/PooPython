class Carro:
    # Definir o construtor
    def __init__(self, marca, ano, potencia, cor):
        self.marca = marca
        self.ano = ano
        self.potencia = potencia
        self.cor = cor

    def ligar(self):
        return f"O carro {self.marca} está agora ligada."

    def desligar(self):
        return f"A moto {self.marca} do ano {self.ano} está agora desligada."

    def acelerar(self):
        return f"o Carro {self.marca} está acelerando com potência de {self.potencia}."

    def status(self):
        return f"Uma moto da marca {self.marca}, do ano {self.ano}, com potência de {self.potencia}, sendo bem {self.cor}."
    
class Moto(Carro):
    # Redefinir o construtor se precisar de atributos adicionais específicos para Moto
    def __init__(self, marca, ano, potencia, cor):
        super().__init__(marca, ano, potencia, cor)

# Criando instâncias de Carro e Moto
carro01 = Carro('Toyota', 2022, '150 CV', 'azul')
moto1 = Moto('Honda', 2016, '2.0', 'vermelha')

# Chamando métodos da classe e imprimindo os resultados
print(carro01.ligar())
print(moto1.ligar())
print(moto1.acelerar())
print(moto1.desligar())
print(moto1.status())













        