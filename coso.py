import pygame
import random

pygame.init()
pygame.display.set_caption("coso")
font = pygame.font.SysFont("consolas",12)
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def color(self):
        return (self.r, self.g, self.b)
    
class Coor:
    def __init__(self, x = 0, y = 0, w = 0, h = 0, vel = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel
    def coor(self):
        return (self.x, self.y, self.w, self.w)
    def hit(self):
        return (self.x, self.y, self.x + self.w, self.y + self.w)
    
class Ventana:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.win = pygame.display.set_mode((x, y))

def img(png):
    return pygame.image.load('{}.png'.format(png))

negro = Color(7, 24, 33)
oscuro = Color(48, 104, 80)
claro = Color(134, 192, 108)
blanco = Color(224, 248, 207)

win = Ventana(160, 144)
player = Coor(72, 64, 16, 16, 1)
pokeball = Coor(random.randint(0, 148), random.randint(0, 132), 12, 12)

pk = (img('pk0'),img('pk1'),img('pk2'),img('pk3'),img('pk4'),img('pk5'),
      img('pk6'),img('pk7'),img('pk8'),img('pk9'),img('pk10'),img('pk11'))
ball = img('ball')
bg = img('bg')
clock = pygame.time.Clock()

def Sprite(img,coor):
    win.win.blit(img, coor)
    
def draw(anim, puntaje, time):
    Sprite(bg,(0,0))
    if puntaje > 9:
        ui = font.render("Score: {} Time: {}".format(puntaje, time), True, negro.color())
    else:
        ui = font.render("Score: 0{} Time: {}".format(puntaje, time), True, negro.color())
    Sprite(ui, (0, 0))
    Sprite(ball, pokeball.coor())
    Sprite(pk[anim], player.coor())
    pygame.display.update()
    
def comp(a,b):
    comp = False
    if (a[0] < b[0]) and (a[2] > b[0]):
        if (a[1] < b[1]) and (b[1] < a[3]):
            comp = True
        elif (a[1] < b[3]) and (b[3] < a[3]):
            comp = True
        else:
            comp = False
    elif (a[0] < b[2]) and (a[2] > b[2]):
        if (a[1] < b[1]) and (b[1] < a[3]):
            comp = True
        elif (a[1] < b[3]) and (b[3] < a[3]):
            comp = True
        else:
            comp = False
    else:
        comp = False
    return comp

def paused():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pause = False
        clock.tick(15)
    return pause

def runtime(limite):
    start = pygame.time.get_ticks()
    run = True
    caminando = False
    up = False
    down = False
    time = 0
    i = 0
    c = 0
    x = False
    y = False
    puntaje = 0
    seconds = 0
    while run:
        seconds = (pygame.time.get_ticks() - start) // 1000
        #seconds += clock.tick()/180
        phit = player.hit()
        bhit = pokeball.hit()
        if comp(phit, bhit):
            puntaje += 1
            pokeball.x = random.randint(0, 148)
            pokeball.y = random.randint(0, 132)   
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                puntaje = -1
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    run = False
                    #while paused():
                     #   pygame.display.update()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and player.x > 0) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            player.x -= player.vel
            if y:
                i=3
            else:
                i=9
            down = False
            up = False
        if (keys[pygame.K_RIGHT] and player.x < win.x-player.w) and not (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
            player.x += player.vel
            if y:
                i=0
            else:
                i=5
            down = False
            up = False
        if (keys[pygame.K_UP] and player.y > 0) and not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            player.y -= player.vel
            if x:
                i=7
            else:
                i=8
            up = True
            caminando = True
            down = False
        elif (not caminando) and up:
            if x:
                i=4
            else:
                i=6
        if (keys[pygame.K_DOWN] and player.y < win.y-player.w) and not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            player.y += player.vel
            if x:
                i=10
            else:
                i=11
            caminando = True
            down = True
            up = False
        elif (not caminando) and down:
            if x:
                i=1
            else:
                i=2
        caminando = False
        if seconds > limite:
            seconds = 0
            run = False
        draw(i, puntaje, limite - seconds//1)
        c += 1
        if c>30:
            y = not y
            x = not y
            c = 0
    return puntaje

def gameover(puntaje):
    correr = True
    fin = True
    while correr:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                correr = False
            if event.type == pygame.QUIT:
                fin = False
                correr = False
        if puntaje < 0:
            puntaje = 0    
        ui = font.render("Final score: {}".format(puntaje), True, negro.color())
        playagain = font.render("Continue? press any key", True, negro.color())
        Sprite(bg,(0, 0))
        Sprite(playagain, (0,90,1,1))
        Sprite(ui,(30, 72, 16, 16))
        pygame.display.update()
    return fin
def main():
    correrse = True
    while correrse:
        puntaje = runtime(30)
        if puntaje == -1:
            correrse = False
        fin = gameover(puntaje)
        if not fin:
            correrse = False
main()
pygame.quit()
