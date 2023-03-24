import os
from palabrasecreta import PalabraSecreta


class Ahorcado:
    
    def __init__(self):
        self.fallos = 0
        self.palabraSecreta = PalabraSecreta.elegirAleatoria()

    
    def __repr__(self) -> str:
        if self.fallos == 0:
            return('''





            ----------
            ''')
        elif self.fallos == 1:
            return('''
                    +
                    |
                    |
                    |
                    |
            ----------
            ''')
        elif self.fallos == 2:
            return('''
                +---+
                    |
                    |
                    |
                    |
            ----------
            ''')
        elif self.fallos == 3:
            return('''
                +---+
                |   |
                    |
                    |
                    |
            ----------
            ''')
        elif self.fallos == 4:
            return('''
                +---+
                |   |
                O   |
                    |
                    |
            ----------
            ''')        
        elif self.fallos == 5:
            return('''
                +---+
                |   |
                O   |
                |   |
                    |
            ----------
            ''')  
        elif self.fallos == 6:
            return('''
                +---+
                |   |
                O   |
               /|\\  |
                    |
            ----------
            ''')  
        elif self.fallos == 7:
            return('''
                +---+
                |   |
                O   |
               /|\\  |
               /    |
            ----------
            ''')  
        elif self.fallos == 8:
            return('''
                +---+
                |   |
                O   |
               /|\\  |
               / \\  |
            ----------
            ''') 
        else:
            return ''
        

    def jugar(self):
        '''
        Dinámica del juego.
        Se pide al usuario que introduzca una letra y se comprueba si dicha letra
        está o no en la palabra secreta. Cada vez que no se acierta una letra, se 
        incrementa el contador de fallos y se representa el ahorcado.
        El juego termina cuando el usuario completa la palabra o acumula 8 fallos.
        '''
        os.system('cls' if os.name == 'nt' else 'clear')

        while (self.fallos < 8) and not self.palabraSecreta.estaCompleta():
            print(self) # Imprime ahorcado
            print(self.palabraSecreta) # Imprime visualización de palabra secreta

            

            try:
                letra = input("Introduce una letra: ")
                if len(letra) != 1:
                    raise Exception("Las letras de una en una, por favor.")
                if not letra.isalpha():
                    raise Exception("Solo se admiten letras.")
                letra = letra.upper()  # Convertimos a mayúscula para que no haya problemas

                os.system('cls' if os.name == 'nt' else 'clear')

                if self.palabraSecreta.adivinarLetra(letra):
                    print("Has adivinado una letra.")
                else:
                    print("Esa letra no está en la palabra.")
                    self.fallos += 1
            except Exception as ex:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(ex)

        if self.palabraSecreta.estaCompleta():
            print(self.palabraSecreta)
            print("Felicidades! Has adivinado la palabra.")
        else:
            print(self)
            print("Lo siento. Otra vez será.")


