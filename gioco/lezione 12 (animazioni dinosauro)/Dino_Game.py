import sys
import pygame 
from pathlib import Path

from Impostazzioni import Impostazzioni 
from Dinosauro import Dinosauro
from Cactus import Cactus 

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni()

        base_path = Path(__file__).parent
        self.immagineSfondo = pygame.image.load(base_path / "immagini" / "sfondo.jpg")
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)) 
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) 
        self.cactus = Cactus(self) 
        self.mostra_hitbox_test = True  

    def get_hitbox(self):
        hitbox_dino = self.dinosauro.rettangolo.inflate(-70, -40)  
        hitbox_cactus = self.cactus.rettangolo.inflate(-50, -30)  
        return hitbox_dino, hitbox_cactus

    def esegui_gioco(self): 
        while(True): 

            self.controlla_eventi() 
            self.dinosauro.aggiorna()
            self.cactus.aggiorna() 
            self.aggiorna_schermo() 
            self.clock.tick(60) 

    def controlla_eventi(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:

                    if not self.dinosauro.saltando: 
                        self.dinosauro.saltando = True
                        self.dinosauro.velocita_y = self.dinosauro.forza_salto
                elif event.key == pygame.K_ESCAPE: 
                    sys.exit()
                elif event.key == pygame.K_F11: 
                    pygame.display.toggle_fullscreen()
        hitbox_dino, hitbox_cactus = self.get_hitbox()  
        if hitbox_dino.colliderect(hitbox_cactus): 
            print("Hai perso!") 
            sys.exit() 
    
    def aggiorna_schermo(self): 
        self.schermata.blit(self.sfondo, (0, 0))
        self.dinosauro.disegna()
        self.cactus.disegna() 
        if self.mostra_hitbox_test:  
            hitbox_dino, hitbox_cactus = self.get_hitbox()
            pygame.draw.rect(self.schermata, (0, 255, 0), hitbox_dino, 2)  
            pygame.draw.rect(self.schermata, (255, 0, 0), hitbox_cactus, 2)  
        pygame.display.flip()

if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 







