import pytest
from src.shopping_cart import ShoppingCart
from unittest.mock import Mock

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"apple": {"quantity": 2, "unit_price": 0.5}}
    
def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # aniade item manzana
    cart.remove_item("apple")  # quita item manzana
    assert cart.items == {}
    
def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # agrega item apple
    cart.add_item("banana", 3, 0.75)  # agrega item banana
    total = cart.calculate_total()  # calcula el total
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25
    
def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # agrega item apple
    cart.add_item("banana", 3, 0.75)  # agrega item banana
    cart.apply_discount(10)  # Descuento del 10%
    total = cart.calculate_total()
    expected_total = (2*0.5 + 3*0.75) * 0.9  # Aplicando 10% de descuento
    assert total == round(expected_total, 2)
    
def test_process_payment():
    payment_gateway = Mock()  # para simular gateway de pago externo
    payment_gateway.process_payment.return_value = True  # siempre devuelve true
    
    cart = ShoppingCart(payment_gateway=payment_gateway)
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)
    
    total = cart.calculate_total()
    result = cart.process_payment(total)
    
    payment_gateway.process_payment.assert_called_once_with(total)  # verifica que se llama al metodo con el monto
    assert result == True
