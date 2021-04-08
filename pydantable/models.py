import pydantic

class BaseModel(pydantic.BaseModel):
    class Config:
        allow_mutation = False

    def __getitem__(self, key):
        return getattr(self, key)

class Document(BaseModel):
    _doc_id: int = pydantic.PrivateAttr()

    def __init__(self, value: dict, doc_id: int):
        super().__init__(**value)

        self._doc_id = doc_id

    @property
    def doc_id(self):
        return self._doc_id
