import pytest
from src.carrito import Carrito, Producto
from src.factories import ProductoFactory

def test_agregar_producto_nuevo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    carrito.agregar_producto(producto_generico, cantidad=1)
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == "Genérico"
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    # Act
    carrito.agregar_producto(producto_generico, cantidad=2)
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    # Act
    carrito.remover_producto(producto_generico, cantidad=1)
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    # Act
    carrito.remover_producto(producto_generico, cantidad=3)
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    producto2 = ProductoFactory(nombre="Escáner", precio=150.00)
    carrito.agregar_producto(producto2, cantidad=1)  # Total 150
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 350.00


def test_aplicar_descuento(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)  # 100
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 90.00


def test_aplicar_descuento_limites(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)

def test_vaciar_carrito(carrito, producto_generico):
    """
    Arrange: Se crean productos y se agregan al carrito
    Act: Se vacia el carrito
    Assert: Se verifica que no haya items en el carrito y que el costo sea 0
    """
    # arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    producto_2 = ProductoFactory(nombre="Pera", precio=2.0)
    carrito.agregar_producto(producto_2, cantidad=1)
    # act
    carrito.vaciar()
    # assert
    assert carrito.obtener_items() == []
    assert carrito.calcular_total() == 0

def test_aplicar_descuento_condicion(carrito, producto_generico):
    """
    Arrange: Se crean productos y se agregan al carrito
    Act: Se prueba si se aplica o no el descuento
    Assert: Se verifica que el descuento se calculó correctamente
    """
    # arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    producto_2 = ProductoFactory(nombre="Ropero", precio=200)
    carrito.agregar_producto(producto_2, cantidad=1)
    # act
    total_con_descuento = carrito.aplicar_descuento_condicion(50, 250)
    # assert
    assert total_con_descuento == 150

def test_agregar_producto_dentro_del_stock(carrito, producto_generico):
    """
    Arrange: Se crea un carrito y un producto con stock random
    Act: Se agrega dicho producto al carrito
    Assert: Se verifica que la cantidad y precio sean correctos
    """
    # arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    # assert
    assert len(carrito.obtener_items()) == 1
    assert carrito.obtener_items()[0].cantidad == 2
    assert carrito.calcular_total() == producto_generico.precio * 2

def test_ordenar_items_por_precio(carrito, producto_generico):
    """
    Arrange: Crear carrito, productos y agregar estos al carrito
    Act: Obtener items del carrito segun su precio
    Assert: Se verifica el orden de cada item
    """
    # arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    producto_2 = ProductoFactory(nombre="Platano", precio=1.2)
    producto_3 = ProductoFactory(nombre="Fresa", precio=2.0)
    carrito.agregar_producto(producto_2, cantidad=2)
    carrito.agregar_producto(producto_3, cantidad=1)
    # act
    items_ordenados = carrito.obtener_items_ordenados("precio")
    # assert
    assert items_ordenados[0].producto.nombre == "Platano"
    assert items_ordenados[1].producto.nombre == "Fresa"
    assert items_ordenados[2].producto.nombre == "Genérico"

def test_ordenar_items_por_nombre(carrito, producto_generico):
    """
    Arrange: Crear carrito, productos y agregar estos al carrito
    Act: Obtener items del carrito segun su nombre
    Assert: Se verifica el orden de cada item
    """
    # arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    producto_2 = ProductoFactory(nombre="Platano", precio=1.2)
    producto_3 = ProductoFactory(nombre="Fresa", precio=2.0)
    carrito.agregar_producto(producto_2, cantidad=2)
    carrito.agregar_producto(producto_3, cantidad=1)
    # act
    items_ordenados = carrito.obtener_items_ordenados("nombre")
    # assert
    assert items_ordenados[0].producto.nombre == "Fresa"
    assert items_ordenados[1].producto.nombre == "Genérico"
    assert items_ordenados[2].producto.nombre == "Platano"

@pytest.mark.parametrize("descuento, total_esperado", [
    (0, 100.00),     # no hay descuento
    (10, 90.00),     # 10% descuento
    (25, 75.00),     # 25% descuento
    (50, 50.00),     # 50% descuento
    (100, 0.00),     # 100% descuento
])

def test_aplicar_descuento_parametrizado(carrito, producto_generico, descuento, total_esperado):
    carrito.agregar_producto(producto_generico, cantidad=1)  # Precio 100
    total = carrito.aplicar_descuento(descuento)
    assert total == total_esperado

@pytest.mark.parametrize("nueva_cantidad, excepcion", [
    (0, False),   # Válido ya que eliminar el item
    (2, False),   # Válido: cantidad a 2
    (-1, True),   # Inválido: cantidad negativa
])
def test_actualizar_cantidad_parametrizado(carrito, producto_generico, nueva_cantidad, excepcion):
    carrito.agregar_producto(producto_generico, cantidad=1)
    if excepcion:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto_generico, nueva_cantidad)
    else:
        carrito.actualizar_cantidad(producto_generico, nueva_cantidad)
        items = carrito.obtener_items()
        if nueva_cantidad == 0:
            assert len(items) == 0
        else:
            assert items[0].cantidad == nueva_cantidad
