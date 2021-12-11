# pydantabase
Pydantic integration for TinyDB

## Example:
```python
import pydantic
import pydantabase
import tinydb.storages
import enum
import typing

class BaseModel(pydantabase.ModelMixin, pydantic.BaseModel):
    class Config:
        allow_mutation: bool = False

class ParentType(enum.Enum):
    COOL   = enum.auto()
    BORING = enum.auto()

class Child(BaseModel):
    name: str
    age:  int

class Parent(BaseModel):
    type:  ParentType
    name:  str
    age:   int
    child: Child

class Database(pydantabase.Database):
    default_storage_class = tinydb.storages.MemoryStorage

    def __getitem__(self, type: enum.Enum) -> typing.Optional[pydantic.BaseModel]:
        return self.get(pydantabase.Query().type == type)
        
db = Database(Parent)

p = Parent \
(
    type  = ParentType.COOL,
    name  = 'Parent',
    age   = 53,
    child = Child \
    (
        name = 'Child',
        age  = 8,
    ),
)
p2 = Parent \
(
    type  = ParentType.BORING,
    name  = 'Parent2',
    age   = 54,
    child = Child \
    (
        name = 'Child2',
        age  = 9,
    ),
)

db.insert(p)
db.insert(p2)

d  = db.get(tinydb.Query().name       == 'Parent')
d2 = db.get(tinydb.Query().child.name == 'Child')
```