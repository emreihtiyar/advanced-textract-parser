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
            raise NotImplementedError('Unknown job status: {}'.format(label))


class DocumentMetadata:
    """Document metadata"""
    def __init__(self, **metadata_dict):
        self.__dict__.update(metadata_dict)
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __hash__(self) -> int:
        return hash(str(self))


class TextractDocument:
    analyze_document_model_version = "1.0"
    
    def __init__(self, blocks:list, document_metadata:DocumentMetadata, job_status:JobStatus, analyze_document_model_version="1.0"):
        self.blocks = blocks
        self.document_metadata = document_metadata
        self.job_status = job_status
        self.analyze_document_model_version = analyze_document_model_version
    
    @classmethod
    def from_json(cls, json):
        from ipdb import set_trace; set_trace()
        return TextractDocument(
            blocks=[],
            document_metadata=DocumentMetadata(**json.get("DocumentMetadata")),
            job_status=JobStatus.from_str(json.get("JobStatus")),
            analyze_document_model_version=json.get("AnalyzeDocumentModelVersion")
        )