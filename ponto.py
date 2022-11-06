class Ponto:
    def __init__(self, coordenadas, tipo = None):
        self.coordenadas = coordenadas
        self.tipo = tipo

    
    def __eq__(self, other):
        for coordenada1, coordenada2 in zip(self.coordenadas, other.coordenadas):
            if coordenada1 != coordenada2:
                return False
        return True
        
    def __repr__(self):
        return f'{self.coordenadas} - {self.tipo}'

    @staticmethod
    def distancia(cls, other):
    # distancia = sqrt( (xa - xb)^2 + (ya - yb)^2 + ...) 
        soma = 0
        for cordenada1, cordenada2 in zip(cls.coordenadas, other.coordenadas):
            soma += pow( (cordenada1 - cordenada2) , 2)
        
        return pow(soma, 1/2)