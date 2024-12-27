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
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed        


game = True
run = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if run != False:
        window.blit(background, (0, 0))

    display.update()
    clock.tick(FPS)