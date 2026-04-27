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
    score = 0

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

class Ball(GameplaySprite):
    direction_x = 1
    direction_y = 1

    def update(self):
        self.rect.x += self.direction_x * self.speed
        self.rect.y += self.direction_y * self.speed

        if self.rect.bottom > window_height or self.rect.top < 0:
            self.direction_y *= -1

racket1 = Player("racket.png", 50, window_height/2, 25, 200, 10)
racket2 = Player("racket.png", 1030, window_height/2, 25, 200, 10)

ball = Ball("tenis_ball.png", 350, 225, 50,50, 10)
clock = time.Clock()

import time

font.init()
fontstyle = font.SysFont('Arial', 25)
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
        ball.update()
        ball.reset()

        if sprite.collide_rect(ball, racket1 ) or sprite.collide_rect(ball, racket2 ):
            ball.direction_x *= -1

        if ball.rect.x < 0:
            racket2.score += 1
            ball.rect.x = 350
            ball.rect.y = 225

            time.sleep(1)
        
        if ball.rect.right > window_width:
            racket1.score += 1
            ball.rect.x = 350
            ball.rect.y = 225

            time.sleep(1)

        if racket1.score >= 3:
            win_text = fontstyle.render("Left player win", 1, (255,255,255))
            window.blit(win_text, (window_width // 2, window_height // 2))
            is_playing = False

        elif racket2.score >= 3:
            win_text = fontstyle.render("Right player win", 1, (255,255,255))
            window.blit(win_text, (window_width // 2, window_height // 2))
            is_playing = False


        score_text = fontstyle.render(str(racket1.score) + " | " + str(racket2.score), 1, (255,255,255))
        window.blit(score_text,(window_width // 2, 25))



    display.update()
    clock.tick(30)