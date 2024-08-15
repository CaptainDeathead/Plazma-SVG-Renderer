import pygame as pg
from bs4 import BeautifulSoup
from bs4.element import Tag
from svg.renderer import SVGRenderer

class SVGParser:
    def __init__(self, svg_code: str) -> None:
        self.svg_code: str = svg_code

        self.xml_tree = BeautifulSoup(svg_code, 'html.parser')
        
        for node in self.xml_tree.find_all():
            if node.name == "svg":
                width, height = int(node.attrs["width"]), int(node.attrs["height"])
                break

        self.renderer = SVGRenderer(width, height)

    def render_svg(self) -> pg.Surface:
        node_stack = [self.xml_tree]

        while len(node_stack) > 0:
            node = node_stack.pop(0)
            if not isinstance(node, Tag): continue

            self.renderer.render_node(node.name, node.attrs)

            for child in node.children:
                node_stack.append(child)

        return self.renderer.image