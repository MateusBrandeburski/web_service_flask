
class RegraDeTres:
    
    def __init__(self, A, B, C):
        self.A = float(A)
        self.B = float(B)
        self.C = float(C)
        
    def calcula_equivalencia_regra_de_3(self):
        multiplica_cruzado = self.C * self.B
        resultado = multiplica_cruzado / self.A
        
        return resultado
    

