import pydantic

from . import models

class Document(models.BaseModel):
    _doc_id: int = pydantic.PrivateAttr()

    def __init__(self, value: dict, doc_id: int):
        super().__init__(**value)

        self._doc_id = doc_id

    @property
    def doc_id(self):
        return self._doc_id
