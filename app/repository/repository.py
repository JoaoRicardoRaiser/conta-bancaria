import uuid


class Repository:
    def __init__(self):
        self._data = []

    def save(self, obj):
        self._data.append(obj)

    def get(self, id: uuid):
        for obj in self._data:
            if obj['id'] == id:
                return obj
        return None

    def get_all(self):
        return self._data
