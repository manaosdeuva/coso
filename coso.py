import pygame
import random

pygame.init()
scale = 1
pygame.display.set_caption("coso")
font = pygame.font.SysFont("consolas", 12*scale)

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
def trs(png,xy):
    return pygame.transform.scale(png,xy)

negro = Color(7, 24, 33)
oscuro = Color(48, 104, 80)
claro = Color(134, 192, 108)
blanco = Color(224, 248, 207)

win = Ventana(160*scale, 144*scale)
player = Coor(72*scale, 64*scale, 16*scale, 16*scale, 1*scale)
pokeball = Coor(random.randint(0, 148*scale), random.randint(0, 132*scale), 12*scale, 12*scale)

pk = [img('pk0'),img('pk1'),img('pk2'),img('pk3'),img('pk4'),img('pk5'),
      img('pk6'),img('pk7'),img('pk8'),img('pk9'),img('pk10'),img('pk11')]
fondo = [img('bg'),img('bg1'),img('bg2'),img('bg3'),img('bg4')]

ball = img('ball')
bg = fondo[2]
bg = trs(bg,(win.x,win.y))
ball = trs(ball,(12*scale,12*scale))

for w in range(len(pk)):
    pk[w] = trs(pk[w],(16*scale,16*scale))
clock = pygame.time.Clock()

def Sprite(img,coor):
    win.win.blit(img, coor)
    
def draw(anim, puntaje, time, bac):
    bg = fondo[bac]
    bg = trs(bg,(win.x,win.y))
    Sprite(bg,(0,0,win.x*scale,win.y*scale))
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
    back = 2
    while run:
        seconds = (pygame.time.get_ticks() - start) // 1000
        phit = player.hit()
        bhit = pokeball.hit()
        if comp(phit, bhit):
            puntaje += 1
            pokeball.x = random.randint(0, 148*scale)
            pokeball.y = random.randint(10*scale, 132*scale)
            limite+=1
            if puntaje%10==0:
                back = random.randint(0,4)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                puntaje = -1
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_SPACE:
                    run = False
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
        if (keys[pygame.K_UP] and player.y > 10*scale) and not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
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
        draw(i, puntaje, limite - seconds//1, back)
        c += 1
        if c>30:
            y = not y
            x = not y
            c = 0
    return puntaje

def gameover(puntaje):
    correr = True
    fin = True
    bg = fondo[4]
    bg = trs(bg,(win.x,win.y))
    while correr:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key != pygame.K_UP) and (event.key != pygame.K_DOWN) and (event.key != pygame.K_RIGHT) and (event.key != pygame.K_LEFT):
                    correr = False
            if event.type == pygame.QUIT:
                fin = False
                correr = False
        if puntaje < 0:
            puntaje = 0    
        ui = font.render("Final score: {}".format(puntaje), True, negro.color())
        playagain = font.render("Continue? press any key", True, negro.color())
        Sprite(bg,(0, 0,win.x*scale,win.y*scale))
        Sprite(playagain, (0,90*scale,1*scale,1*scale))
        Sprite(ui,(30*scale, 72*scale, 16*scale, 16*scale))
        pygame.display.update()
    return fin

def title():
    run = True
    title = img('title')
    title = trs(title,(win.x,win.y))
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run = False
        Sprite(title,(0,0,win.x*scale,win.y*scale))
        pygame.display.update()

def main():
    correrse = True
    title()
    while correrse:
        puntaje = runtime(30)
        if puntaje == -1:
            correrse = False
        fin = gameover(puntaje)
        if not fin:
            correrse = False

main()
pygame.quit()
