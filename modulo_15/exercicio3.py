class Televisao:
    
    def __init__(self):
        self.__status: bool = False
        self.__volume: int = 0
        self.__canal: int = 0

    @property
    def status(self) -> bool:
        return self.__status
    
    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status


    @property
    def volume(self) -> bool:
        return self.__volume
    
    @status.setter
    def volume(self, volume: bool) -> None:
        self.__volume = volume
        
    @property

    def canal(self) -> bool:
        return self.__canal
    
    @status.setter
    def canal(self, canal: bool) -> None:
        self.__canal = canal


    def ligar_desligar(self) -> None:
        self.status = not self.status
        

    def aumentar_volume(self) -> None:
        self.volume = self.volume + 1


    def diminuir_volume(self) -> None:
        self.volume = self.volume - 1


    def aumentar_canal(self) -> None:
        self.canal = self.canal + 1
        

    def diminuir_canal(self) -> None:
        self.volume = self.volume - 1

    def mudar_canal(self, canal: int) -> None:
        self.canal = canal

class ControleRemoto:

    def __init__(self, televisao: Televisao) -> None:
        self.__televisão: Televisao = televisao

    @property
    def televisao(self) -> Televisao:
        return self.__televisão
    

    def ligar_desligar(self) -> None:
        self.televisao.ligar_desligar()

    
    def aumentar_volume(self) -> None:
        self.televisao.diminuir_volume()

    
    def diminuir_volume(self) -> None:
        self.televisao.diminuir_canal()


    def aumentar_canal(self) -> None:
        self.televisao.diminuir_canal()


    def mudar_canal(self, canal: int) -> None:
        self.televisao.mudar_canal(canal) 


if __name__ == '__main__':
    tv: Televisao = Televisao()

    tv.ligar_desligar()

    tv.aumentar_canal()
    tv.aumentar_canal()
    tv.aumentar_canal()

    tv.mudar_canal(42)

    tv.aumentar_volume()
    tv.aumentar_volume()
    tv.aumentar_volume()

    tv.diminuir_canal()
    tv.diminuir_volume()

    tv.ligar_desligar()

    cr: ControleRemoto = ControleRemoto(tv)

    
    cr.ligar_desligar()

    cr.aumentar_canal()
    cr.aumentar_canal()
    cr.aumentar_canal()

    cr.mudar_canal(42)

    cr.aumentar_volume()
    cr.aumentar_volume()
    cr.aumentar_volume()

    cr.diminuir_canal()
    cr.diminuir_volume()

    cr.ligar_desligar()