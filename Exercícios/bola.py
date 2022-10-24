class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor=cor
        self.__circunferencia=circunferencia
        self.__material=material

    def trocar_cor(self, nova_cor):
        self.__cor=nova_cor

    def mostrar_cor(self):
        print('A cor da bola: {}'.format(self.__cor))