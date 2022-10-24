class Retangulo:
    def __init__(self, lado_1, lado_2):
        self.lado_1=lado_1
        self.lado_2=lado_2
        #self._area=0
        #self._perimetro=0

    def mudar_lado_1(self, novo_valor):
        self.lado_1=novo_valor
    
    def mudar_lado_2(self, novo_valor):
        self.lado_2=novo_valor

    def area(self):
        self._area = self.lado_1 * self.lado_2

    def perimetro(self):
        self._perimetro = 2*self.lado_1+2*self.lado_2

    def dimensoes(self):
        reta.perimetro()
        reta.area()

        print('As dimensoes do retangulo: {} por {}\nArea do retangulo: {}\nPerimentro do retangulo: {}'.
              format(self.lado_1,self.lado_2,self._area,self._perimetro))

        #print('A area do retangulo: {}*{}={}'.format(self.lado_1, self.lado_2, self.area))
        #print('Perimetro do retangulo: {}'.format(self.perimetro))

class Rodape(Retangulo):




reta=Retangulo(2,5)
reta.dimensoes()

        