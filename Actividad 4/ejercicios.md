# ACTIVIDAD 4 - EJERCICIOS
## Ejercicio 1: Manejo avanzado de ramas y resolución de conflictos
Este ejercicio nos ayudará a comprender mejor las diversas acciones que se pueden hacer con las ramas, como lo son la unión, la creación o eliminación de estas. Sabemos que durante el desarrollo de un proyecto pueden ocurrir conflictos, entonces este ejercicio nos muestra claramente cómo se pueden solucionarlos.
### 1. Crear una rama para una característica:
<img src="../Imagenes/ejer1_1.jpg" width="560">

### 2. Modificar archivos en la nueva rama:
<img src="../Imagenes/ejer1_2.jpg" width="560">

### 3. Simular un desarrollo paralelo en la rama main:
<img src="../Imagenes/ejer1_3.jpg" width="560">

### 4. Intentar fusionar la rama feature/advanced-feature en main:
<img src="../Imagenes/ejer1_4.jpg" width="560">

### 5. Resolver el conflicto de fusión:
<img src="../Imagenes/ejer1_5_1.jpg" width="560">
<img src="../Imagenes/ejer1_5_2.jpg" width="560">
<img src="../Imagenes/ejer1_5_3.jpg" width="560">

### 6. Eliminar la rama fusionada:
<img src="../Imagenes/ejer1_6.jpg" width="560">

## Ejercicio 2: Exploración y manipulación del historial de commits
Este ejercicio nos permite explorar los commits y su historial, además de cómo "jugar" con estos mediante comandos. Es un ejercicio importante ya que la revisión de commits anteriores y gestionarlos es fundamental para saber como se está desarrollando el proyecto.
### 1. Ver el historial detallado de commits:
<img src="../Imagenes/ejer2_1.jpg" width="560">

**Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada uno?**

En la imagen podemos ver algunos commits que se hizo en el repositorio, los últimos commits fueron hechos en el ejercicio anterior. En la imagen podemos notar como cada commit tiene un hash diferente, además nos muestra el autor que los realizó (mi persona), la fecha y el mensaje que se pone en cada commit para indicar que se hizo.

### 2. Filtrar commits por autor:
<img src="../Imagenes/ejer2_2.jpg" width="560">

### 3. Revertir un commit:
<img src="../Imagenes/ejer2_3_1.jpg" width="560">
<img src="../Imagenes/ejer2_3_2.jpg" width="560">

### 4. Rebase interactivo:
<img src="../Imagenes/ejer2_4.jpg" width="560">

### 5. Visualización gráfica del historial:
<img src="../Imagenes/ejer2_5.jpg" width="560">

**Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?**

Debido a que se uso la opción --graph, podemos ver la lista de commits de una forma más agradable, organizada. Se observa los primeros commits que se hizo de otras actividades, también una rama distinta a main, que es advanced-feature.
Se ven varias actividade que se hicieron en el proyecto, por ejemplo actualizaciones, creaciones o eliminaciones de archivo. Por último vemos un merge, lo cual indica que hubo una unión entre dos branchs

## Ejercicio 3: Creación y gestión de ramas desde commits específicos
En este ejercicio aprenderemos a cómo crear ramas desde commits ya hechos. Esto nos ayudará a entender como funcionan las referencias en Git y a tener un mayor control en las versiones del código en nuestros proyectos a lo largo del desarrollo.
### 1. Crear una nueva rama desde un commit específico:
<img src="../Imagenes/ejer3_1.jpg" width="560">

### 2. Modificar y confirmar cambios en la nueva rama:
<img src="../Imagenes/ejer3_2.jpg" width="560">

### 3. Fusionar los cambios en la rama principal:
<img src="../Imagenes/ejer3_3.jpg" width="560">

### 4. Explorar el historial después de la fusión:
<img src="../Imagenes/ejer3_4.jpg" width="560">

### 5. Eliminar la rama bugfix/rollback-feature:
<img src="../Imagenes/ejer3_5.jpg" width="560">

## Ejercicio 4: Manipulación y restauración de commits con git reset y git restore
Este ejercicio es importante ya que comprenderemos lo importante que es deshacer cambios en nuestro proyecto. Conoceremos comandos poderosos como `git reset` o `git restore`, que nos ayudarán a corregir errores sin afectar el flujo de trabajo.
### 1. Hacer cambios en el archivo main.py:
<img src="../Imagenes/ejer4_1.jpg" width="560">

### 2. Usar git reset para deshacer el commit:
<img src="../Imagenes/ejer4_2_1.jpg" width="560">
<img src="../Imagenes/ejer4_2_2.jpg" width="560">

### 3. Usar git restore para deshacer cambios no confirmados:
<img src="../Imagenes/ejer4_3.jpg" width="560">

## Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests
Ejercicio importante ya que simularemos como si estuviéramos en una organización, viendo la colaboración en los flujos de trabajo con los branchs. Acá veremos el pull request, que son solicitudes para fusionar cambios con el branch principal.
### 1. Crear un nuevo repositorio remoto:
<img src="../Imagenes/ejer5_1.jpg" width="560">

### 2. Crear una nueva rama para desarrollo de una característica:
<img src="../Imagenes/ejer5_2.jpg" width="560">

### 3. Realizar cambios y enviar la rama al repositorio remoto:
<img src="../Imagenes/ejer5_3.jpg" width="560">

### 4. Abrir un Pull Request:
<img src="../Imagenes/ejer5_4.jpg" width="560">

### 5. Revisar y fusionar el Pull Request:
<img src="../Imagenes/ejer5_5_1.jpg" width="560">
<img src="../Imagenes/ejer5_5_2.jpg" width="560">

### 6. Eliminar la rama remota y local:
<img src="../Imagenes/ejer5_6.jpg" width="560">

## Ejercicio 6: Cherry-Picking y Git Stash
En este último ejercicio aprenderemos sobre `git cherry-pick` y cómo podemos almacenar cambios no confirmados de manera temporal.
### 1. Hacer cambios en main.py y confirmarlos:
<img src="../Imagenes/ejer6_1.jpg" width="560">

### 2. Crear una nueva rama y aplicar el commit específico:
<img src="../Imagenes/ejer6_2.jpg" width="560">

### 3. Guardar temporalmente cambios no confirmados:
<img src="../Imagenes/ejer6_3.jpg" width="560">

### 4. Aplicar los cambios guardados:
<img src="../Imagenes/ejer6_4.jpg" width="560">

### 5. Revisar el historial y confirmar la correcta aplicación de los cambios:
<img src="../Imagenes/ejer6_5.jpg" width="560">
