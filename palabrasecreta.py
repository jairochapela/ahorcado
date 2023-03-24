

import random


class PalabraSecreta:
    '''
    Esta clase representa la palabra que hay que adivinar.
    '''
    
    def __init__(self, palabra):
        '''
        Construye el objeto de palabra secreta con la palabra que se le
        indica como parámetro y se inicializan las letras introducidas
        al conjunto vacío.
        '''
        self.palabra = palabra
        self.letras = set({})

    
    def __repr__(self) -> str:
        '''
        Representación del objeto con la palabra secreta.
        Se mostrará un _ con cada letra aún por adivinar y con la propia
        letra las que ya fueron adivinadas.
        '''
        return ' '.join([c if c in self.letras else '_' for c in self.palabra])
    
    # def __repr__(self) -> str:
    #     '''
    #     Representación del objeto con la palabra secreta.
    #     Se mostrará un _ con cada letra aún por adivinar y con la propia
    #     letra las que ya fueron adivinadas.
    #     '''
    #     t = []
    #     for c in self.palabra:
    #         if c in self.letras:
    #             t.append(c)
    #         else:
    #             t.append('_')
    #     return ' '.join(t)
    

    def adivinarLetra(self, letra) -> bool:
        '''
        Registra cada intento de letra en el conjunto de letras y retorna
        una valor verdadero o falso dependiendo de si la letra indicada como
        parámetro está en la palabra o no.
        '''
        if letra in self.letras:
            raise Exception("Esa letra ya se probó antes")
        self.letras.add(letra)
        return letra in self.palabra
    

    def estaCompleta(self) -> bool:
        '''
        Una palabra está completa si el conjunto de las letras que forman esa
        palabra es un subconjunto del conjunto de las letras introducidas.
        '''
        return set(self.palabra) <= self.letras 
    

    @staticmethod
    def elegirAleatoria():
        '''
        Selecciona una palabra aleatoriamente del fichero de palabras
        y crea un objeto de palabra secreta con ella.
        '''
        with open("words.txt", "r", encoding='UTF-8') as f:
            palabra = random.choice([linea for linea in f])
            return PalabraSecreta(palabra.rstrip())