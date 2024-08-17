import pygame as pg
from svg.node import GeometryNode

class SVGRenderer:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.image = pg.Surface((width, height))

    def render_node(self, tag: str, attrs: dict[str, str]) -> None:
        node = GeometryNode(tag, attrs)

        pg.draw.rect(self.image, (255,255,255), (0, 0, self.width, self.height))

        self.image.blit(node.render(), (node.global_coords))