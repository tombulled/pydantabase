import tinydb

import functools

from . import document
from . import table

class Database(tinydb.TinyDB):
    def __init__(self, model: type, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @functools.wraps(model, updated = ())
        class Document(document.Document, model): pass

        @functools.wraps(table.Table, updated = ())
        class Table(table.Table):
            document_class: type = Document

        self.table_class = Table
