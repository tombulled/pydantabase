import pydantic

from . import mixins

class BaseModel(mixins.ModelMixin, pydantic.BaseModel):
    class Config:
        allow_mutation: bool = False
