

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


class BoundingBox:
    def __init__(self, top_left:Point, bottom_right:Point) -> None:
        self.tl = top_left
        self.br = bottom_right
        self.tr = Point(bottom_right.x, top_left.y)
        self.bl = Point(top_left.x, bottom_right.y)
    
    @classmethod
    def from_tlwh(cls, top_left:Point, width:float, height:float) -> 'BoundingBox':
        return cls(top_left, Point(top_left.x + width, top_left.y + height))
    
    @classmethod
    def from_tlwh2(cls, top:float, left:float, width:float, height:float) -> 'BoundingBox':
        return cls.from_tlwh(Point(left, top), width, height)
    
    def __eq__(self, __o: object) -> bool:
        return self.tl == __o.tl and self.br == __o.br

class Polygon:
    def __init__(self, points:list) -> None:
        self.points = points
    
    def __eq__(self, __o: object) -> bool:
        return self.points == __o.points


class Geometry:
    def __init__(self, bounding_box:BoundingBox, polygon:Polygon) -> None:
        self.bounding_box = bounding_box
        self.polygon = polygon
    
    def __eq__(self, __o: object) -> bool:
        return self.bounding_box == __o.bounding_box and self.polygon == __o.polygon