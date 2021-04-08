import tinydb
import tinydb.table
import tinydb.storages
import functools

from . import models

class ModelTable(tinydb.table.Table):
    def __init__(self, model_type: type):
        super().__init__ \
        (
            name    = tinydb.table.Table.__name__.lower(),
            storage = tinydb.storages.MemoryStorage(),
        )

        @functools.wraps(model_type, updated=())
        class ModelDocument(models.Document, model_type): pass

        self.document_class = ModelDocument

    def insert(self, model):
        return super().insert(model.dict())

class MappedModelTable(ModelTable):
    document_query: tinydb.Query

    def __init__(self, model_type: type, document_query: tinydb.Query):
        super().__init__(model_type)

        self.document_query = document_query

    def __getitem__(self, value):
        return self.get(self.document_query == value)
