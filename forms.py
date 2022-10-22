import pygame as pg

pg.init()
pg.font.init()


class carga:
    def __init__(self, pos_x, pos_y, sinal_carga) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cont = 1
        self.sinal_carga = sinal_carga
        if sinal_carga.lower() == 'negativo':
            icone = 'imagens/menos.png'
        else:
            icone = 'imagens/mais.png'
        self.carga_elementar = 1.6 * 10 ** (-19)
        self.valor_carga = self.carga_elementar
        imagem = pg.image.load(icone)
        self.icone = pg.transform.scale(imagem, (60, 60))

    def draw_carga(self, surface):
        surface.view.blit(self.icone, (self.pos_x, self.pos_y))

    def change_icon(self, icon_link):
        self.icone = pg.image.load(icon_link)
        self.icone = pg.transform.scale(self.icone, (60, 60))
        sinal = icon_link[8:12]
        if 'mais' in icon_link:
            self.sinal_carga = 'positivo'
        elif 'menos' in icon_link:
            self.sinal_carga = 'negativo'
        else:
            print('Deu erro mano')
        print(self.sinal_carga)

    def increment_x(self, increment):
        if 99 < self.pos_x < 501 and 99 < self.pos_x + increment < 501:
            self.pos_x += increment

    def increment_carga(self, increment):
        if 0 < self.cont < 11 and 0.1 < self.cont + increment < 10.1:
            self.cont += increment
            if increment > 0:
                self.valor_carga = self.valor_carga + self.carga_elementar
            else:
                self.valor_carga = self.valor_carga - self.carga_elementar


class button_menu:
    def __init__(self, icon_link, button_x, button_y, size_button=None) -> None:
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)

        self.icon = pg.image.load(icon_link)
        if size_button != None:
            self.icon = pg.transform.scale(self.icon, size_button)
        self.button_x = button_x
        self.button_y = button_y
        self.size = self.icon.get_size()
        self.mouse_in_button = False

    def verifica_mouse(self):
        mouse = pg.mouse.get_pos()
        if self.button_x <= mouse[0] <= self.button_x + self.size[0] and self.button_y <= mouse[1] <= self.button_y + \
                self.size[1]:
            return True
        else:
            return False

    def draw_button(self, surface):
        surface.blit(self.icon, (self.button_x, self.button_y))


class lable:
    def __init__(self, text, size, lbl_x, lbl_y, color='black'):
        self.font = pg.font.SysFont("Arial", size)
        self.text = text
        self.txt = self.font.render(text, True, color)
        _, _, w, h = self.txt.get_rect()
        self.rect = pg.Rect(lbl_x, lbl_y, w, h)

    def draw(self, surface):
        surface.blit(self.txt, (self.rect))

    def change_text(self, newtext, color="black"):
        self.txt = self.font.render(newtext, 1, color)


class box_text:
    def __init__(self, lable, size, color='white') -> None:
        self.lable = lable
        self.collor = color
        self.pos_box = self.lable.rect[:2]
        self.size = size

    def draw_box(self, surface):
        pg.draw.rect(surface, self.collor, [self.pos_box[0], self.pos_box[1], self.size[0], self.size[1]])
        self.lable.draw(surface)