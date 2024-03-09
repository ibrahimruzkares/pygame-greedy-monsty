import random
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Greedy monsty")
pygame.display.set_icon(pygame.image.load("bee.png"))
background = pygame.image.load("seabottom.jpg")
pygame.mouse.set_visible(False)

mixer.music.load("ocean.wav")
mixer.music.play(-1)
kill_effect = mixer.Sound("laser.wav")

player1 = pygame.image.load("monsty32.png")
player2 = pygame.image.load("monsty64.png")
player3 = pygame.image.load("monsty128.png")

player1Co = player1.get_rect()
player1Co.topleft = (700,800)
player2Co = player2.get_rect()
player2Co.topleft = (700,800)
player3Co = player3.get_rect()
player3Co.topleft = (700,800)

bait1 = pygame.image.load("fishy16.png")
bait2 = pygame.image.load("steaky32.png")
bait3 = pygame.image.load("chicky64.png")

bait1Co = bait1.get_rect()
bait1Co.topleft = (800, 100)
bait2Co = bait2.get_rect()
bait2Co.topleft = (500, 200)
bait3Co = bait3.get_rect()
bait3Co.topleft = (500, 200)

speed = 1
score_point = 0


score_font = pygame.font.Font("Sunday Mango.ttf", 32)
game_over_font = pygame.font.Font("Sunday Mango.ttf", 72)

def player_main():
    if score_point <= 1:
        screen.blit(player1, player1Co)
    elif score_point >= 2:
        screen.blit(player2, player2Co)
    elif score_point >= 5:
        screen.blit(player3, player3Co)


def bait_main():
    if score_point <= 1:
        screen.blit(bait1, bait1Co)
    elif score_point >= 2:
        screen.blit(bait2, bait2Co)
    elif score_point >= 3:
        screen.blit(bait3, bait3Co)

def score():
    scoree = score_font.render(f"Score: {score_point}", True, (255, 255, 255))
    screen.blit(scoree, (700,50))

def game_over():
    game_over_text = game_over_font.render("Game Over!", True, (255, 255, 255))
    screen.blit(game_over_text,(650,450))


running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT] and player1Co.x > 0:
        player1Co.x -= speed
    if button[pygame.K_RIGHT] and player1Co.x < 1466:
        player1Co.x += speed
    if button[pygame.K_UP] and player1Co.y > 0:
        player1Co.y -= speed
    if button[pygame.K_DOWN] and player1Co.y < 966:
        player1Co.y += speed


    if player1Co.colliderect(bait1Co):
        kill_effect.play()
        score_point += 1
        bait1Co.x = random.randint(100, 1400)
        bait1Co.y = random.randint(100, 900)
        if score_point >= 2 and score_point <= 5:
            bait1 = bait2
            player1 = player2
            player2Co = player1Co
            bait2Co.x = random.randint(100, 1400)
            bait2Co.y = random.randint(100, 900)
    if player1Co.colliderect(bait2Co):
        kill_effect.play()
        score_point += 1
        bait2Co.x = random.randint(100, 1400)
        bait2Co.y = random.randint(100, 900)
        if score_point > 6:
            bait2 = bait3
            player2 = player3
            player3Co = player2Co
            bait3Co.x = random.randint(100, 1400)
            bait3Co.y = random.randint(100, 900)




    screen.blit(background,(0, 0))
    bait_main()
    player_main()
    score()
    pygame.display.update()