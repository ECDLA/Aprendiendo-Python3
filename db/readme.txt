####################
##      User      ##
####################

La clase "User":

CREAR USUARIOS:

Para crear un usuario seria de la siguiente manera:

User('nombre_de_usuario', 'contraseña').create_user()

Retorna "True" si se creo el usuario y "False" si no es asi.

Un nombre de usuario es unico, asi que si un usuario se registra 
con un nombre de usuario ya existente no podra registrarse, esa
es una razon de la cual puede retornar "False" el metodo "authenticate_user()".

AUTENTICAR USUARIOS:

El metodo "authenticate_user()" Autentica un usario. Ejemplo de uso:

User('nombre_de_usuario', 'contraseña').authenticate_user()

Si el usuario escribio el usuario y contraseña correctos el metodo "authenticate_user()"
retornara "True", caso contrario retornara "False".

NOTA:

En la base de datos se guarda el hash de la contraseña no la contraseña como tal.
Asi que el sistema de Autenticasion es seguro.

##############################
## DatabaseManagementSystem ##                     
##############################

La clase "DatabaseManagementSystem" tiene 2 metodos de clase.

initilize_tables()
    Inicialisa o crea las tablas necesarias en la base de datos.

    Ejemplo de como insialisar las tablas:

    DatabaseManagementSystem.initilize_tables()

run_query()
    Ejecuta una consulta SQL dada, en la base de datos.

    Por ejemplo, si quieres hacer un consulta SQL, seria de la siguiente manera:

    DatabaseManagementSystem.run_query("SELECT * FROM users")

    El metodo "run_query()" se encargara de ejecutar la consulta, y retornara el resultado.

ADVERTENCIA: 

Los metodos "initilize_tables()" y "run_query()" son metodos de 
clase (@classmethod), no metodos de instancia.

No es necesario crear una instancia de la clase DatabaseManagementSystem.

Por ejemplo esto no es necesario:

# Malo
DatabaseManagementSystem().run_query(...)

# Malo 
x = DatabaseManagementSystem()
x.run_query(...)

Lo correcto seria asi:

# Bueno
DatabaseManagementSystem.run_query(...)

