import typing

class ModelMixin(object):
    def __getitem__(self, key: str) -> typing.Any:
        return getattr(self, key)
