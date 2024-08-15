import pygame as pg

class Circle:
    def __init__(self, cx: float = 0.0, cy: float = 0.0, r: float = 0.0, path_length: float = None) -> None:
        self.cx = cx
        self.cy = cy
        self.radius = r
        self.path_length = path_length

        self.color = (255, 0, 0) # Example (test) color

        self.surface = pg.Surface((self.radius*2, self.radius*2))

    @property
    def global_coords(self) -> tuple[int, int]:
        return self.cx - self.radius, self.cy - self.radius

    def render(self) -> pg.Surface:
        # filled eclipse
        pg.draw.circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        
        return self.surface