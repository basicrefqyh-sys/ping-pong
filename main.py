from pygame import *
from random import randint

window_width = 1080
window_height = 720
window = display.set_mode((window_width, window_height))

class GameplaySprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(GameplaySprite):
    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < window_height - self.size_y:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        
    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y < window_height - self.size_y:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
racket1 = Player("racket.png", 50, window_height/2, 25, 90, 10)
racket2 = Player("racket.png", 650, window_height/2, 25, 90, 10)

ball = GameplaySprite("tenis_ball.png", 350, 225, 50,50, 10)
clock = time.Clock()

is_running = True
is_playing = True

while is_running:
    for e in event.get():
        if e.type == QUIT:
            is_running = False

    if is_playing:
        window.fill((150,150, 250))
        racket1.reset()
        racket1.update_left()
        racket2.reset()
        racket2.update_right()
        ball.reset()

    display.update()
    clock.tick(30)