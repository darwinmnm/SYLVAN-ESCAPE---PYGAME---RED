import pygame
import sys
from random import randint, choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, x, y):
        super().__init__()

        # Tải hình ảnh cho chướng ngại vật
        if obstacle_type == 'snail':
            self.frames = [pygame.image.load('snail/snail1.png').convert_alpha(),
                           pygame.image.load('snail/snail2.png').convert_alpha()]
            y_pos = 435
        else:
            self.frames = [pygame.image.load(f'Eyebeast/Eye Beast Attack{i}.png').convert_alpha() for i in range(1, 9)]
            y_pos = 210

            # Chiều rộng và chiều cao mong muốn cho eyebeast
            self.width = 90
            self.height = 90

            # Thay đổi kích thước hình ảnh
            for i in range(len(self.frames)):
                self.frames[i] = pygame.transform.scale(self.frames[i], (self.width, self.height))

        # Thiết lập trạng thái hoạt hình ban đầu
        self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

        # Tạo đối tượng rect cho vị trí và phát hiện va chạm
        self.rect = self.image.get_rect(midbottom=(x, y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6

        # Xóa chướng ngại vật khi nó đi ra khỏi phía bên trái màn hình
        if self.rect.right < 0:
            self.kill()
# Khởi tạo Pygame
pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 608

#BACKGROUND
background = pygame.image.load('background/background.png')
floor = pygame.image.load('background/floor.png')

#SCREEN # Thiết lập cửa sổ trò chơi
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SYLVAN ESCAPE')


# Tạo nhóm chướng ngại vật
obstacle_group = pygame.sprite.Group()

# Biến để theo dõi vị trí x của chướng ngại vật trước đó
last_obstacle_x = 800

# Tạo nhóm chướng ngại vật
obstacle_group = pygame.sprite.Group()


i=0
# Thêm nhiều chướng ngại vật vào nhóm
while i<5:
    obstacle_type = choice(['snai', 'eye_beast'])
    
    if obstacle_type == 'snai':
        obstacle = Obstacle('snail', last_obstacle_x + randint(600,800),200)
    else:
        obstacle = Obstacle('eye_beast', last_obstacle_x + randint(600,800), 300)
    i+=1
    obstacle_group.add(obstacle)
    
    # Cập nhật vị trí x của chướng ngại vật trước đó
    last_obstacle_x = obstacle.rect.x

# Vòng lặp trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Cập nhật và vẽ các sprite
    obstacle_group.update()

    # Vẽ background và floor trước
    screen.blit(background, (0, 0))
    screen.blit(floor, (-5, 75))

    # Vẽ các sprite trong nhóm chướng ngại vật
    obstacle_group.draw(screen)
    # Xóa các chướng ngại vật đã ra khỏi màn hình
    for obstacle in obstacle_group.copy():
        if obstacle.rect.x < -obstacle.rect.width:
            obstacle_group.remove(obstacle)


    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt FPS
    pygame.time.Clock().tick(60)

# Kết thúc trò chơi
pygame.quit()
