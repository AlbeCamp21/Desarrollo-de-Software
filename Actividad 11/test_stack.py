from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def setUp(self) -> None:
        """Configuración antes de cada prueba."""
        self.stack = Stack()

    def tearDown(self) -> None:
        """Limpieza después de cada prueba."""
        self.stack = None

    def test_is_empty(self) -> None:
        stack = Stack()
        assert stack.is_empty() == True
        stack.push(5)
        assert stack.is_empty() == False
        
    def test_peek():
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.peek() == 2
        
    def test_peek(self):
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        
    def test_pop():
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.peek() == 1
    
    def test_pop(self):
        self.stack.push(3)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        
    def test_push():
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
    
    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
