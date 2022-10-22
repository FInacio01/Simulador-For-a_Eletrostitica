import pygame as pg
from View import view
from forms import *

pg.init()


def calc_forca(q1, q2, r):
    k = 9 * 10 ** 9
    forca = k * (q1 * q2) / r ** 2
    return forca


def verifica_setido_forca(carga1, carga2):
    if carga1.sinal_carga == carga2.sinal_carga:
        setas_forca = ('imagens/seta_esquerda.png', 'imagens/seta_direita.png')
    else:
        setas_forca = ('imagens/seta_direita.png', 'imagens/seta_esquerda.png')
    return setas_forca


# Inicia a tela e os objetos
cor_tela = (211, 211, 211)
carga_prova = carga(100, 290, 'negativo')
carga_fixa = carga(570, 290, 'positivo')
painel = view(background_collor=cor_tela, caption='Simulador - Lei de Coulomb')
formula = pg.image.load('imagens/Força.gif')
formula = pg.transform.scale(formula, (150, 100))
view.show_view(painel)
velocidade_x = 1
running = True

buttons = {button_menu('imagens/mais_button.png', 690, 30, (25, 25)): [carga_prova.increment_carga, 1],
           button_menu('imagens/menos_button.png', 580, 30, (25, 25)): [carga_prova.increment_carga, -1],
           button_menu('imagens/mais_button.png', 690, 80, (25, 25)): [carga_fixa.increment_carga, 1],
           button_menu('imagens/menos_button.png', 580, 80, (25, 25)): [carga_fixa.increment_carga, -1],
           button_menu('imagens/mais_button.png', 690, 130, (25, 25)): [carga_prova.increment_x, -50],
           button_menu('imagens/menos_button.png', 580, 130, (25, 25)): [carga_prova.increment_x, +50],
           button_menu('imagens/mais.png', 50, 100, (20, 20)): [carga_prova.change_icon, 'imagens/mais.png'],
           button_menu('imagens/menos.png', 80, 100, (20, 20)): [carga_prova.change_icon, 'imagens/menos.png'],
           button_menu('imagens/mais.png', 50, 140, (20, 20)): [carga_fixa.change_icon, 'imagens/mais.png'],
           button_menu('imagens/menos.png', 80, 140, (20, 20)): [carga_fixa.change_icon, 'imagens/menos.png']
           }

lbls = [lable('Carga Q1', 15, 520, 33, 'black'),
        lable('Carga Q2', 15, 520, 83, 'black'),
        lable('Distância R', 15, 515, 133, 'black'),
        lable('Força Eletrostática', 30, 240, 40, 'black'),
        lable('Q1: ', 20, 10, 100, 'black'),
        lable('Q2: ', 20, 10, 140, 'black')]

lbl_forca = [lable('F =', 25, 530, 200, 'black'),
             lable('0', 25, 570, 200, 'black')]

boxes = [box_text(lable(str(carga_prova.valor_carga) + ' C', 15, 605, 30, 'black'), (85, 25)),
         box_text(lable(str(carga_fixa.valor_carga) + ' C', 15, 605, 80, 'black'), (85, 25)),
         box_text(lable(str((carga_fixa.pos_x - carga_prova.pos_x) / 1000) + ' m', 15, 605, 130, 'black'), (85, 25))]

clock = pg.time.Clock()

# Loop principal
while running:
    mouse = pg.mouse.get_pos()

    painel.view.fill(painel.background_collor)

    # Captura os eventos que fecham a aplicação
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            for button in buttons.keys():
                if button.verifica_mouse():
                    buttons[button][0](buttons[button][1])

    boxes[0].lable.change_text(f'{carga_prova.valor_carga:.2e} C')
    boxes[1].lable.change_text(f'{carga_fixa.valor_carga:.2e} C')
    boxes[2].lable.change_text(f'{(carga_fixa.pos_x - carga_prova.pos_x) / 1000} m')
    for box in boxes:
        box.draw_box(painel.view)

    for lbl in lbls:
        lbl.draw(painel.view)

    r = (carga_fixa.pos_x - carga_prova.pos_x) / 1000
    forca = calc_forca(carga_prova.valor_carga, carga_fixa.valor_carga, r)
    lbl_forca[1].change_text(f'{forca:.2e} N/C')
    for lbl in lbl_forca:
        lbl.draw(painel.view)

    setas_forca = verifica_setido_forca(carga_prova, carga_fixa)
    imagem = pg.image.load(setas_forca[0])
    imagem = pg.transform.scale(imagem, (55, 55))
    painel.view.blit(imagem, (carga_prova.pos_x, carga_prova.pos_y - 40))
    imagem = pg.image.load(setas_forca[1])
    imagem = pg.transform.scale(imagem, (55, 55))
    painel.view.blit(imagem, (carga_fixa.pos_x, carga_fixa.pos_y - 40))

    # painel.view.blit(formula, (100, 50))
    painel.draw_plane()
    carga_prova.draw_carga(painel)
    carga_fixa.draw_carga(painel)
    for button in buttons:
        button.draw_button(painel.view)

    pg.display.update()
    clock.tick(20)
pg.quit()
