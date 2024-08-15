import pygame as pg
from svg.parser import SVGParser

pg.init()

class Window:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((800, 600))

        self.SVG_PATH: str = "./test/circle.svg"
        self.svg_parser = SVGParser(open(self.SVG_PATH).read())

        self.screen.blit(self.svg_parser.render_svg(), (0, 0))

    def main(self) -> None:
        clock = pg.time.Clock()

        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            pg.display.flip()
            clock.tick(60)

def main() -> None:
    window = Window()
    window.main()

if __name__ == "__main__":
    main()
    