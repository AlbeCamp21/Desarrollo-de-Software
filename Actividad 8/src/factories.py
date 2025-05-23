import factory
from .carrito import Producto

class ProductoFactory(factory.Factory):
    class Meta:
        model = Producto

    nombre = factory.Faker("word")
    precio = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
    stock = factory.Faker("random_int", min=10, max=100)  # stock aleatorio
