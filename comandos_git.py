# Comandos para configurar nuestra identidad:

# git config --global user.name "nombre apellido"
# git config --global user.email "nombre@example.com"

# git init  Se usa una sola vez (crea capeta .git)


# Se usan cuando nosotros queramos:
# git status  Muestra el estado del repo (archivos modificados, no agregados, etc.)
# git log  Muestra el historial de commits

# Se repiten siempre que haya cambios:
# git add .  Agrega todos los archivos al repo
# git commit -m "mensaje"  Crea un commit con los archivos agregados (etiqueta de info)
# git push origin main  Sube los cambios al repositorio remoto (GitHub, GitLab, etc.)

# ramas:
# crear y movernos a rama nueva:
# git checkout -b "funciones-nuevas"

# movernos a rama existente:
# git checkout "main"

# ver ramas:
# git branch

# juntar ramas en main:
# git merge "funciones-nuevas"
