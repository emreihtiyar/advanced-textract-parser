import json
from src import TextractDocument


with open("response example.json") as f:
    json_data = json.load(f)
    textract_document = TextractDocument.from_json(json_data)
TextractDocument.from_json()