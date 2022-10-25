"""
SVG avatar generation library
More info @ https://github.com/emreihtiyar/advanced-textract-parser
"""

__version__ = "0.0.1"

import enum


class JobStatus(enum.Enum):
    """Job status enum"""
    PENDING = 0
    IN_PROGRESS = 1
    SUCCEEDED = 2
    FAILED = 3


class 

class TextractDocument:
    analyze_document_model_version = "1.0"
    job_status = JobStatus.PENDING
    document_metadata = None
    
    def __init__(self, blocks:list, document_metada:dict, job_status):
        pass
    
    @classmethod
    def from_json(cls, json):
        cls.analyze_document_model_version = json.get("AnalyzeDocumentModelVersion")