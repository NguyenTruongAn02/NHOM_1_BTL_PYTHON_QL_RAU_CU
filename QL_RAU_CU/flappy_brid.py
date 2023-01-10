import pygame, sys, random
#Hàm vẽ bụi cỏ chạy
def draw_floor():
    screen.blit(floor, (floor_x_pos, 550))
    screen.blit(floor, (floor_x_pos + 370, 550))

#Tạo hàm sinh ra ống
def create_pite():
    random_pipe_pos = random.choice(pipe_height)
    bot_pipe = pipe_surface.get_rect(midtop = (400, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(400, random_pipe_pos - 680))
    return bot_pipe, top_pipe

#Hàm chuyển động của chim
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement * 2, 1)
    return new_bird

#Hàm di chuyển ống
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

#Vẽ ống
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)
        if pipe.bottom >= 620:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
#Tao hàm xử lý va chạm
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 550:
            hit_sound.play()
            return False
    return True

#Hiển thị điểm
def score_display(game_sate):
    if game_sate == 'main game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(100, 100))
        screen.blit(score_surface, score_rect)
    if game_sate == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(200, 70))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(200, 210))
        screen.blit(high_score_surface, high_score_rect)

#Hàm cập nhật điểm
def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((370, 620))
clock = pygame.time.Clock()
game_font =pygame.font.Font('04B_19.TTF', 40)

# Tạo biến trọng lực
gravity = 0.25
# Ta biến tốc độ di chuyển của chim
bird_movement = 0
#Biến chạy game
game_active = True
score = 0
high_score = 0


#Tạo hình nền
bg = pygame.image.load('background-night.png')
bg = pygame.transform.scale2x(bg)

#Tạo bụi cỏ
floor = pygame.image.load('floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#Tạo chim
bird = pygame.image.load('yellowbird-downflap.png').convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100, 310))

#Tạo ống
pipe_surface = pygame.image.load('pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

#Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1500)
pipe_height = [300, 200, 250, 270]

#Tạo màn hình kết thúc
game_over_surface = pygame.image.load('message.png').convert_alpha()
game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_rect = game_over_surface.get_rect(center =(185, 310))

#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sfx_hit.wav')
score_sound = pygame.mixer.Sound('sfx_point.wav')
score_sound_countdown = 100


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -6
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 310)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pite())


    screen.blit(bg, (0, 0))

    if game_active:
        # Chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display('main game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    #Sàn cỏ
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -370:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)