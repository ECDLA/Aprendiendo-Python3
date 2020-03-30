# Documentacion:

*Documentacion del codigo escrito en este modulo. Author: JCVBS / 67*

**Advertencia:**

*COMO PRIORIDAD, ANTES DE EJECUTAR O UTILISAR CUALQUIER FUNCION, METODO O CLASE DE ESTE MODULO("db"), POR FABOR, INICIALISAR LAS TABLAS, PARA EVITAR MULTIPLES ERRORES!*

## Base De Datos (`base.py`)

La clase `DatabaseManagementSystem` se encarga de toda la administracion, gestion y manipulacion de la base de datos.
Por otra parte la clase `DatabaseManagementSystem` tiene *dos metodos de clase*.

- Metodo `initilize_tables()`:
    - Inicialisa o crea las tablas necesarias en la base de datos.

    - Ejemplo de como insialisar las tablas:

      ```python
      DatabaseManagementSystem.initilize_tables()
      ```

- Metodo `run_query()` (**Aviso:** ¡Tener cuidado al ejecutar las consultas SQL!):
    - Ejecuta una consulta SQL dada, en la base de datos.

    - Por ejemplo, si quieres hacer un consulta SQL, seria de la siguiente manera:

      ```python
      # El metodo run_query() se encargara de ejecutar la consulta, y retornara el resultado.
      DatabaseManagementSystem.run_query("SELECT * FROM users")
      ```
      
------------------

**Advertencia:**

Los metodos `initilize_tables()` y `run_query()` son metodos de 
clase (`@classmethod`), no metodos de instancia.

No es necesario crear una instancia de la clase `DatabaseManagementSystem`.

Por ejemplo esto no es necesario:

```python
# Malo
DatabaseManagementSystem().run_query(...)

# Malo 
x = DatabaseManagementSystem()
x.run_query(...)
```
Lo correcto seria asi:

```python
# Bueno
DatabaseManagementSystem.run_query(...)
```

## Usuarios (`users.py`)

La clase `User` se encargara de gestionar y manipular los usuarios.

**Crear usuarios:**

Para crear un usuario seria de la siguiente manera:
```python
User('nombre_de_usuario', 'contraseña').create_user()
```
Retorna `True` si se creo el usuario y `False` si no es asi.

Un nombre de usuario es unico, asi que si un usuario se registra 
con un nombre de usuario ya existente no podra registrarse, esa
es una razon de la cual puede retornar `False` el metodo `authenticate_user()`.

**Autenticar usuarios:**

El metodo `authenticate_user()` Autentica un usario. Ejemplo de uso:
```python
User('nombre_de_usuario', 'contraseña').authenticate_user()
```

Si el usuario escribio el usuario y contraseña correctos el metodo `authenticate_user()`
retornara `True`, caso contrario retornara `False`.

**Login simple:**

*Este es un ejemplo sencillo de un login, para que sepan como trabajar con la clase `User()`*

```python
from ... import User

username = input('Nombre de usuario:')
password = input('Contraseña:')

if User(username, password).authenticate_user():
    print('Iniciaste sesion correctamente!')
else:
    print('Nombre de usuario o contraseña incorrectos :(')
```

**Registro simple**

*Este es un ejemplo sencillo de un registro, para que sepan como trabajar con la clase `User()`*

```python
from ... import User

username = input('Nombre de usuario:')
password1 = input('Contraseña:')
password2 = input('Repite la contraseña:')

if password1 == password2 and User(username, password1).create_user():
    print('Te has registrado correctamente!')
else:
    print('Ah ocurrido un error!, lo mas probable es que utilisaste un nombre de usuario ya existente')
```

**Configuraciones de usuario:**

Cada usuario por defecto tiene una configuracion de terminal predeterminada.

- Color predeterminado de la terminal (`color`), que debe ser de tipo texto.
- Velocidad de texto predeterminada de la terminal (`text_speed`), que debe ser de tipo decimal o float.

Para cambiar los valores por defecto del color y la velocidad de texo de la terminal, hay que situarnos en el archivo `users.py`, y modificar las constantes `USER_DEFAULT_COLOR` y `USER_DEFAULT_TEXT_SPEED`, de la siguiente manera:

```python
...
USER_DEFAULT_COLOR = 'color que quiera'
USER_DEFAULT_TEXT_SPEED = 55555.0777
...
```

Para obtener la configuracion de un usuario en especifico, hay que utilisar el **metodo de instancia** `get_user_configuration()`, que retornara en un diccionario la configuracion de dicho usuario (si no existe el usuario ocurrira una excepcion o error), de la siguiente manera:

```python
>>> user = User('Juan', 'juan123')
>>> user.get_user_configuration()
{'color': 'red', 'text_speed': 5.0}
```

Para actualisar la configuracion de un usuario, hay que utilisar el **metodo de instancia** `set_user_configuration()`, que recibe como argumentos, los nuevos valores de `color` y `text_speed`, y dicho metodo retornara la nueva configuracion (si no existe el usuario ocurrira una excepcion o error), de la siguiente manera:

```python
>>> user = User('Juan', 'juan123')
>>> user.get_user_configuration()
{'color': 'red', 'text_speed': 5.0}
>>> user.set_user_configuration('cyan', 8.0)
{'color': 'cyan', 'text_speed': 8.0}
```

**Utilidades de la clase User:**

La clase `User` tiene dos **metodos de clase**, que son utilidades o se denominan asi, pues fueron creadas para eso, para ser utiles:

- Metodo `generate_password_hash()`:
    - Genera un hash de contraseña que es pasada como argumento, y la devuelve. Se puede dar una situacion que requiera generar el hash de una contraseña de un usuario.

    - Ejemplo de como usuarlo:

    ```python
    >>> User.generate_password_hash('contraseña')
    '4c882dcb24bcb1bc225391a602feca7c'
    ``` 

- Metodo `get_all_users()`:
    - Devuelve todos los usuarios registrados en la base de datos.

    - Ejmplo de como usarlo:

    ```python
    >>> User.get_all_users()
    [(1, 'nombre_de_usuario', 'contraseña'), (2, 'nombre_de_usuario2', 'contraseña2')]
        ```

----------------------

**Nota:**

*En la base de datos se guarda el hash de la contraseña no la contraseña como tal.
Asi que el sistema de autenticasion es seguro.*

*Progresivamente se estara mejorando el codigo y añadiendo mas funcionalidades. Atentamente: JCVBS / 67.*
