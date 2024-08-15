import pygame as pg
from svg.geometry.ellipse import Circle

class GeometryNode:
    def __init__(self, tag: str, attributes: dict[str, str]) -> None:
        self.tag = tag
        self.attrs = attributes

        self.geometry = self.get_geometry()

    @property
    def global_coords(self) -> tuple[int, int]:
        if self.geometry is None: return (0, 0)

        return self.geometry.global_coords

    def render(self) -> pg.Surface:
        if self.geometry is None: return pg.Surface((0, 0))

        return self.geometry.render()

    def create_circle(self) -> Circle:
        return Circle(int(self.attrs["cx"]), int(self.attrs["cy"]), int(self.attrs["r"]), self.attrs.get("path_length", None))

    def get_geometry(self) -> object:
        match self.tag:
            case "circle":
                return self.create_circle()
        
        return None