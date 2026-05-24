# investigacion_git.md
echo # investigacion_git.md
1. ¿Qué es el "staging area" o "índice" en Git y para qué sirve? 
Explica la diferencia entre working directory, staging area y repository ¿Por qué es útil tener esta área intermedia?

---El stagin area es tambien llamado indice en Git  es una zona intermedia donde se colocan los cambios antes de confirmarlos en el repositorio.

---Diferencias---

Working Directory : Es tener la carpèta de trabajo en el sistema de archivos.Aqui editas creas o borras archivos.-- aca editas investigacion_git.md

Staging Area : Zona intermedia donde seleccionas que cambios quieres inclcuir en el proximo commit.-- Usas git add investigacion_git.md para prepàrar ese archivo.

Repository: Es la Base de datos interna de Git donde se guardan los commits confirmados.

2. ¿Qué hace el comando git status y por qué es importante usarlo frecuentemente? Menciona al menos 3 tipos de información que proporciona

Que hace Revisa el working directory y el staging area
indica cambios pendientes.archivos nuevos.modificados o eliminados
te dice si la rama local esta sincronizada en la remota.

* Estado de la rama
* Cambios en archivos
* Mensajes de limpìeza o pendientes

3. Diferencia entre git fetch y git pull ¿Cuándo usarías uno u otro? ¿Cuál es más seguro y por qué?

La Diferencia entre git fetch y gi pull esta en como traen y aplican los cambios desde el repositorio remoto a tu repositorio local.

git fetch 

* Descarga los cambios del repositorio remoto - nuevos commits-ramas-etiquetas
* No modifican tu rama local ni tu working directory.
* Los cambios quedan disponibles en ramas remotas (ejemplo: origin/main), pero no se mezclan autormaticamente con tu rama actual.

git pùll

* Hace lo mismo que git fetch pereo ademas suiona (merge o rebase) los cambios en tu rama local.
* Modifica tu Working directory y tu historial local inmediatamente.
* Es mas rapido, ero menos seguro si no revisaste antes que cambios venian.

4. ¿Qué es un "merge conflict" y cómo se resuelve? Da un ejemplo de cuándo podría ocurrir Describe los pasos básicos para resolverlo

Un merge conflict ocurre en Git cuando dos ramas tienen cambios incompatibles en las mismas lineas de un archivo y Git no puede decidir automaticamente cual version conservar.

<<<<< HEAD
Git es un sistema de control de versiones distribuido.

Git es una herramienta para gestionar proyectos de software.

PASOS PARA RESOLVER

1- Detectar el conflicto ( git te lo indica al hacer merge y git status muestran los archivos en conflicto.)
2- Abrir el archivo afectado veras las marcas  <<<<<, ======, >>>>>
3- Editar manualmente decide que versiones conservar o combin ambas.
