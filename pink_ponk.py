from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Pink Ponk')

background = transform.scale(
    image.load('back.jpg'), (700, 500)
)

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_speed, sprite_x, sprite_y, x, y):
        super().__init__()
        self.image = transform.scale(
            image.load(sprite_image), (x, y)
        )
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= -10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 311:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= -5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 311:
            self.rect.y += self.speed  

            
left_ponk = Player('left.png', 5, 5, 150, 80, 200)
right_ponk = Player('right.png', 5, 620, 150, 80, 200)

ball = GameSprite('bal.png', 1, 310, 230, 40, 40)
speed_x = 7
speed_y = 7

font.init()
font1 = font.Font(None, 55)
lose_player1 = font1.render(
    'Player 1 - LOSE', True, (150, 0, 0)
)

lose_player2 = font1.render(
    'Player 2 - LOSE', True, (150, 0, 0)
)


game = True
run = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if run != False:
        window.blit(background, (0, 0))
        left_ponk.reset()
        right_ponk.reset()
        ball.reset()
        

        left_ponk.update_l()
        right_ponk.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(left_ponk, ball) or sprite.collide_rect(right_ponk, ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            window.blit(lose_player1, (220, 250))
            run = False

        if ball.rect.x > 700:
            window.blit(lose_player2, (220, 250))
            run = False

    display.update()
    clock.tick(FPS)
