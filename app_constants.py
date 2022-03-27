class DictAttr(dict):
    def __getattr__(self, attr):
        return self[attr]
    def __setattr__(self, attr, value):
        self[attr] = value

constants = {
'db': 'movies'
}

constants = DictAttr(constants)

