class Item:
    def __init__(self, type):
        self.name  = 'Unset'
        self.type  = type
        self.value = 0

    def get_class(self):
        return self.__class__.__name__
