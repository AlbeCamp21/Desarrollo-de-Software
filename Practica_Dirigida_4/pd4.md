# Testing y Devops con principios SOLID

## Nivel Teórico

### 1. Clasificación de Responsabilidades
- *Contexto:* El módulo `services.py` concentra orquestación de pagos.
- *Enunciado:* Señala cuatro responsabilidades concretas de `PaymentService`. Indica cuáles serían candidatas a extraerse a nuevos "policies" u "object collaborators" para reforzar SRP sin romper LSP.
- *Aceptación:* ensayo de 400 palabras; menciona qué fixtures habría que crear para las nuevas clases.

**Resolución**
Los mocks nos permiten simular objetos que imitan métodos reales. Si bien el nombre del método está mal escrito, el mock puede invocarlo y aplicar lógica personalizada, generando la ilusión de que se está ejecutando el comportamiento verdadero. Esto nos ayuda a mantener la coherencia funcional en los tests.


### 5. Ventajas y riesgos de monkeypatch
- *Enunciado:* contrapón en 300 palabras setter-like vs constructor-like.
- *Aceptación:* lista de "casos de uso apropiados" y "smells" para cada estilo.

**Resolución**
##### Setter-like (parcheo directo)
a) Casos de uso apropiados:
-   Parcheo temporal de métodos de terceros.
-   Simulación de errores en funciones concretas, como interrupciones de red.

b) Code Smells:
-   Parcheo extensivo que vuelve frágiles los tests.
-   Dependencia de nombres internos no públicos.
    

##### Constructor-like (inyección de dependencias)
a) Casos de uso apropiados:
-   Uso con arquitecturas basadas en interfaces.
-   Facilita reemplazo de componentes mediante mocks o fakes.

b) Code Smells:
-   Parámetros agregados solo para testear.
-   Constructores inflados con muchas dependencias.

## Nivel implementación, código y fixtures
### 6. Fixture condicional por entorno
   *Objetivo:* permitir que los mismos tests usen `DummyGateway` localmente y un gateway real en integración.
   *Tareas:*
- Leer la variable de entorno `USE_REAL_GATEWAY`.
- Si está activa, crear el gateway real (puede ser un stub que simule latencia).
- Ajustar `conftest.py` para registrar la nueva fixture con prioridad.
*Aceptación:* `pytest -m "not slow"` corre en < 1 s; `pytest -m slow` tarda ≥ 0.5 s por la latencia simulada.
```python
# conftest.py

@pytest.fixture
def payment_gateway():
    if os.getenv("USE_REAL_GATEWAY") == "1":
        class RealGatewayWithDelay(RealGateway):
            def charge(self, customer_id, total):
                time.sleep(0.6)
                return super().charge(customer_id, total)
        return RealGatewayWithDelay()
    return MockGateway()
```

### 7. Custom marker `@pytest.mark.contract`
   *Objetivo:* señalar tests que verifiquen invariantes de dominio (p. ej. "no se persiste un `Payment` sin usuario").
   *Tareas:*
   - Definir marcador en `pytest.ini`.
   -  Etiquetar dos casos.
   -  Añadir a CI un paso "contract" que solo ejecute esos tests.
      *Aceptación:* salida de `pytest -m contract` muestra exactamente 2 tests.

```python
# test_payments.py
import pytest

@pytest.mark.contract
def test_payment_requires_user():
    # Para asegurar que no se permita guardar pagos sin usuario

@pytest.mark.contract
def test_user_balance_must_not_be_negative():
    # Para asegurar que no se acepte un saldo negativo

# Ejemplo de step en CI
- name: Ejecutar pruebas contract
  run: pytest -m contract
```

### 9. Property-based testing con Hypothesis
   *Objetivo:* generar montos aleatorios positivos y verificar que siempre se persiste el pago.
   *Tareas:*
- Añadir `hypothesis` a `requirements.txt` (sin romper velocidad de suite).
- Crear `test_payment_property.py`.
      *Aceptación:* la prueba se ejecuta en < 1 s con 100 ejemplos.

```python
# test_payment_property.py
from hypothesis import given, strategies as st

def test_payment_persists_any_positive_amount(payment_service):
    @given(st.decimals(min_value=0.01, max_value=1000))
    def inner(amount):
        result = payment_service.process_payment("Alem", amount)
        assert result
    inner()
```
  
