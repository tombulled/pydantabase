# pydantabase
Pydantic integration for TinyDB

## Example:
```python
import pydantabase
import tinydb.storages

class Person(pydantabase.BaseModel):
    name: str
    age: int

class Database(pydantabase.Database):
    default_storage_class = tinydb.storages.MemoryStorage
        
db = Database(Person)

db.insert_multiple([
    Person(
        name = 'Paul',
        age = 53,
    ),
    Person(
        name = 'Rebecca',
        age = 47,
    ),
])
```

```python
>>> db.get(tinydb.Query().name == 'Paul')
Person(name='Paul', age=53)
```