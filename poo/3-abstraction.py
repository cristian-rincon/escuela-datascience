import time



class Lavadora:
    
    def __init__(self):
        pass
    
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        time.sleep(2)
        self._anadir_jabon()
        time.sleep(2)
        self._lavar()
        time.sleep(2)
        self._centrifugar()
        time.sleep(2)
    
    def _llenar_tanque_de_agua(self,temperatura):
        print(f'llenando el tanque con agua {temperatura}.')
    
    def _anadir_jabon(self):
        print('Añadiendo jabón')
        
    def _lavar(self):
        print('Lavando la ropa, por favor espere.')
        
    def _centrifugar(self):
        print('Centrifugando, por favor no apagar la lavadora')

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
