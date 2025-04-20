import pytest
from user_management.user_manager import UserManager
from unittest.mock import MagicMock

class FakeHashService:
    """
    Servicio 'fake' que devuelve un hash simplificado con un prefijo, y lo verifica.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "albecamp"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
    
def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)  # se agrega el usuario

    # Act
    autenticado = manager.authenticate_user(username, password)  # verifica las credenciales

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)
    
class InMemoryUserRepository:
    """Fake de repositorio en memoria."""
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_pw):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_pw

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)  # inyectamos el repo
    username = "fakeUser"
    password = "fakePass"

    manager.add_user(username, password)
    assert manager.user_exists(username)
    
def test_envio_correo_bienvenida_al_agregar_usuario():
    from unittest.mock import MagicMock

    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)
