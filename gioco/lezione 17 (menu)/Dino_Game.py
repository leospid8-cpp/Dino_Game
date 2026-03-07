import random
import sys
import pygame 


from pathlib import Path
from Impostazzioni import Impostazzioni 
from Dinosauro import Dinosauro
from Cactus import Cactus 
from Menu import Menu

class dino_game: 
    
    def __init__(self): 

        pygame.init()  
        self.aggiunta_cactus = 200
        self.secondi = 0
        self.clock = pygame.time.Clock()  
        self.impostazzione = Impostazzioni()
        self.millisecondi_inizio_pausa = 0
        self.millisecondi_totale_pause = 0 
        base_path = Path(__file__).parent
        self.immagineSfondo = pygame.image.load(base_path / "immagini" / "sfondo.jpg")
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)) 
        self.schermata = pygame.display.set_mode(
            (self.impostazzione.schermata_larghezza, self.impostazzione.schermata_altezza)
        ) 

        pygame.display.set_caption("Dino Game") 

        self.dinosauro = Dinosauro(self) 
        self.cactus = [Cactus(self)] 
        self.menu = Menu(self)
        self.mostra_hitbox_test = True  
        self.inpausa = False

    def get_hitbox(self):
        hitbox_dino = self.dinosauro.rettangolo.inflate(-70, -40)  
        hitbox_cactus = [] 
        for c in self.cactus: 
            hitbox = c.rettangolo.inflate(-50, -30)  
            hitbox_cactus.append(hitbox)
        return hitbox_dino, hitbox_cactus

    def esegui_gioco(self): 
        while(True): 
            
            self.controlla_eventi() 
            if not self.inpausa: # se il gioco non in pausa, aggiorna tutto
                self.dinosauro.aggiorna()
                self.aggiorna_cactus() 
            if self.inpausa: # se il gioco in pausa, mostra il menu
                verifica = self.inpausa # salva lo stato di pausa prima di entrare nel menu
                self.inpausa = self.menu.menu(self,self.inpausa) # entra nel menu e aggiorna lo stato di pausa al ritorno
                if verifica != self.inpausa: #se lo stato di inpausa cambia, significa che il menu è stato chiuso e il gioco deve riprendere
                    self.millisecondi_totale_pause += pygame.time.get_ticks() - self.millisecondi_inizio_pausa #calcolca il tempo totale di pausa
            self.aggiorna_schermo() 
            self.clock.tick(60) 



    def timer(self): 
        if self.inpausa: 
            return # se il gioco in pausa, non aggiorna il timer
        millisecondi = pygame.time.get_ticks() - self.millisecondi_totale_pause # sottrae il tempo di pausa al tempo totale
        self.secondi = int(millisecondi / 60) 
        self.rettangolo_timer = pygame.Rect(10, 10, 100, 50) 
        font = pygame.font.SysFont(None, 36) 
        testo_timer = font.render(f"Punteggio: {self.secondi}", True, (255, 255, 255)) 
        x = self.impostazzione.schermata_larghezza - testo_timer.get_width() - 20 
        y = 20 
        self.schermata.blit(testo_timer, (x, y)) 

    

    def controlla_eventi(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:

                    if not self.dinosauro.saltando: 
                        self.dinosauro.saltando = True
                        self.dinosauro.velocita_y = self.dinosauro.forza_salto
                elif event.key == pygame.K_ESCAPE: # mette in pausa
                    self.inpausa = True # cambia lo stato di pausa
                    if self.inpausa:
                        self.millisecondi_inizio_pausa = pygame.time.get_ticks()
                    
                    
                elif event.key == pygame.K_F11: 
                    pygame.display.toggle_fullscreen()

        hitbox_dino, hitbox_cactus = self.get_hitbox()  

        for hitbox in hitbox_cactus: 
            if hitbox_dino.colliderect(hitbox): 
                print("Hai perso!") 
                sys.exit() 

        if self.secondi >= self.aggiunta_cactus: 
            self.cactus.append(Cactus(self)) 
            self.aggiunta_cactus += 200



    
    def aggiorna_schermo(self): 
        self.schermata.blit(self.sfondo, (0, 0))
        self.disegna_cactus() 
        self.dinosauro.disegna()
        self.timer() 
        if self.mostra_hitbox_test:  
            hitbox_dino, hitbox_cactus = self.get_hitbox()
            pygame.draw.rect(self.schermata, (0, 255, 0), hitbox_dino, 2)  
            for hitbox in hitbox_cactus:
                pygame.draw.rect(self.schermata, (255, 0, 0), hitbox, 2)  
        pygame.display.flip()

    def aggiorna_cactus(self):
        for c in self.cactus:
            c.aggiorna(self.secondi)

        
        for c in self.cactus:  
            if c.rettangolo.right < 0:
                cactus_piu_avanti = self.schermata.get_width() 
                gap = random.randint(20, 600)  
                c.rettangolo.left = cactus_piu_avanti + gap 




    def disegna_cactus(self): 
        for c in self.cactus: 
            c.disegna()



if __name__ == "__main__": 
    dinoGame = dino_game() 
    dinoGame.esegui_gioco() 
