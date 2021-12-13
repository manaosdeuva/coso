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

function img(png){
    return "pygame.image.load('{}.png'.format(png))"
}

function trs(png,xy){
    return "pygame.transform.scale(png,xy)"
}