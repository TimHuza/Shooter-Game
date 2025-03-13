from random import randint
import pygame

pygame.init()

WHITE = (255, 255, 255)
game_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)

WIDTH, HEIGHT = 800, 600
screen_color = (32, 52, 71)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Shooter Game!")

FIGHTER_STEP = 0.8
fighter = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter.get_size()
fighter_x, fighter_y = WIDTH / 2 - fighter_width / 2, HEIGHT - fighter_height
fighter_move_left, fighter_move_right = False, False

BALL_STEP = 0.3
ball = pygame.image.load('images/ball.png')
ball_width, ball_height = ball.get_size()
ball_x, ball_y = 0, 0
ball_fired = False

ALIEN_STEP = 0.1
alien_speed = ALIEN_STEP
alien = pygame.image.load('images/alien.png')
alien_width, alien_height = alien.get_size()
alien_x, alien_y = randint(0, WIDTH - alien_width), 0

run = True

game_score = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_move_left = True
            if event.key == pygame.K_RIGHT and fighter_x <= WIDTH - fighter_width - FIGHTER_STEP:
                fighter_move_right = True
            if event.key == pygame.K_SPACE:
                ball_fired = True
                ball_x = fighter_x + fighter_width / 2 - ball_width / 2
                ball_y = fighter_y - ball_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_move_left = False
            if event.key == pygame.K_RIGHT:
                fighter_move_right = False

    if fighter_move_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_move_right and fighter_x <= WIDTH - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    alien_y += alien_speed

    if ball_fired and ball_y + ball_height < 0:
        ball_fired = False

    if ball_fired:
        ball_y -= BALL_STEP

    screen.fill(screen_color)
    screen.blit(fighter, (fighter_x, fighter_y))
    screen.blit(alien, (alien_x, alien_y))

    if ball_fired:
        screen.blit(ball, (ball_x, ball_y))

    score_text = score_font.render(f"Your score is: {game_score}", True, 'white')
    screen.blit(score_text, (20, 20))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        run = False

    if ball_fired and alien_x < ball_x < alien_x + alien_width - ball_width and alien_y < ball_y < alien_y + alien_height - ball_height:
        ball_fired = False
        alien_x, alien_y = randint(0, WIDTH - alien_width), 0
        alien_speed += ALIEN_STEP / 2
        game_score += 1


game_over_text = game_font.render("Game Over!", True, 'white')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()