from pygame.locals import *
def dc ():
    import pygame
    
    import sys
    c6=0
    c1=0
    c2=0
    c =0
    c4 =0
    c7 =0
    pygame.init()
    surface = pygame.display.set_mode((800,600))
    black = (0,0,0)
    white = (255,255,255)
    background = pygame.image.load("Backg.JPG")  
    pygame.display.set_caption("SET-CARDS")
    gameIcon = pygame.image.load('ico.jpg')
    pygame.display.set_icon(gameIcon)
    imagerect = background.get_rect() 
    pygame.display.toggle_fullscreen()
    size = ((140,70))
    card1_pink_diamond = pygame.image.load("card 1 Pink diamond.PNG").convert()
    card1_pink_diamond = pygame.transform.scale(card1_pink_diamond, (80,100))
    card1_violet_diamond = pygame.image.load("card 1 violet diamond.PNG").convert()
    card1_violet_diamond = pygame.transform.scale(card1_violet_diamond,(80,100))
    card1_green_diamond = pygame.image.load("card 1 green diamond.PNG").convert()
    card1_green_diamond = pygame.transform.scale(card1_green_diamond, (80,100))
    card1_pink_star = pygame.image.load("card 1 pink star.PNG").convert()
    card1_pink_star = pygame.transform.scale(card1_pink_star,(80,100))
    card2_violet_rect = pygame.image.load("card 2 rect violet.PNG").convert()
    card2_violet_rect = pygame.transform.scale(card2_violet_rect,(80,100))
    card3_violet_rect = pygame.image.load("card 3 rect violet.PNG").convert()
    card3_violet_rect = pygame.transform.scale(card3_violet_rect,(80,100))
    card1_pink_rect = pygame.image.load("card 1 pink rect.PNG").convert()
    card1_pink_rect = pygame.transform.scale(card1_pink_rect,(80,100))
    card2_green_rect = pygame.image.load("card 2 green rect.PNG").convert()
    card2_green_rect = pygame.transform.scale(card2_green_rect,(80,100))
    card1_violet_rect = pygame.image.load("card 1 rect violet.PNG").convert()
    card1_violet_rect = pygame.transform.scale(card1_violet_rect,(80,100))

    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Level 2", True, (250, 80, 37))
    surface.blit(background,(0,0))
    font = pygame.font.SysFont("comicsansms", 25)
    text1 = font.render("Submit", True, (255, 255,255))
    font = pygame.font.SysFont("comicsansms", 34)
    gameover = font.render(" ((GOOD)) ",True,(255,255,255))
    Wrong = font.render("((Try Again))",True,(255,255,255))
    Note = font.render(" Find a Set of Cards And Consecutive Cards",True,(255,255,255))
    
    top = (180,240)
    left = (123,30)
    width = 100
    height = 100
    width1 = 200
    height1 = 100
    width2 = 0
    height2 = 0
    
    card1  = pygame.draw.rect(surface,black,(309,193,width,height))
    card3 = pygame.draw.rect(surface,black,(157,321,width,height))
    card5 = pygame.draw.rect(surface,black,(457,325,width,height))
    card2 = pygame.draw.rect(surface,black,(458,195,width,height))
    card4 = pygame.draw.rect(surface,black,(312,319,width,height))
    card = pygame.draw.rect(surface,black,(140,183,width,height))
    card6 = pygame.draw.rect(surface,black,(163,447,width,height))
    card7 = pygame.draw.rect(surface,black,(309,450,width,height))
    card8 = pygame.draw.rect(surface,black,(460,455,width,height))
    gameover1 = pygame.draw.rect(surface,black,(577,55,width1,height1))
    lev = pygame.draw.rect(surface,black,(8,52,width2,height2))
    
    
#rect = rect.move(40,80)
#def game_loop():
    
    while True:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if pressed1 and b.collidepoint(pos):
                if (c1 == 1 and c6 ==1 and c2 == 1):
                    pass
                    if (c == 1 and c4 == 1 and c7 == 1):
                        
                        import Level3
                    surface.blit(gameover,gameover1)
                else:
                    surface.blit(Wrong,gameover1)
            if card1.collidepoint(pos) and pressed1:
                c1 += 1
                print("Correct")
            if card.collidepoint(pos) and pressed1:
                c +=1
                print("Correct")
            if card2.collidepoint(pos) and pressed1:
                c2 += 1
                print("CORRECT")
            if card6.collidepoint(pos)and pressed1:
                c6 += 1
                print("Correct")
            if card3.collidepoint(pos)and pressed1:
                print("Wrong")
            if card4.collidepoint(pos)and pressed1:
                c4 +=1
                print("Correct")
            if card5.collidepoint(pos)and pressed1:
                print("Wrong")
            if card7.collidepoint(pos)and pressed1:
                print("Correct")
                c7 +=1
            if card8.collidepoint(pos)and pressed1:
                print("Wrong")
        pygame.draw.rect(surface, (193, 154, 107),(632,355,90,60))
        b = pygame.draw.rect(surface, (193, 154, 107),(632,355,90,60))
        surface.blit(card1_pink_diamond,card1)
        surface.blit(card1_green_diamond,card3)
        surface.blit(card1_violet_diamond,card5)
        surface.blit(card1_pink_star,card2)
        surface.blit(card2_violet_rect,card4)
        surface.blit(card3_violet_rect,card)
        surface.blit(card1_pink_rect,card6)
        surface.blit(card1_violet_rect,card7)
        surface.blit(card2_green_rect,card8)
        surface.blit(text,lev)
        surface.blit(text1,b)
        surface.blit(Note,imagerect)
        pygame.display.update()

dc()