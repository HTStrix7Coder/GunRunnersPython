import pygame
import os
pygame.font.init()
pygame.mixer.init()
width,height=928,793
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("THE GUNRUNNERS")
BULLET_VEL=50
POLICE_HIT = pygame.USEREVENT + 1
Bulletdrawn=pygame.transform.scale(pygame.image.load(r"C:\Users\thiru\Documents\Project Barrel\bullet.png"),(20,20))
ROOFTOP=pygame.image.load(r"C:\Users\thiru\Documents\Project Barrel\BackgroundFINAL.png")
VEL=5
JUMP=5
MAX_BULLETS=7
bullets=[]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PLAYER_WIDTH,PLAYER_HEIGHT=90,100
FPS=30
Wastedtext="WASTED"
HEALTH_FONT=pygame.font.SysFont('pricedown bl',40)
WASTED_FONT=pygame.font.SysFont('pricedown bl',70)
BACKROUND = pygame.image.load(r"C:\Users\thiru\Documents\Project Barrel\Background.png")
PLAYER = pygame.transform.scale(pygame.image.load(r"C:\Users\thiru\Documents\Project Barrel\Character.png"),(PLAYER_WIDTH,PLAYER_HEIGHT))
POLICE=pygame.image.load(r"C:\Users\thiru\Documents\Project Barrel\3_police_attack_Attack_005.png")
FOOTSTEPS=pygame.mixer.Sound(r"C:\Users\thiru\Documents\Project Barrel\Sound effects\audiomass-output.mp3")
BULLET_FIRE_SOUND=pygame.mixer.Sound(r"C:\Users\thiru\Documents\Project Barrel\Sound effects\GunShotSnglShotIn PE1097906.mp3")
POLICEROTATED=pygame.transform.scale(POLICE,(PLAYER_WIDTH,PLAYER_HEIGHT))
def draw(player,police,bullets,police_health):
    WIN.blit(ROOFTOP,(0,0))
    WIN.blit(PLAYER,(player.x,player.y))
    WIN.blit(POLICEROTATED,(police.x,police.y))
    Health_display = HEALTH_FONT.render("POLICE HEALTH:" + str(police_health),1,BLACK)
    WIN.blit(Health_display,(width - Health_display.get_width() -20,50))
    for bulletshot in bullets:
        WIN.blit(Bulletdrawn,(bulletshot.x,bulletshot.y))      
    pygame.display.update()
def drawpolicekilled(Wastedtext):
    draw_text=WASTED_FONT.render(Wastedtext,1,WHITE)
    WIN.blit(draw_text,(width/2 - draw_text.get_width()/2,height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def playermovement(keys_pressed,player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:
            player.x-=VEL
            FOOTSTEPS.play()
    if keys_pressed[pygame.K_d] and player.x + VEL + player.width < width:
            player.x+=VEL
            FOOTSTEPS.play()
            
def handlebullets(bullets,player,police):
    for bulletshot in bullets:
        bulletshot.x += BULLET_VEL
        if bulletshot.colliderect(police):
            pygame.event.post(pygame.event.Event(POLICE_HIT))
            bullets.remove(bulletshot)
        elif bulletshot.x > width:
            bullets.remove(bulletshot)

def main():
    player=pygame.Rect(70,625,PLAYER_WIDTH,PLAYER_HEIGHT)
    police=pygame.Rect(700,625,PLAYER_WIDTH,PLAYER_HEIGHT)
    police_health=10
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bullets) < MAX_BULLETS:
                    bulletshot = pygame.Rect(player.x + player.width, player.y + player.height//2 - 35,32,32) 
                    bullets.append(bulletshot)
                    BULLET_FIRE_SOUND.play()
            if event.type == POLICE_HIT:
                police_health-=1
        text = ""
        if police_health<=0:
            text="theif wins"
        if text != "":
            drawpolicekilled(Wastedtext)
            break

        keys_pressed=pygame.key.get_pressed()
        playermovement(keys_pressed,player)
        draw(player,police,bullets,police_health)
        handlebullets(bullets,player,police)
    main()

if __name__=="__main__":
    main()