class Carro:
    
    def __init__(self, id, marca, modelo, cor, combustivel, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ano = ano


    def __str__(self):
        return f'{self.id}, {self.marca}, {self.modelo}, {self.cor}, {self.combustivel}, {self.ano}'