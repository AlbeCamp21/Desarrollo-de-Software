# ACTIVIDAD 5 - CASOS Y EJERCICIOS
## Caso 1: Fusión Fast-forward
Aplicando los comandos en la actividad:

<img src="../Imagenes/act5/ejem1_1.jpg" width="560">
<img src="../Imagenes/act5/ejem1_2.jpg" width="560">

**Pregunta:** Muestra la estructura de commits resultante.

<img src="../Imagenes/act5/ejem1_3.jpg" width="560">

**Resultado:** Ahora, veamos la lista de commits después de aplicar merge:

<img src="../Imagenes/act5/ejem1_4.jpg" width="560">

## Caso 2: Fusión No-fast-forward
Aplicando los comandos en la actividad:

<img src="../Imagenes/act5/ejem2_1.jpg" width="560">
<img src="../Imagenes/act5/ejem2_2.jpg" width="560">

**Pregunta:** Muestra el log de commits resultante.

<img src="../Imagenes/act5/ejem2_3.jpg" width="560">

**Resultado:** Después de la edición, veamos el log ahora:

<img src="../Imagenes/act5/ejem2_4.jpg" width="560">

## Caso 3: Fusión squash
Aplicando los comandos en la actividad:

<img src="../Imagenes/act5/ejem3_1.jpg" width="560">
<img src="../Imagenes/act5/ejem3_2.jpg" width="560">
<img src="../Imagenes/act5/ejem3_3.jpg" width="560">

**Pregunta:** ¿Cuál es tu estructura de commits?.

<img src="../Imagenes/act5/ejem3_4.jpg" width="560">

**Resultado:** Luego de hacer la fusión squash, obtenemos:

<img src="../Imagenes/act5/ejem3_5.jpg" width="560">

## Ejercicio 1: Clona un repositorio Git con múltiples ramas
Identifica dos ramas que puedas fusionar utilizando `git merge --ff`.

<img src="../Imagenes/act5/ejer1_1.jpg" width="560">

Haz el proceso de fusión utilizando `git merge --ff`.

<img src="../Imagenes/act5/ejer1_2.jpg" width="560">

Verifica el historial con `git log --graph --oneline`

<img src="../Imagenes/act5/ejer1_3.jpg" width="560">

**Pregunta:** ¿En qué situaciones recomendarías evitar el uso de `git merge --ff`? Reflexiona sobre las desventajas de este método.

El uso de `git merge --ff` recomiendo evitar cuando se quiere mantener un historial claro, sobretodo cuando se trabajo en equipos. Este tipo de merge no genera un commit de combinación, entonces puede hacer que el historial de commits sea confusa al no quedar registrado la fusión de ramas. Ademá, se hace más complicado cuando se quiere revertir cambios de un branch completo.

## Ejercicio 2: Simula un flujo de trabajo de equipo
Trabaja en dos ramas independientes, creando diferentes cambios en cada una.

<img src="../Imagenes/act5/ejer2_1.jpg" width="560">

Fusiona ambas ramas con `git merge --no-ff` para ver cómo se crean los commits de fusión.

<img src="../Imagenes/act5/ejer2_2.jpg" width="560">

Observa el historial utilizando `git logo --graph --oneline`

<img src="../Imagenes/act5/ejer2_3.jpg" width="560">

**Pregunta:** ¿Cuáles son la principales ventajas de utilizar `git merge --no-ff` en un proyecto en equipo? ¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?

Usar este tipo de merge en un proyecto en equipo nos da la ventaja de mantener un historial claro, mostrando datos importantes como el momento cuando se integró un branch, haciendo más fácil la revisión o el revertimiento de cambios.
El problema que puede provocar esto es que el historial se puede llenar de merges irrelevantes, volviéndose más complicado de leerlas si se abusa de este tipo.


## Ejercicio 3: Crea múltiples commits en una rama
Haz varios cambios y commits en una rama feature.

<img src="../Imagenes/act5/ejer3_1.jpg" width="560">

Fusiona la rama con `git merge --squash` para aplanar todos los commits en uno solo.

<img src="../Imagenes/act5/ejer3_2.jpg" width="560">

Verifica el historial de commits antes y después de la fusión para ver la diferencia.

<img src="../Imagenes/act5/ejer3_3.jpg" width="560">

**Pregunta:** ¿Cuándo es recomendable utilizar una fusión squash? ¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?

Se recomienda usar el merge squash cuando se quiere hacer fusiones de una rama con commits pequeños, como por ejemplo commits experimentales, queriendo resumir todo eso en un solo commit. A diferencia de los otros tipos de merge, el squash no ayuda a evitar rellenar el historial con datos innecesarios, facilitando la revisión del proyecto.

## Caso 4: Resolver conflictos en una fusión non-fast-forward
1. Crea un archivo index.html y realiza un commit en la rama main.

<img src="../Imagenes/act5/ejem4_1.jpg" width="560">

2. Crea y cambia a una nueva rama para luego editar el archivo y realizar un commit.

<img src="../Imagenes/act5/ejem4_2.jpg" width="560">

3. Regresa a la rama main y realiza una edición en el mismo archivo.

<img src="../Imagenes/act5/ejem4_3.jpg" width="560">

4. Fusiona la rama feature-update con --no-ff y observa el conflicto.

<img src="../Imagenes/act5/ejem4_4.jpg" width="560">

5. Edita el archivo para eliminar el conflicto y haz commit.

<img src="../Imagenes/act5/ejem4_5.jpg" width="560">

6. Verifica el historial para confirmar la fusión y el commit de resolución de conflicto.

<img src="../Imagenes/act5/ejem4_6.jpg" width="560">

**Preguntas:**
- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?
klklklklk
- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?
jjkljljk

## Ejercicio 4: Comparar los historiales con git log después de diferentes fusiones
1. Crea un nuevo repositorio y realiza varios commits en dos rama.

<img src="../Imagenes/act5/ejer4_1.jpg" width="560">
<img src="../Imagenes/act5/ejer4_2.jpg" width="560">

2. Fusiona feature-1 usando fast-forward.

<img src="../Imagenes/act5/ejer4_3.jpg" width="560">

3. Fusiona feature-2 usando non-fast-forward.

<img src="../Imagenes/act5/ejer4_4.jpg" width="560">

4. Realiza una nueva rama feature-3 con múltiples commits y fusiónala con squash.

<img src="../Imagenes/act5/ejer4_5.jpg" width="560">
<img src="../Imagenes/act5/ejer4_6.jpg" width="560">

5. Compara el historial de Git

<img src="../Imagenes/act5/ejer4_7.jpg" width="560">

**Preguntas:**
- ¿Cómo se ve el historial en cada tipo de fusión?
klklklklk
- ¿Qué método prefieres en diferentes escenarios y por qué?
jjkljljk

## Ejercicio 5: Usando fusiones automáticas y revertir fusiones
1. Inicializa un nuevo repositorio y realiza dos commits en main.

<img src="../Imagenes/act5/ejer5_1.jpg" width="560">

2. Crea una nueva rama auto-merge y realiza otro commit en file.txt.

<img src="../Imagenes/act5/ejer5_2.jpg" width="560">

3. Vuelve a main y realiza cambios no conflictivos en otra parte del archivo.

<img src="../Imagenes/act5/ejer5_3.jpg" width="560">

4. Fusiona la rama auto-merge con main.

<img src="../Imagenes/act5/ejer5_4.jpg" width="560">

5. Revertir la fusión: Si decides que la fusión fue un error, puedes revertirla. Luego, verifica el historial.

<img src="../Imagenes/act5/ejer5_5.jpg" width="560">

**Preguntas:**
- ¿Cuándo usarías un comando como git revert para deshacer una fusión?
Usaría dicho comando para revertir una fusión de una rama con la principal, revirtiendo esos cambios sin borrarlos del historial. En casos colaborativos es muy útil cuando el merge ya se ha compartido con otras personas.
- ¿Qué tan útil es la función de fusión automática en Git?
Es muy útil ya que resuelve la gran mayoría de conflictos de forma inteligente, su utilidad aumenta en proyectos grandes donde hay muchos colaboradores. Sin embargo, hay casos donde aún se necesitará intervención manual.

## Ejercicio 6: Fusión remota en un repositorio colaborativo
1. Clona un repositorio remoto desde GitHub o crea uno nuevo.

<img src="../Imagenes/act5/ejer6_1.jpg" width="560">

2. Crea una nueva rama de colaboración y haz algunos cambios.

<img src="../Imagenes/act5/ejer6_2.jpg" width="560">

3. Empuja los cambio a la rama remota.

<img src="../Imagenes/act5/ejer6_3.jpg" width="560">

4. Simula una fusión desde la rama colaboración en la rama main de otro colaborador. (Puedes usar la interfaz de GitHub para crear un Pull Request y realizar la fusión).

<img src="../Imagenes/act5/ejer6_4.jpg" width="560">
<img src="../Imagenes/act5/ejer6_5.jpg" width="560">
<img src="../Imagenes/act5/ejer6_6.jpg" width="560">

**Preguntas:**
- ¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?
Cuando se colabora con otras persona en un repositorio, el uso de Pull Request se vuelve fundamental para revisar y sobretodo discutir los cambios que se hacen. También, al colaborar, se debe mantener un historial ordenado, por lo que una buena idea es usar No-fast-forward o squash.
- ¿Qué problemas comunes pueden surgir al integrar ramas remotas?
Al usar ramas remota pueden aparecer conflictos si varias personas modifican las mismas líneas de código. Otro problema común es que alguien se olvide de hacer push, causando falla en la sincronización.
