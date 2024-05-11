from pygame import *

#
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (window_height - 80):
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (window_height - 80):
            self.rect.y += self.speed


#Constants
racket_image = 'racket.png'
ball_image = 'ball.png'
window_width = 700
window_height = 500
window_color = (255, 255, 255)
clock = time.Clock()
FPS = 60

#Window
window = display.set_mode((window_width, window_height))
window.fill(window_color)

#Markers
game = True
finish = False

#Sprites

left_racket = Player(racket_image, 20, 200, 4, 50, 150)
right_racket = Player(racket_image, 520, 200, 4, 50, 150)
ball = GameSprite(ball_image, 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(window_color)
        left_racket.update_left()
        right_racket.update_right()
        left_racket.reset()
        right_racket.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
            
