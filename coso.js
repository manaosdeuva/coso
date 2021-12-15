let scale = 1

class Color {
    constructor(r, g, b) {
        this.r = r
        this.g = g
        this.b = b
    }
    color() {
        return [this.r, this.g, this.b]
    }
}

class Coor {
    constructor(x = 0, y = 0, w = 0, h = 0, vel = 0) {
        this.x = x
        this.y = y
        this.w = w
        this.h = h
        this.vel = vel
    }
    coor() {
        return [this.x, this.y, this.w, this.h]
    }
    hit() {
        return [(this.x, this.y, this.x + this.w, this.y + this.w)]
    }
}

class Ventana {
    constructor(x, y) {
        this.x = x
        this.y = y
        this.win = "pygame.display.set_mode((x, y))"
        //boludez de pygame
    }
}

function img(png) {
    return "pygame.image.load('{}.png'.format(png))"
}

function trs(png, xy) {
    return "pygame.transform.scale(png,xy)"
}

let negro = new Color(7, 24, 33),
    oscuro = new Color(48, 104, 80),
    claro = new Color(134, 192, 108),
    blanco = new Color(224, 248, 207),
    win = new Ventana(160 * scale, 144 * scale),
    player = new Coor(72 * scale, 64 * scale, 16 * scale, 16 * scale, 1 * scale),
    pokeball = new Coor(random.randint(0, 148 * scale), random.randint(0, 132 * scale), 12 * scale, 12 * scale),
    pk = [img('pk0'), img('pk1'), img('pk2'), img('pk3'), img('pk4'), img('pk5'),
    img('pk6'), img('pk7'), img('pk8'), img('pk9'), img('pk10'), img('pk11')],
    fondo = [img('bg'), img('bg1'), img('bg2'), img('bg3'), img('bg4')],
    ball = img('ball'),
    bg = fondo[2],
    bg = trs(bg, (win.x, win.y)),
    ball = trs(ball, (12 * scale, 12 * scale))

for (let w = 0; w < pk.length; w++) {
    pk[w] = trs(pk[w], (16 * scale, 16 * scale))
}
clock = pygame.time.Clock()



