class PegadaHidrica:
    def __init__(self, banho: int, roupa: int, torneira: int):
        self.__banho = banho
        self.__roupa = roupa
        self.__torneira = torneira

    def get_banho(self): return self.__banho
    def set_banho(self, v: int): self.__banho = v

    def get_roupa(self): return self.__roupa
    def set_roupa(self, v: int): self.__roupa = v

    def get_torneira(self): return self.__torneira
    def set_torneira(self, v: int): self.__torneira = v

    def calcular_total(self) -> int:
        banho = self.__banho * 9 * 7
        roupa = self.__roupa * 70
        torneira = self.__torneira * 6 * 7
        return banho + roupa + torneira