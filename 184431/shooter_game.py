from pygame import *
import random 
font.init()
window = display.set_mode((900,900))
display.set_caption("Anime girl bombing Шидов Дмитрий")
background = transform.scale(image.load("s.png"),(900,900))
debily = sprite.Group()
abeme = sprite.Group()
x1 = 200
x2 = 300
y1 = 200
y2 = 300
clock = time.Clock()
FPS = 60
loozeer = 0
killeeer = 0
n = 0
fontdlyalohov = font.Font(None,50)
texttyloh = fontdlyalohov.render("ааа пропущенааекеппппв:" + str(loozeer),1,(225,200,50))
texttynormchel = fontdlyalohov.render("убита лохов тупих:" + str(killeeer),1,(223,100,214))
texttyloser = fontdlyalohov.render("АХАХАХАХАХА ДАЖЕ Я ТАК НЕ ИГРАЮ АХХААХХА",1,(223,0,1))
texttyhacker = fontdlyalohov.render("БАН ЗА ЧИТЫ ОТ АЛГОРИТМИКИ ФФХХФХФХФХФВЗЛФЯТПОРВФИАПОР!!!",1,(223,100,29))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y, player_speed,player_h,player_w):
        super().__init__()
        self.h = player_h
        self.w = player_w
        self.name = player_image
        self.image = transform.scale(image.load(player_image),(self.h,self.w))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >= 15:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <= 780:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self,player_image, player_x,player_y, player_speed,player_h,player_w):
        super().__init__(player_image, player_x,player_y, player_speed,player_h,player_w)
    def respawn(self):
        self.image = transform.scale(image.load(self.name),(random.randint(self.h - 10,self.h + 10),random.randint(self.w - 10,self.w + 10)))
    def update(self):
        self.rect.y += self.speed
        global loozeer
        if self.rect.y >= 1000:
            loozeer += 1
            self.rect.x = random.randint(15,810)
            self.speed = random.randint(3,6)
            self.respawn()
            self.rect.y = -100

class Bullet(GameSprite):
    def __init__(self,player_image, player_x,player_y, player_speed,player_h,player_w):
        super().__init__(player_image, player_x,player_y, player_speed,player_h,player_w)
        self.rect.y = hero.rect.y 
        self.rect.x = hero.rect.x + 28
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()



hero = Player("aav.jpg", 100, 790, 10,100,100)
for i in range(5):
    debily.add(Enemy("aaaa.png",random.randint(15,810) ,-100, random.randint(3,6),random.randint(70,90),random.randint(70,90)))

mixer.init()
mixer.music.load("jewrey.ogg")
mixer.music.play()
winnnner = mixer.Sound("asasasa.ogg")
loser = mixer.Sound("brue.ogg")
fire = mixer.Sound("1.ogg")
paaw = mixer.Sound("probitie1.ogg")
finish = False
game = True
while game:
    n += 1
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if keys_pressed[K_f]:
        fire.play()
        if n >= 15:
            n = 0
            abeme.add(Bullet("bomb.png",-100 ,-100, 10,45,60))
    if not finish :
        window.blit(background, (0,0))
        texttyloh = fontdlyalohov.render("ааа пропущенааекеппппв:" + str(loozeer),1,(225,200,50))
        window.blit(texttyloh,(200,20))
        hero.update()
        hero.reset()
        debily.update()
        debily.draw(window)
        texttynormchel = fontdlyalohov.render("убита лохов тупих:" + str(killeeer),1,(223,100,214))
        window.blit(texttynormchel,(200,80))
        abeme.update()
        abeme.draw(window)
        for i in debily:
            if sprite.collide_rect(hero,i):
                window.blit(texttyloser,(0,200))
                finish = True
                paaw.play()
        for i in debily:
            for b in abeme:
                if sprite.collide_rect(b,i):
                    killeeer += 1
                    i.kill()
                    b.kill()
                    debily.add(Enemy("aaaa.png",random.randint(15,810) ,-100, random.randint(3,6),random.randint(70,90),random.randint(70,90)))
                    loser.play()
        if killeeer >= 30:
            killeeer = 30
            finish = True
            winnnner.play()
            window.blit(texttyhacker,(0,200))
        if loozeer >= 5:
            loozeer = 5
            finish = True
            loser.play()
            window.blit(texttyloser,(0,200))
            
            

    
    clock.tick(FPS)

    display.update()
