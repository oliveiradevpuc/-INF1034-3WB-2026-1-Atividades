from pygame import *
import sys

init()

# Criar relógio
clock = time.Clock()

# Estado inicial
estado = 'mouse'

# Posição do sol
sol_x, sol_y = 100, 100

# Cor de fundo
background_color = (152, 209, 250)

# Posição das nuvens
pos_x, pos_x2, pos_x3 = 450, 700, 800
direcao = 1

# Carregar imagem
homer_png = image.load('homer.png')
homer_png = transform.scale(homer_png, (100,150))

# Fonte
simpson_font = font.Font('Simpsonfont DEMo.ttf', 25)

# Música
mixer.music.load('simpsonsmusica.mp3')
mixer.music.play(-1)

# Janela
window = display.set_mode((1100,720))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            sys.exit()

    # Update
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    # Movimento do sol
    if estado == 'mouse':
        sol_x, sol_y = mouse.get_pos()
    elif estado == 'teclado':
        if keys[K_d]:
            sol_x = sol_x + 300 * dt
        if keys[K_a]:
            sol_x = sol_x - 300 * dt
        if keys[K_w]:
            sol_y = sol_y - 300 * dt
        if keys[K_s]:
            sol_y = sol_y + 300 * dt

    # Limite do sol
    if sol_x > 1100:
        sol_x = 1100
    elif sol_x < 0:
        sol_x = 0

    # Cor do fundo
    if sol_x > 366 and sol_x < 732:
        background_color = (227, 162, 11)
    elif sol_x > 732:
        background_color = (50, 68, 168)
    else:
        background_color = (152, 209, 250)

    window.fill(background_color)

    # Chão
    draw.rect(window, (72, 157, 37), (0, 600, 1100, 120))

    # Casa
    draw.rect(window, (100, 100, 100), (200, 400, 200, 200))
    draw.polygon(window, (166, 60, 15), ((190, 400), (230, 300), (370,300), (410,400)))
    draw.rect(window, (13,22,100), (230, 480, 50, 80))
    draw.rect(window, (121,77,27), (300, 465, 65, 135))
    draw.circle(window, (0,0,0), (310, 530), 5)

    # Árvore
    draw.rect(window, (121,77,27), (680,460,40,140))
    draw.circle(window, (72, 157, 37), (700,400), 75)

    # Sol
    draw.circle(window, (235, 242, 17), (int(sol_x), int(sol_y)), 60)
    draw.line(window, (235, 242, 17), (int(sol_x), int(sol_y+60)), (int(sol_x), int(sol_y+130)), 5)
    draw.line(window, (235, 242, 17), (int(sol_x+60), int(sol_y)), (int(sol_x+130), int(sol_y)), 5)
    draw.line(window, (235, 242, 17), (int(sol_x), int(sol_y-60)), (int(sol_x), int(sol_y-130)), 5)
    draw.line(window, (235, 242, 17), (int(sol_x-60), int(sol_y)), (int(sol_x-130), int(sol_y)), 5)

    # Nuvens (agora usando posição)
    draw.circle(window, (235,235,235), (int(pos_x),100), 50)
    draw.circle(window, (235,235,235), (int(pos_x+50),100), 50)
    draw.circle(window, (235,235,235), (int(pos_x+100),100), 50)

    draw.circle(window, (235,235,235), (int(pos_x2),200), 50)
    draw.circle(window, (235,235,235), (int(pos_x2+50),200), 50)
    draw.circle(window, (235,235,235), (int(pos_x2+100),200), 50)

    # Movimento das nuvens
    pos_x = pos_x + (100 * direcao) * dt
    pos_x2 = pos_x2 + (100 * direcao) * dt

    if pos_x2 > 1100:
        direcao = -1
    elif pos_x < 0:
        direcao = 1

    # Imagem
    window.blit(homer_png, (450, 470))

    # Texto
    texto = simpson_font.render('The Simpsons...', True, (0,0,0))
    window.blit(texto, (410,650))

    display.update()
    clock.tick(60)