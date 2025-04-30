from behave import given, when, then
sys.path.append("..")
from src.autenticador import autenticar
import re

@given(re.compile(r'el usuario "(?P<user>[^"]+)" con contraseña "(?P<passwd>[^"]+)"'))
def step_user(context, user, passwd):
    context.user = user
    context.passwd = passwd

@when('intenta iniciar sesión')
def step_try(context):
    context.result = autenticar(context.user, context.passwd)

@then(r'debe ver "(?P<msg>[^"]+)"')
def step_verify(context, msg):
    assert context.result == msg
