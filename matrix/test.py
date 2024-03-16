import pygame as pg
from random import randint
import colors
import sys
from sprites import W,H,Symbol

pg.init()
sc = pg.display.set_mode((W,H))
font = pg.font.SysFont('Perfo Bold', 30)

columns = 30
col_w = W // columns

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper() + '1234567890'
Symbol_surf = []
for symb in alphabet:
	symb_surf = font.render(symb, True, colors.GREEN)
	w, h = symb_surf.get_size()
	surf = pg.Surface((col_w, col_w))
	sx = col_w // 2 - w // 2
	sy = col_w // 2 - h // 2
	surf.blit(symb_surf, (sx, sy))
	Symbol_surf.append(surf)

Symbols = pg.sprite.Group()

for i in range(1, columns + 1):
    sy = randint(-100, -20)
    sx = i * col_w - col_w // 2
    rand_i = randint(0, len(Symbol_surf) - 1)
    Symbol(Symbol_surf[rand_i], (sx, sy), Symbols)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit

    sc.fill(colors.BLACK)

    Symbols.draw(sc)
    Symbols.update()

    for s in Symbols.sprites()[-columns:]:
        sx = s.rect.centerx
        sy = s.rect.centery - s.rect.h - 10
        rand_i = randint(0, len(Symbol_surf) - 1)
        Symbol(Symbol_surf[rand_i], (sx, sy), Symbols)

    pg.display.update()
    pg.time.delay(20)
pygame.quit()
