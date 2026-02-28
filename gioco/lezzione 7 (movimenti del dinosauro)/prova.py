import pygame

# Inizializzazione
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Variabili personaggio
player_x = 180
player_y = 200
player_width = 40
player_height = 40

# Variabili Salto
is_jumping = False
jump_count = 10 # Forza iniziale del salto
velocity = jump_count

run = True
while run:
    screen.fill((0, 0, 0)) # Sfondo nero
    
    # 1. Gestione Eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Rileva pressione tasto singolo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True

    # 2. Logica Salto Graduale
    if is_jumping:
        # Calcola la nuova posizione y (salita + discesa)
        player_y -= (velocity * abs(velocity)) * 0.5
        
        # Simula gravità: riduci la velocità
        velocity -= 1
        
        # Termina il salto quando torna al livello del suolo
        if velocity < -jump_count:
            is_jumping = False
            velocity = jump_count
            player_y = 200 # Riposiziona a terra

    # Disegna il personaggio
    pygame.draw.rect(screen(0, 200, 255)(player_x, player_y, player_width, player_height))
    
    pygame.display.flip()
    clock.tick(60) # 60 FPS per fluidità

pygame.quit()
