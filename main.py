import sys
import random
import pygame
from pygame.locals import *

pygame.init()
fps_clock = pygame.time.Clock()

# --- CONFIG ---

def game_settings_one():

    global fps
    global speed
    global speed_min
    global speed_max
    global motion_gap
    global speed_default
    global motion_rotate
    
    fps = 30
    speed = 15
    speed_min = 10
    speed_max = 35
    motion_gap = 30
    speed_default = 15
    motion_rotate = 100

game_settings_one()

def game_settings_two():

    global game_type
    global width
    global height
    global game_mode
    global player_score
    global computer_score
    global screen
    global screen_rect
    global ball_positions
    global ball_position

    game_type = 'EASY'
    width, height = 802, 502
    game_mode = "PLAYER VS COMPUTER"
    player_score, computer_score = 0, 0
    screen = pygame.display.set_mode((width, height))
    screen_rect = screen.get_rect()
    ball_positions = ['top_left', 'top_right', 'bottom_left', 'bottom_right']
    ball_position = random.choice(ball_positions)

game_settings_two()

# --- IMAGES ---

def game_images():

    global bg_image
    global ball_image
    global player_image
    global computer_image
    global top_left_image
    global score_bar_image
    global top_right_image
    global bottom_left_image
    global bottom_right_image
    global score_bar_left_image
    global score_bar_right_image

    bg_image = pygame.image.load('assets/arts/Board.png').convert()
    ball_image = pygame.image.load('assets/arts/Ball.png').convert()
    player_image = pygame.image.load('assets/arts/Player.png').convert()
    top_left_image = pygame.image.load('assets/arts/TopLeft.png').convert()
    computer_image = pygame.image.load('assets/arts/Computer.png').convert()
    top_right_image = pygame.image.load('assets/arts/TopRight.png').convert()
    score_bar_left_image = pygame.image.load('assets/arts/ScoreBar.png').convert()
    bottom_left_image = pygame.image.load('assets/arts/BottomLeft.png').convert()
    bottom_right_image = pygame.image.load('assets/arts/BottomRight.png').convert()

    score_bar_right_image = pygame.transform.flip(score_bar_left_image, True, False)

game_images()

# --- POSITION ---

def update_ball_position(position):

    match (position):

        case "top_left":
            return top_left_image

        case "top_right":
            return top_right_image

        case "bottom_left":
            return bottom_left_image

        case "bottom_right":
            return bottom_right_image

global motion_image
motion_image = update_ball_position(ball_position)

# --- RECT ---

def game_rects():

    global ball_rect
    global motion_rect
    global player_rect
    global computer_rect
    global score_bar_right_rect
    
    ball_rect = ball_image.get_rect()
    motion_rect = motion_image.get_rect()
    player_rect = player_image.get_rect()
    computer_rect = computer_image.get_rect()
    score_bar_right_rect = score_bar_right_image.get_rect()

game_rects()

# --- POSITION ---

def game_positions():

    global ball_y
    global ball_x
    
    ball_x,ball_y = screen_rect.center
    player_rect.y = screen_rect.centery
    score_bar_right_rect.right = screen_rect.right
    player_rect.x = screen_rect.left + player_rect.w
    ball_rect.x, ball_rect.y = ball_x, ball_y,
    computer_rect.x, computer_rect.y = screen_rect.right - computer_rect.w * 2, screen_rect.centery

game_positions()

# --- GAME-FONTS ---

def game_fonts():

    global font
    font = pygame.font.SysFont('assets/fonts/Teko-VariableFont_wght.ttf', 40)

game_fonts()

# --- GAME-TYPE ---

def game_type_font():

    global game_type_text
    global game_type_text_rect

    game_type_text = font.render(f'TYPE: {game_type}', True, 'Black')
    game_type_text_rect = game_type_text.get_rect()
    game_type_text_rect.x = screen_rect.centerx + game_type_text_rect.w
    game_type_text_rect.y = 10

game_type_font()

# --- GAME-SCORE ---

def game_score_text():

    global score_text
    global score_text_rect

    score_text = font.render(f'{player_score} VS {computer_score}', True, 'White')
    score_text_rect = score_text.get_rect()
    score_text_rect.centerx = screen_rect.centerx
    score_text_rect.y = 10

game_score_text()

# --- GAME-MODE ---

def game_mode_font():

    global game_mode_text
    global game_mode_text_rect

    game_mode_text = font.render(game_mode, True, 'White')
    game_mode_text_rect = game_mode_text.get_rect()
    game_mode_text_rect.y = screen_rect.bottom - game_mode_text_rect.h - 20
    game_mode_text_rect.centerx = screen_rect.centerx

game_mode_font()

# --- GAME-SPEED ---

def game_speed_text():
    
    global speed_text
    global speed_text_rect

    speed_text = font.render(f'SPEED: {speed}', True, 'Black')
    speed_text_rect = speed_text.get_rect()
    speed_text_rect.y = 10
    speed_text_rect.centerx = screen_rect.centerx / 3

game_speed_text()

# --- SCORE ---

def update_score(player, type):
    
    global player_score, computer_score, score_text

    if player == 'player':

        if type == 'inc': player_score += 1
        elif type == 'dec': player_score -= 1
        elif type == 'def': player_score = 0

    if player == 'computer':

        if type == 'inc': computer_score += 1
        elif type == 'dec': computer_score -= 1
        elif type == 'def': computer_score = 0

    score_text = font.render(f'{player_score} VS {computer_score}', True, 'White')

# --- PLAYER ---

def update_player(direction):

    global player_rect

    if direction == 'up':
        if player_rect.y >= 75:
            player_rect.y -= speed

    elif direction == 'down':
        if player_rect.y <= (height - player_rect.h):
            player_rect.y += speed

# --- COMPUTER ---

def update_computer(direction):

    global computer_rect

    if direction == 'up':
        if computer_rect.y >= 75:
            computer_rect.y -= speed

    elif direction == 'down':
        if computer_rect.y <= (height - computer_rect.h):
            computer_rect.y += speed

def update_speed(type):
    
    global speed, speed_text

    if type == 'dec':
        if speed > speed_min: speed -= 1
    
    elif type == 'inc':
        if speed < speed_max: speed += 1
    
    elif type == 'def':
        speed = speed_default
    
    elif type == 'min':
        speed = speed_min

    speed_text = font.render(f'SPEED: {speed}', True, 'Black')

# --- TYPE ---

def update_type(type):

    global game_type, game_type_text
    game_type = type
    game_type_text = font.render(f'TYPE: {game_type}', True, 'Black')

# --- MODE ---

def update_mode(mode):

    global game_mode, game_mode_text
    game_mode = mode
    game_mode_text = font.render(f'{game_mode}', True, 'White')

# --- WINNER ---

def check_winner():
    
    global ball_position, motion_image, player_score, computer_score

    if ball_rect.y >= height:

        if ball_position == "bottom_left":
            ball_position = "top_left"
            motion_image = top_left_image

        elif ball_position == "bottom_right":
            ball_position = "top_right"
            motion_image = top_right_image

    elif ball_rect.y <= 75:

        if ball_position == "top_left":
            ball_position = "bottom_left"
            motion_image = bottom_left_image

        elif ball_position == "top_right":
            ball_position = "bottom_right"
            motion_image = bottom_right_image

    if ball_rect.x <= 0:
        update_score('computer', 'inc')
        ball_rect.x, ball_rect.y = ball_x, ball_y
        ball_position = random.choice(ball_positions)
        motion_image = update_ball_position(ball_position)
    
    elif ball_rect.x >= width:
        update_score('player', 'inc')
        ball_rect.x, ball_rect.y = ball_x, ball_y
        ball_position = random.choice(ball_positions)
        motion_image = update_ball_position(ball_position)

# --- COLLISION ---

def check_collision():

    global ball_position, motion_image

    if ball_rect.colliderect(player_rect):

        if game_type == 'HARD':

            if speed < speed_max: update_speed('inc')
            else:
                update_speed('min')

        ball_position = random.choice(['top_right', 'bottom_right'])
        motion_image = update_ball_position(ball_position)

    elif ball_rect.colliderect(computer_rect):

        if game_type == 'HARD':

            if speed < speed_max: update_speed('inc')
            else:
                update_speed('min')

        ball_position = random.choice(['top_left', 'bottom_left'])
        motion_image = update_ball_position(ball_position)

# --- COMPUTER ---

def automate_computer():

    if game_mode == "PLAYER VS COMPUTER" or game_mode == "COMPUTER VS COMPUTER":

        if ball_position == "top_right":
            if computer_rect.y >= 75:
                computer_rect.y -= speed

        elif ball_position == "bottom_right":
            if computer_rect.y <= (height - computer_rect.h):
                computer_rect.y += speed

def automate_player():

    if game_mode == "COMPUTER VS COMPUTER":

        if ball_position == "top_left":
            if player_rect.y >= 75:
                player_rect.y -= speed

        elif ball_position == "bottom_left":
            if player_rect.y <= (height - computer_rect.h):
                player_rect.y += speed

def update_position():

    if ball_position == "top_right":
        ball_rect.x += speed
        ball_rect.y -= speed
        motion_rect.x = ball_rect.x - motion_gap
        motion_rect.y = ball_rect.y + motion_gap - 15

    elif ball_position == "bottom_left":
        ball_rect.x -= speed
        ball_rect.y += speed
        motion_rect.x = ball_rect.x + motion_gap - 5
        motion_rect.y = ball_rect.y - motion_gap - 15 + 5

    elif ball_position == "top_left":
        ball_rect.x -= speed
        ball_rect.y -= speed
        motion_rect.x = ball_rect.x + motion_gap - 5
        motion_rect.y = ball_rect.y + motion_gap - 5

    elif ball_position == "bottom_right":
        ball_rect.x += speed
        ball_rect.y += speed
        motion_rect.x = ball_rect.x - motion_gap
        motion_rect.y = ball_rect.y - motion_gap

# --- KEYS ---

def game_keysa():

    print(
        "\n"
        "(=) \t\t increase game speed\n"
        "(-) \t\t decrease game speed\n"
        "(s) \t\t reset game speed\n"
        "(r) \t\t reset game scores\n"
        "(e) \t\t switch to easy mode\n"
        "(h) \t\t switch to hard mode\n"
    )

game_keysa()

# --- KEYSB ---

def game_keysb():

    print(
        "(pgdown) \t move player2 up\n"
        "(pgup) \t\t move player2 up\n"
        "(p) \t\t player vs computer\n"
        "(up) \t\t move player up\n"
        "(down) \t\t move player down\n"
        "(2) \t\t player1 vs player2\n"
        "(c) \t\t computer vs computer\n"
    )

game_keysb()

# --- LOOP ---

mouse = pygame.mouse.get_rel()

while True:

    # --- FILL ---

    screen.fill("Black")
    
    # --- EVENT ---

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # --- KEYS-A ---

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        update_player('up')

    elif keys[pygame.K_DOWN]:
        update_player('down')

    elif keys[pygame.K_PAGEUP]:
        update_computer('up')

    elif keys[pygame.K_PAGEDOWN]:
        update_computer('down')

    elif keys[pygame.K_r]:
        update_score('player', 'def')
        update_score('computer', 'def')
        
    # --- KEYS-B ---

    elif keys[pygame.K_MINUS]:
        update_speed('dec')

    elif keys[pygame.K_EQUALS]:
        update_speed('inc')

    elif keys[pygame.K_s]:
        update_speed('def')

    elif keys[pygame.K_e]:
        update_type('EASY')

    elif keys[pygame.K_h]:
        update_type('HARD')

    # --- KEYS-C ---
    
    elif keys[pygame.K_p]:
        update_mode("PLAYER VS COMPUTER")

    elif keys[pygame.K_c]:
        update_mode("COMPUTER VS COMPUTER")

    elif keys[pygame.K_2]:
        update_mode("PLAYER VS PLAYER")

    # --- MOUSE ---

    if pygame.mouse.get_rel() != mouse:
        player_rect.y = pygame.mouse.get_pos()[1]
        mouse = pygame.mouse.get_rel()

    # --- FUNCTIONS ---

    update_position()
    check_winner()
    check_collision()
    automate_computer()
    automate_player()

    # --- DRAW ---

    screen.blit(bg_image, (0, 47))
    screen.blit(score_bar_left_image, (0, 0))
    screen.blit(score_bar_right_image, score_bar_right_rect)
    screen.blit(motion_image, motion_rect)
    screen.blit(ball_image, ball_rect)
    screen.blit(player_image, player_rect)
    screen.blit(computer_image, computer_rect)
    screen.blit(speed_text, speed_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(game_mode_text, game_mode_text_rect)
    screen.blit(game_type_text, game_type_text_rect)
    pygame.display.flip()
    fps_clock.tick(fps)
