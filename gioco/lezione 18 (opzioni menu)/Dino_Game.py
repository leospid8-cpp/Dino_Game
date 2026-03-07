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
        self.millisecondi_inizio_gioco = pygame.time.get_ticks()
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

    def aggiorna_display(self):
        self.schermata = pygame.display.get_surface()
        larghezza, altezza = self.schermata.get_size()
        self.impostazzione.schermata_larghezza = larghezza
        self.impostazzione.schermata_altezza = altezza
        self.sfondo = pygame.transform.scale(self.immagineSfondo, (larghezza, altezza))

        nuovo_rettangolo_schermo = self.schermata.get_rect()
        self.dinosauro.schermata = self.schermata
        self.dinosauro.schermata_rettangolo = nuovo_rettangolo_schermo
        self.dinosauro.posizione_terra = nuovo_rettangolo_schermo.bottom
        if not self.dinosauro.saltando:
            self.dinosauro.rettangolo.bottom = self.dinosauro.posizione_terra

        for c in self.cactus:
            c.schermata = self.schermata
            c.schermata_rettangolo = nuovo_rettangolo_schermo
            c.rettangolo.bottom = nuovo_rettangolo_schermo.bottom

        self.menu.aggiorna_superfici(self)

    def get_hitbox(self):
        hitbox_dino = self.dinosauro.rettangolo.inflate(-70, -40)  
        hitbox_cactus = [] 
        for c in self.cactus: 
            hitbox = c.rettangolo.inflate(-50, -30)  
            hitbox_cactus.append(hitbox)
        return hitbox_dino, hitbox_cactus

    def esegui_gioco(self): 
        while(True): 
            
            restart =self.controlla_eventi() 
            if restart == False:
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
            else: # se restart è True, significa che il giocatore ha scelto di reiniziare, quindi resetta tutto
                self.reset_gioco() 
                



    def timer(self): 
        if self.inpausa: 
            return # se il gioco in pausa, non aggiorna il timer
        millisecondi = (
            pygame.time.get_ticks()
            - self.millisecondi_inizio_gioco
            - self.millisecondi_totale_pause
        )
        self.secondi = max(0, int(millisecondi / 60))
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
                    self.aggiorna_display()

        hitbox_dino, hitbox_cactus = self.get_hitbox()  

        for hitbox in hitbox_cactus: 
            if hitbox_dino.colliderect(hitbox): 
                self.inpausa = True 
                scelta_restart = self.menu.menu_sconfitta(self, self.secondi) 
                # se il menu di sconfitta ritorna True, reinizia il gioco
                if scelta_restart:
                    return True

                

        if self.secondi >= self.aggiunta_cactus: 
            self.cactus.append(Cactus(self)) 
            self.aggiunta_cactus += 200

        return False


    
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

    
    def reset_gioco(self):
        self.dinosauro = Dinosauro(self) 
        self.cactus = [Cactus(self)] 
        self.millisecondi_inizio_gioco = pygame.time.get_ticks()
        self.millisecondi_totale_pause = 0
        self.aggiunta_cactus = 200
        self.secondi = 0
        self.inpausa = False



if __name__ == "__main__": 
    while True:
        dinoGame = dino_game() 
        restart = dinoGame.esegui_gioco()
    
        if restart:
            del dinoGame  # libera le risorse del gioco precedente
            dinoGame = None  # libera le risorse del gioco precedente
            continue  # avvia un nuovo gioco
        break  # esce dal ciclo dopo un solo gioco, rimuovi questa linea se vuoi permettere più giochi consecutivi
        
        
