import enum
from src.Exceptions import TypeNotFoundError

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
            raise  TypeNotFoundError(f'Unknown block type: {label}')


class TextType(enum.Enum):
    "Text Type enum"
    PRINTED = 0
    HANDWRITTEN = 1


class JobStatus(enum.Enum):
    """Job status enum"""
    PENDING = 0
    IN_PROGRESS = 1
    SUCCEEDED = 2
    FAILED = 3
    
    @classmethod
    def from_str(cls, label):
        if label in ('SUCCEEDED', 'succeeded', 'Succeeded'):
            return cls.SUCCEEDED
        elif label in ('FAILED', 'failed', 'Failed'):
            return cls.FAILED
        elif label in ('IN_PROGRESS', 'in_progress', 'In_progress'):
            return cls.IN_PROGRESS
        elif label in ('PENDING', 'pending', 'Pending'):
            return cls.PENDING
        else:
            raise TypeNotFoundError(f'Unknown job status: {label}')