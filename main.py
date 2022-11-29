import pygame as pg


pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Canicas Rebotando")

game_over = False

x = 400
y = 300

x1 = 200
y1 = 100

vx = 1
vy = 1

vx1 = 1
vy1 = 1

while not game_over:

    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
            
            
    pantalla_principal.fill((52,152,219))
    
    x += vx
    y += vy
    
    x1 += vx1
    y1 += vy1
    
    
    if x >= 800 or x == 0:
        vx *=-1
    
    if y >= 600 or y == 0:
        vy *= -1
        
    if x1 >= 800 or x1 == 0:
        vx1 *=-1
    
    if y1 >= 600 or y1 == 0:
        vy1 *= -1  
    
    
    pg.draw.rect(pantalla_principal,(248,10,21),(x,y,20,20))
    pg.draw.rect(pantalla_principal,(230,248,10),(x1,y1,20,20))
    
    
    pg.display.flip()
