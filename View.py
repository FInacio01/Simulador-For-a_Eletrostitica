import pygame as pg


class view:

    def __init__(self, background_collor, width=720, height=480, caption='Título') -> None:
        self.background_collor = background_collor
        self.image = pg.image.load('imagens/atoms.png')
        self.view = pg.display.set_mode((width, height))
        pg.display.set_icon(self.image)
        pg.display.set_caption(caption)
        self.view.fill(background_collor)
        self.draw_plane()

    def show_view(self):
        pg.display.flip()

    def update_view(self):
        self.view.fill(self.background_collor)
        pg.display.update()

    def draw_plane(self):
        pg.draw.rect(self.view, (169, 169, 169), (0, 350, 720, 220))
