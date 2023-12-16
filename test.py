import pygame
from PIL import Image
import numpy as np
from NeuralNetworkUse import UseThisShit

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
BRUSH = (250, 250, 250)
W, H = 1850, 1000
screen = pygame.display.set_mode((W, H))
screen.fill((0, 0, 0))
pygame.display.set_caption("Stonetown Interactive")

def DrawCircle(screen, x, y):
    pygame.draw.circle(screen, BRUSH, (x, y), 15)



font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, white, blue)
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)

isPressed = False
screen.blit(text, textRect)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed:       
            x, y = pygame.mouse.get_pos()
            DrawCircle(screen, x, y)   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                data = pygame.image.tobytes(screen.subsurface(0, 0, 500, 500), "RGB")
                img = Image.frombytes('RGB', (500, 500), data)
                img.show()
                img = img.resize((28, 28))
                img = img.convert('L')
                arr = np.array(img).reshape(784)

                print(UseThisShit(arr))
                screen.fill((0, 0, 0))
                
    pygame.display.flip()
    #pygame.time.Clock().tick(60)