clock = pygame.time.Clock()
frame_count = 1

#PLAYER
# Tạo danh sách chứa các đối tượng màn hình
frames = [pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) for _ in range(frame_count)]

# Tạo lớp để biểu diễn người chơi
class Player:
    def __init__(self, x, y, frame_list):
        self.x = x
        self.y = y
        self.frame_list = frame_list
        self.current_frame = 0

    def draw(self, frame):
        frame.blit(self.frame_list[self.current_frame], (self.x, self.y))

    def update_animation(self):
        self.current_frame += 1
        if self.current_frame >= len(self.frame_list):
            self.current_frame = 0

# Tải hình ảnh cho người chơi
playerrun_frames = [
    pygame.image.load('player/run/run1.png').convert_alpha(),
    pygame.image.load('player/run/run2.png').convert_alpha(),
    pygame.image.load('player/run/run3.png').convert_alpha(),
    pygame.image.load('player/run/run4.png').convert_alpha(),
    pygame.image.load('player/run/run5.png').convert_alpha(),
    pygame.image.load('player/run/run6.png').convert_alpha(),
    pygame.image.load('player/run/run8.png').convert_alpha(),   
]

playerjump_frames = [
    pygame.image.load('player/jump/jump1.png').convert_alpha(),
    pygame.image.load('player/jump/jump2.png').convert_alpha(),
    pygame.image.load('player/jump/jump3.png').convert_alpha(),
    pygame.image.load('player/jump/jump4.png').convert_alpha(),
    pygame.image.load('player/jump/jump5.png').convert_alpha(),
    pygame.image.load('player/jump/jump6.png').convert_alpha(),
    pygame.image.load('player/jump/jump7.png').convert_alpha(),
    pygame.image.load('player/jump/jump8.png').convert_alpha(),
    pygame.image.load('player/jump/jump9.png').convert_alpha(),
    pygame.image.load('player/jump/jump10.png').convert_alpha(),
    pygame.image.load('player/jump/jump11.png').convert_alpha(),

]

# Tạo người chơi và thêm vào danh sách
players = [Player(- 50, 50, playerrun_frames)]

# Vị trí ban đầu của nhân vật
player_x, player_y = 0, 5

# Tốc độ di chuyển và tốc độ nhảy
player_speed = 5
jump_speed = 10
is_jumping = False
jump_count = 10

isGameRunning = True
while isGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
    pygame.display.update()

    # Xử lý logic ở đây cho mỗi frame (player)
    for player in players:
        player.update_animation()

    # Vẽ và xử lý logic cho mỗi frame
    for i, frame in enumerate(frames):
        # Xử lý logic ở đây cho mỗi frame (player)

        # Vẽ người chơi lên màn hình
        players[i].draw(frame)

        # Hiển thị frame lên màn hình
        pygame.display.flip()
        
    # Điều chỉnh độ trễ để giới hạn tốc độ khung hình
    clock.tick(10)
