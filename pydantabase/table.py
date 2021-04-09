import tinydb.table
import pydantic
import typing

class Table(tinydb.table.Table):
    def insert(self, model: pydantic.BaseModel) -> int:
        return super().insert(model.dict())

    def insert_multiple(self, models: typing.List[pydantic.BaseModel]) -> typing.List[int]:
        return list(map(self.insert, models))
