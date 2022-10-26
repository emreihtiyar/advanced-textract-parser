
import enum
import Geometry

class BlockType(enum.Enum):
    """Job status enum"""
    PAGE = 0
    LINE = 1
    WORD = 2
    KEY_VALUE_SET = 3
    
    @classmethod
    def from_str(cls, label):
        if label in ('PAGE', 'page', 'Page'):
            return cls.PAGE
        elif label in ('LINE', 'line', 'Line'):
            return cls.LINE
        elif label in ('WORD', 'word', 'Word'):
            return cls.WORD
        elif label in ('KEY_VALUE_SET', 'key_value_set', 'Key_value_set'):
            return cls.KEY_VALUE_SET
        else:
            raise NotImplementedError('Unknown block type: {}'.format(label))


class TextType(enum.Enum):
    "Text Type enum"
    PRINTED = 0
    HANDWRITTEN = 1



class BaseBlock:
    def __init__(self, id:str, block_type:BlockType, geometry:Geometry, relationships:list) -> None:
        self.id = None
        self.block_type = None
        self.geometry = None
        self.relationships = None


class PageBlock(BaseBlock):
    def __init__(self, id:str, block_type:BlockType, geometry:Geometry, relationships:list, page_number:int) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.page_number = page_number


class LineBlock(BaseBlock):
    def __init__(self, id:str, block_type:BlockType, geometry:Geometry, relationships:list,\
                page:PageBlock ,text:str, confidence:float) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.text = text
        self.confidence = confidence
        self.page = page


class WordBlock(BaseBlock):
    def __init__(self, id:str, block_type:BlockType, geometry:Geometry, relationships:list,\
                page:PageBlock, line:LineBlock, text:str,confidence:float, text_type:TextType) -> None:
        super().__init__(id, block_type, geometry, relationships)
        self.text = text
        self.confidence = confidence
        self.page = page
        self.line = line
        self.text_type = text_type