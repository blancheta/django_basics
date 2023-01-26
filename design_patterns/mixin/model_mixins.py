
# Second hand

class DimensionMixin:

    def __init__(self, width, height, weight):
        self.width = width
        self.height = height
        self.weight = weight


class Product:

    def __init__(self, name):
        self.name = name


class Table(Product, DimensionMixin):
    pass


class Chair(Product, DimensionMixin):
    pass


class CardboardBox(DimensionMixin):
    pass


