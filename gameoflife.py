"""
nariši vzores s stiskom miške
začni simulacijo - space bar
pospeši simulacijo - puščica gor
upočasni simulacijo - puščica dol
"""

def cells_update(screen, cells, size):
    """funkcija za posodabljanje celic - vrne array posodobljenih celic"""
    newcells = numpy.zeros((cells.shape[0], cells.shape[1]))

    for row, col in numpy.ndindex(cells.shape):
        alive = numpy.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        
        if cells[row, col] == 0:
            color = c_dead
        else:
            color = c_alive

        if cells[row, col] == 1:

            if 2 <= alive <= 3:
                newcells[row, col] = 1

        else:
            if alive == 3:
                newcells[row, col] = 1

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return newcells


import numpy
import pygame
import time

pygame.init()
screen_size = 800

#izdelava okenca
pygame.display.set_caption("game of life")
screen = pygame.display.set_mode((screen_size, screen_size))

#celice
cell_size = 32
cells = numpy.zeros((cell_size, cell_size))
size = int(screen_size/cell_size) + 1

#barve celic
c_dead = (0, 0, 0,)
c_background = (70, 70, 70)
c_alive = (255, 255, 255)

sleep = 0.01
sleep_before = sleep
running = False

screen.fill(c_background)
cells_update(screen, cells, size)
pygame.display.flip()
pygame.display.update()

#glavna zanka
while True:
    for Q in pygame.event.get():                      #zapiranje okenca z rdečim križcem
        if Q.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif Q.type == pygame.KEYDOWN:                 #ustavitev in ponoven začetek simulacije
            if Q.key == pygame.K_SPACE:
                running = not running
                cells_update(screen, cells, size)
                pygame.display.update()

            if Q.key == pygame.K_UP:                   #pospešitev simulacije s puščico gor
                if sleep > 0.01:
                    sleep = sleep - 0.01
                elif  0.01 > sleep > 0.002:
                    sleep = sleep - 0.002
                elif 0.003 > sleep > 0.0002:
                    sleep = sleep - 0.0002

            if Q.key == pygame.K_DOWN:                 #upočasnitev simulacije s puščico dol
                if sleep > 0.01:
                    sleep = sleep + 0.01
                else:
                    sleep = sleep + 0.002
        try:
            if pygame.mouse.get_pressed()[0]:                #risanje začetne pozicije živih celic
                pos = pygame.mouse.get_pos()
                cells[pos[1] // size, pos[0] // size] = 1
                cells_update(screen, cells, size)
                pygame.display.update()
                screen.fill(c_background)
        except:
            pass
        

    if running:                                          #potek simulacije
        cells = cells_update(screen, cells, size)
        pygame.display.update()
        time.sleep(sleep)
