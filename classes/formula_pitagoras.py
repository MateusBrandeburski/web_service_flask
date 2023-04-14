
# essa classe é usada tanto na rota "calculadora_grafica" quando na rota "calculadora_query" por isso algumas verificações precisam ser feitas de maneira diferentes.
class TeoremaDePitagoras():
    
    def __init__(self,  catetoA=0, catetoO=0, hipotenusa=0):  
        """Explicação dessa conversão
        Essas converções e condições são necessárias porque na rota são decalarados 3 tipos de query paramns, e quando um desses parametros não é passado, ele retorna um item None (e um item None não pode ser multiplicado, o que faz com que esse item caia no tratamento de erro). Então "float(catetoO) if catetoO is not None else 0" é a condição que faz com que, caso seja None, ele vire 0.
        
        Acima, em self, precisa ser passado como (catetoA=0, catetoO=0, hipotenusa=0) para que não precise sempre declarar todos sempre que for usar a classe, por exemplo: teorema=TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO).
        
        O if ternário trata tanto None quando uma string vázia (""), porque em query, se não for passado nada é None, mas em um input html, se não for passado nada é "".
        
        Receber o valor 0 (zero)  dá certo porque a fórmula começa somando = cO²+cA² = h²
        Se começasse multiplicando, ele teria que receber como valor 1 (um)
        """
        self.__catetoO= float(catetoO) if catetoO is not "" and catetoO is not None else 0
        self.__catetoA = float(catetoA) if catetoA is not "" and catetoA is not None else 0
        self.__hipotenusa = float(hipotenusa) if hipotenusa is not "" is not None else 0
        
    def calcular_catetos(self):
        """Como funcinona a formula matemática dessa função:
        O Teorema de Pitágoras diz que é possível calcular qualquer um dos lados de um triângilo retângulo se soubermos o valor de 2 lados. 
        
        Os nomes dos 3 lados são: Cateto Oposto, Cateto Adjacente, Hipotenusa.
        
        cA² + cO² = h²
        
        Sendo assim, não importa a ordem dos catetos, a formula dará o mesmo valor.
        As variáveis foram contruídas como se tivesse sido calculado "na mão", primiero um lado, depois passa para o outro lado da equação seguindo as regras matemáticas...   
        """ 
        quadrado_do_cateto = self.__catetoA ** 2 or self.__catetoO ** 2
        quadrado_da_hipotenusa = self.__hipotenusa**2    
        passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
        cateto_final = passa_subtraindo ** (1/2) # ou 0,5  
        """Explicação dessa condicinal
        Se a hipotenusa tiver o mesmo valor de um cateto, isso siguinifica que ele não é um triângulo retângulo. Logo, o cálculo é impossível e não se aplica. Porque o resultado será sempre 0 (zero)
        """   
        if cateto_final == 0.0:
            return "Cálculo Impossível. Lembre-se que a hipotenusa é o maior lado."
        else:
            return f"Cateto = {round(cateto_final, 2)}"
      
    def calcular_hipotenusa(self):    
        quadrado_da_hipotenusa = self.__catetoO**2 + self.__catetoA**2
        hipotenusa = quadrado_da_hipotenusa ** (1/2)
        return f"Hipotenusa = {round(hipotenusa, 2)}"
        
    @staticmethod
    def strings_teorema(name):       
        if "hipotenusa" in name:
            return name
        elif "cateto" in name:
            return name 
        elif "falta_parametros" in name:
            name = "Dois campus devem ser preenchidos para calcular."
            return name
        elif "TypeError" in name:
            name = "Cálculo Impossível. Resultado Nº negativo."
            return name



