
# INFORME - ACTIVIDAD 2

## 1. Importancia de IaC

### 1.1. Agilidad acelerada:
* IaC permite la creación rápida de entornos de desarrollo, pruebas y producción. Esto reduce notoriamente los tempos de espera y potencia el ciclo de vida del software.
* La capacidad de abastecer infraestructura dependiendo de la demanda facilita el desarrollo y la administración, esenciales para las metodologías ágiles.

### 1.2. Consistencia y reducción de errores:
* Al definir la infraestructura en código, se elimina la inestabilidad y los errores humanos que puede originar la configuración manual. Esto asegura la igualdad de los entornos en toda etapa del desarrollo.

### 1.3. Colaboración y control de versiones:
* IaC fomenta la colaboración entre equipos de desarrollo y operaciones (DevOps), ya que todos trabajan con el mismo código-infraestructura.
* El control de versiones de la infraestructura permite seguir los cambios, chequear quién los realizó y revertir a versiones anteriores si es necesario.

### 1.4. Automatización y eficiencia:
* La automatización del suministro y la configuración de la infraestructura hace que los equipos dejen de lado las tareas manuales y repetitivas.
* Esto optimiza la eficiencia, reduce los costos y permite a los equipos centrarse en tareas de mayor relevancia.

### 1.5. Recuperación ante desastres:
* IaC facilita la recuperación rápida de la infraestructura en caso de errores, ya que los entornos se pueden recrear automáticamente y fácilmente a partir del código.


## 2. Importancia de Contenedores

### 2.1. Portabilidad y consistencia:
* Los contenedores nos aseguran que las aplicaciones funcionen de manera sólida en cualquier entorno, desde el inicio (desarrollo) hasta el final (producción).
* Estos contenedores eliminan el típico problema de "funcionaba en mi máquina", simplificando el despliegue en diferentes plataformas y nubes.

### 2.2. Eficiencia y escalabilidad:
* Los contenedores optimizan el uso de recursos, ya que solo consumen los recursos que se necesitan en el momento.
* La capacidad de la escalabilidad horizontal de los contenedores permite a las aplicaciones adaptarse a las variaciones en la demanda, garantizando un rendimiento óptimo.

### 2.3. Microservicios y desarrollo ágil:
* Los contenedores son perfectos para la arquitectura de micro servicios, ya que permiten empaquetar y desplegar cada servicio de forma independiente.
* El desarrollo ágil se simplifica con este método, ya que los equipos pueden trabajar simultáneamente en diferentes partes sin interferir entre si, lanzando nuevas funciones con mayor rapidez.

### 2.4. Aislamiento y seguridad:
* Los contenedores brindan un alto nivel de aislamiento, lo que evita que las aplicaciones interfieran entre sí, mejorando la seguridad.

### 2.5. Integración continua:
* Los contenedores van perfectamente de la mano con los procesos de integración continua (CI), facilitando la automatización de las pruebas y la creación de imágenes de contenedores.
 

## 3. Importancia de Kubernetes

### 3.1. Orquestación y automatización:
* Kubernetes automatiza el despliegue, el escalado y la gestión de aplicaciones dentro de contenedores, liberando a los equipos de tareas manuales y complicadas.
* Todo esto permite la entrega del software más rápida y eficiente.

### 3.2. Alta disponibilidad y resiliencia:
* Kubernetes asegura que las aplicaciones sigan disponibles cuando se reparten los contenedores entre varios nodos, y reiniciar de forma automática los contenedores fallidos.
* Su arquitectura flexible con los fallos reduce el tiempo de inactividad, garantizando una experiencia agradable y consistente al usuario.

### 3.3. Escalabilidad dinámica:
* Kubernetes brinda la capacidad de escalar las aplicaciones de forma automática y dinámica dependiendo de la demanda.
* Esto garantiza que las aplicaciones puedan manejar altas cantidades de tráfico y mantener un rendimiento óptimo.

### 3.4. Gestión de microservicios:
* Kubernetes facilita la gestión de arquitecturas basadas en microservicios, permitiendo la gestión eficiente de aplicaciones complicadas, asegurando estabilidad y optimizando los recursos disponibles.

### 3.5. Abstracción de la infraestructura:
* Kubernetes "oculta" la complejidad de la infraestructura subyacente, lo que permite a los desarrolladores enfocarse en escribir y mejorar el código de la aplicación en lugar de preocuparse en otros temas, como la gestión de servidores o redes.


## 4. Importancia de Observabilidad

### 4.1. Detección y resolución de problemas:
* La observabilidad es un método para detectar y diagnosticar problemas de rendimiento y errores en tiempo real.
* Como ventaja tenemos la reducción en el tiempo de resolución de incidentes y la mejora en la confiabilidad del software.

### 4.2. Optimización del rendimiento:
* La observabilidad brinda una visión profunda del rendimiento tanto de las aplicaciones como de la infraestructura.
* Esto permite detectar cuellos de botella y optimizar el rendimiento para mejorar la experiencia del usuario.

### 4.3. Mejora continua:
* Los datos obtenidos gracias a la observabilidad proporcionan información importante para entender el comportamiento de las aplicaciones que están en producción.
* Esto beneficia a los equipos de desarrollo, ya que les permite tomar decisiones informadas sobre futuras mejoras y nuevas funciones.

### 4.4. Comprensión de sistemas complejos:
* En los entornos de microservicios, la observabilidad es fundamental para comprender como fluyen las solicitudes a través de los diferentes servicios. Esto asegura que la comunicación entre componentes sea confiable y eficaz.


## 5. Importancia de CI/CD

### 5.1. Automatización y velocidad:
* El proceso de entrega de software se automatiza gracias al CI/CD, aplicándolo desde la integración del código hasta el despliegue en producción.
* CI/CD acelera el ciclo de entrega y permite lanzar nuevas versiones de software con mayor frecuencia y confiabilidad.

### 5.2. Calidad y confiabilidad:
* Aplicar CI/CD en el proyecto es incluir pruebas automatizadas en cada etapa del flujo de trabajo, garantizando la calidad y la confiabilidad del software.
* Esto reduce los errores y mejora la confianza en el software entregado para las partes interesadas.

### 5.3. Entrega continua:
* La entrega continua permite el lanzamiento de nuevas versiones de software con mayor frecuencia y confianza.
* Esto trae como ventaja que las organizaciones puedan adaptarse rápidamente a los cambios del mercado y a las necesidades de los usuarios.

### 5.4. Reducción de riesgos:
* Al automatizar las pruebas y los despliegues con CI/CD, se reduce el riesgo de errores humanos y problemas en producción gracias a las pipelines que se aplican.

### 5.5. Retroalimentación temprana:
* CI/CD proporciona retroalimentación inmediata a los desarrolladores, lo que les permite corregir errores, agilizar las mejoras sin perder la calidad del software.
