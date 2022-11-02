import Geometry
from src.Types import BlockType, TextType


class BaseBlock:
    def __init__(self, id: str, block_type: BlockType, geometry: Geometry, relationships: list) -> None:
        self.id = None
        self.block_type = None
        self.geometry = None
        self.relationships = None


class PageBlock(BaseBlock):
    def __init__(self, id: str, block_type: BlockType, geometry: Geometry, relationships: list, page_number: int) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.page_number = page_number


class LineBlock(BaseBlock):
    def __init__(self, id: str, block_type: BlockType, geometry: Geometry, relationships: list,
                 page: PageBlock, text: str, confidence: float) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.text = text
        self.confidence = confidence
        self.page = page


class WordBlock(BaseBlock):
    def __init__(self, id: str, block_type: BlockType, geometry: Geometry, relationships: list,
                 page: PageBlock, line: LineBlock, text: str, confidence: float, text_type: TextType) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.text = text
        self.confidence = confidence
        self.page = page
        self.line = line
        self.text_type = text_type
