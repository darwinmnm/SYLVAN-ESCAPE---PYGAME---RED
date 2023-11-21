import pygame
from random import randint, choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, x, y):
        super().__init__()

        # Tải hình ảnh cho chướng ngại vật
        if obstacle_type == 'snail':
            self.frames = [snail1, snail2]
            self.y_pos = 435
        else:
            self.frames = [pygame.transform.scale(image, (90, 90)) for image in eye_beast_images]
            self.y_pos = 210

        # Thiết lập trạng thái hoạt hình ban đầu
        self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

        # Tạo đối tượng rect cho vị trí và phát hiện va chạm
        self.rect = self.image.get_rect(midbottom=(x, self.y_pos))

    def animation_state(self):
        self.animation_index = (self.animation_index + 0.1) % len(self.frames)
        self.image = self.frames[int(self.animation_index)]

    def update(self, speed):
        self.animation_state()
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

# Khởi tạo Pygame
pygame.init()

# Thiết lập cửa sổ trò chơi
screen = pygame.display.set_mode((1080, 608))
pygame.display.set_caption('SYLVAN ESCAPE')

# Tải hình ảnh
background = pygame.image.load('asset/background/background.png')
floor = pygame.image.load('asset/background/floor.png')
snail1 = pygame.image.load('asset/snail/snail1.png').convert_alpha()
snail2 = pygame.image.load('asset/snail/snail2.png').convert_alpha()
eye_beast_images = [pygame.image.load(f'asset/Eyebeast/Eye Beast Attack{i}.png').convert_alpha() for i in range(1, 9)]

# Tạo nhóm chướng ngại vật
obstacle_group = pygame.sprite.Group()

# Biến để theo dõi vị trí x của chướng ngại vật trước đó
last_obstacle_x = 800

# Thêm nhiều chướng ngại vật vào nhóm
for _ in range(5):
    obstacle_type = choice(['snail', 'eye_beast'])
    obstacle = Obstacle(obstacle_type, last_obstacle_x + randint(600,800), 200 if obstacle_type == 'snail' else 300)
    obstacle_group.add(obstacle)
    last_obstacle_x = obstacle.rect.x

# Vòng lặp trò chơi
running = True
speed = 6
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật và vẽ các sprite
    obstacle_group.update(speed)

    # Vẽ background và floor trước
    screen.blit(background, (0, 0))
    screen.blit(floor, (-5, 75))

    # Vẽ các sprite trong nhóm chướng ngại vật
    obstacle_group.draw(screen)

    # Thêm chướng ngại vật mới nếu cần
    if len(obstacle_group) < 5:
        obstacle_type = choice(['snail', 'eye_beast'])
        obstacle = Obstacle(obstacle_type, last_obstacle_x + randint(600,800), 200 if obstacle_type == 'snail' else 300)
        obstacle_group.add(obstacle)
        last_obstacle_x = obstacle.rect.x

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt FPS
    pygame.time.Clock().tick(60)

    # Tăng tốc độ theo thời gian
    speed = min(speed + 0.005, 10)  # Giới hạn tốc độ tối đa là 10

# Kết thúc trò chơi
pygame.quit()