
# Bespoke furniture store


class DimensionMixin:

    def __init__(self, width, height, length, weight):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight


class Product:
    def __init__(self, color):
        self.color = color


class FlatSurface(DimensionMixin, Product):

    def __init__(self, w, h, l, weight, color):
        DimensionMixin.__init__(self, w, h, l, weight)
        Product.__init__(self, color)

class Leg(DimensionMixin, Product):
    pass


class CardboardBox(DimensionMixin, Product):
    pass


# For the given table and table legs,
# select a cardboard fitting perfectly those dimensions
# 4 legs and one table

# cardboard_1 = CardboardBox(20, 30, 50, 0.200)
# cardboard_2 = CardboardBox(40, 40, 40, 0.200)
# cardboard_3 = CardboardBox(60, 30, 60, 0.200)
#
flat_surface = FlatSurface(20, 20, 5, 1, "white")
print(flat_surface.color)
#
# leg_1 = Leg(2, 2, 5, 0.100)
# leg_2 = Leg(2, 2, 5, 0.100)
# leg_3 = Leg(2, 2, 5, 0.100)
# leg_4 = Leg(2, 2, 5, 0.100)
print(flat_surface)
