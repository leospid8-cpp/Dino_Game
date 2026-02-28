import sys
import pygame 


class dino_game: #classe che serve a gestire risorse e comportamenti del gioco
    
    def __init__(self): #dichiarazzione del metodo costruttore( inizializza e crea le risorse del gioco)

        pygame.init()  #chiamata al metodo costruttore di pygame
        
        self.schermata = pygame.display.set_mode((1200, 800)) #si va a creare un oggeto utilizzando self(This) in qui viene detto la grandezza della schermata

    pygame.display.set_caption("Dino Game") #serve ad impostare il nome della schermata

    def esegui_gioco(self): #dichiarazione della funzione che avvia il ciclo principale
        while(True): #ciclo per l'attesa di eventi 
            for event in pygame.event.get(): #si ripete per ogni evento che avviene in pygame
                if event.type == pygame.quit: #verifica se l'evento rilevato è quello di uscita
                    sys.exit() #chiude tutte le istanze di pygame
            pygame.display.flip() #rende visibile la schemata creata più di recente

if __name__ == "__main__": #funziona come se fosse int main(){} in c++
    dinoGame = dino_game() #creazzione del oggetto 
    dinoGame.esegui_gioco() #esegue il ciclo principale







