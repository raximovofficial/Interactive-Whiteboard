import pygame
from PIL import Image
import numpy as np
from NeuralNetworkUse import UseThisShit
from generator import GiveMeQuestion, Tekshirish
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (200, 0, 0)

W, H = 1850, 1000
BW = 2
screen = pygame.display.set_mode((W, H))
screen.fill(black)

pygame.display.set_caption("Stonetown Interactive")

def DrawCircle(screen, x, y):
    pygame.draw.circle(screen, white, (x, y), BW)

def DrawCorrect(screen, x, y):
    pygame.draw.line(screen, green, (x+10, y+10), (x+40, y+30), 5)
    pygame.draw.line(screen, green, (x+40, y+30), (x+60, y-10), 5)

def DrawWrong(screen, x, y):
    pygame.draw.line(screen, red, (x+10, y+10), (x+40, y+40), 5)
    pygame.draw.line(screen, red, (x+50, y), (x+10, y+40), 5)




quess = []

font = pygame.font.Font('freesansbold.ttf', 32)

def fincount(a):
    if a == 0:
        return 0
    return 1+fincount(a//10)

def QuestionGenerator(rob = 10):
    quess = []
    for i in range(rob):
        str, a = GiveMeQuestion()
        print(a)
        text = font.render(str, True, white, black)
        text_Rect = text.get_rect()
        text_Rect.top = (H - 100) // rob * i + 100
        text_Rect.left = 200
        surfaces = []
        rectangles = []
        for u in range(max(1, fincount(a))):
            surfaces.append(screen.subsurface(200+text_Rect.width + 65*u, (H - 100) // rob * i + 100, 50, 50))
            rectangles.append(pygame.Rect(200+text_Rect.width + 65*u, (H - 100) // rob * i + 100, 50, 50))

        quess.append((text, text_Rect, a, surfaces, rectangles))
    return quess
    
rob = 5
def generate():
    global quess
    quess = QuestionGenerator(rob)
    for k in quess:
        screen.blit(k[0], k[1])
        for t in k[4]:
            pygame.draw.rect(screen, blue, t, 1, 5)


generate()
isPressed = False
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
            for j in quess:
                for s in range(len(j[3])):
                    DrawCircle(j[3][s], x-j[4][s].left, y-j[4][s].top)   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                screen.fill((0, 0, 0))
                generate()
            if event.key == pygame.K_t:
                print(len(quess))
                print("__________")
                for q in quess:
                    
                    ss = ""
                    for sur in q[3]:    
                        data = pygame.image.tobytes(sur, "RGB")
                        ss = ss + Tekshirish(data)
                    ss = int(ss)
                    print(ss)
                    if ss == q[2]:
                        DrawCorrect(screen, q[4][-1].left + q[4][-1].width + 20, q[4][-1].top)
                    else:
                        DrawWrong(screen, q[4][-1].left + q[4][-1].width + 20, q[4][-1].top)
                            
                #screen.fill((0, 0, 0))
                
    pygame.display.flip()
    #pygame.time.Clock().tick(60)