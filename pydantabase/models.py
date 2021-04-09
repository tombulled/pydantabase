import pydantic

from . import mixins

class BaseModel(mixins.ModelMixin, pydantic.BaseModel): pass
