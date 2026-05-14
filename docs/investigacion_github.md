1. ¿Qué es un Pull Request (PR) y cuál es su propósito?

Un PR es ima solicitud para integrar cambios desde una rama hacia otra en un repositorio
lo cual permite revision-discusion y validadcion antes de fusionar.

¿En qué se diferencia de un merge directo?

* PR requiere revision u puede activar pruebas automaticas.
* Merge directo integra cambios sin revision ni discusion.

¿Cuáles son las ventajas de usar PRs en proyectos colaborativos?

* Mejor calidad del codigo.
* Prevencion de errores.
* Historial claro y documentado.
* Mayor seguridad.

2. ¿Qué es un fork en GitHub y cuándo se usa?

Un fork es una copia de un repositorio en tu cuenta de GiTHub y se usa para contribuir a proyectos open source sin modificar dirrectamente el repositorio original.

¿Diferencia entre fork y clone?

Fork: copia en GitHub, vinculada al repositorio original.
Clone: Copia local en tu maquina.

¿Cómo contribuirías a un proyecto open source usando fork?

 1- Hacer un fork del proyecto.
 2- Clonas tu fork en tu PC
 3- Creas una rama y aplicas cambios.
 4- Subes la rama tu fork y abres un Pulls Request al repositorio original.

3. ¿Qué es el archivo .gitignore y por qué es importante?

Lista de archivos io carpetas que Git debe ignorar.
Tambien evita subir archivos innecesarios o sensibles.

Menciona al menos 5 tipos de archivos que NO deberían subirse a un repositorio Python

__Pycache__/
Archivos .pyc
Carpeta venv/
Archivos de configuracion loca (.env)
Archivos de logs(*.log)

¿Qué problemas podrían ocurrir si no usas .gitignore?

Repositorio pesado.
Exposicion de credenciales.
Conflictos entre entornos de desarrollo.

4. ¿Qué son los issues en GitHub y para qué sirven?

Herramienta para reportar errores.proponer mejoras o discutir tareas.

¿Qué información debería contener un buen issue?

Titulo Claro.
Descripcion detallada del problema o prouesta.
Pasos para reproducri (si es un bug).
Evidencia (capturas,logs).
Etiquetas(bug, enhancement,documentacion).

¿Cómo se pueden relacionar issues con commits?

Se puede vincular usando #<numero_issue> en el mesanje del commit.

git commit -m "fix: corregir bug en login #12"

5. Investiga qué es GitHub Actions

Plataforma de automatizacion integrada en GitHub..

¿Para qué se utiliza?

Ejecuta flujos de trabajo (workflows) definidos en archivos YAML.

Menciona 2 ejemplos de tareas que podrías automatizar

Ejecutar pruebas unitarias automaticamente al hacer un commit.
Desplegar una aplicacion en un servidor o servicio cloud despues de un merge.


