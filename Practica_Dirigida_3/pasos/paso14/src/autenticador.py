
def autenticar(user, passwd):
    usuarios = {
        "alice": "secret1"
    }
    if user in usuarios and usuarios[user] == passwd:
        return f"Bienvenido, {user}"
    return "Datos inválidos"

