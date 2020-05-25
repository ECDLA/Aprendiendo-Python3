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

Cada usuario por defecto tiene una configuracion de terminal predeterminada:

- `animation` (integer)
- `flicker` (string)

Para cambiar los valores por defecto o la configuracion predeterminada de **todos** los usuarios hay que situarnos en el archivo `settings.py`, y modificar las constantes `USER_DEFAULT_COLOR` y `USER_DEFAULT_TEXT_SPEED`, de la siguiente manera:

```python
...
# Warning!: integer values only!, valid values: 0, 12
USER_DEFAULT_ANIMATION = 12

# Warning: string value only!, valid values: 'A_BLINK', 'A_STANDOUT'
USER_DEFAULT_FLICKER = 'A_BLINK'
...
```

> **IMPORTANTE:** 
>
> El archivo `settings.py`, es la configuracion del modulo **db**, en general. 
>
> Se creo dicho archivo para poder configurar de manera mas sencilla el modulo, evitando asi ver todo el codigo o el funcionamiento por detras de dicho modulo.

-------------

**¿Como accedemos a la configuracion del usuario?**

Para acceder a la configuracion del usuario, seria mendiante los siguientes atributos de la instancia:

- `animation_config` -> configuracion de la animacion del usuario
- `flicker_config` -> configuracion del parpadeo del usuario

Un ejemplo:

```python
>>> user = User('Juan', 'juan123')
>>> user.animation_config
12
>>> user.flicker_config
524288
>>> import curses
>>> curses.A_BLINK
524288 # user.flicker_config es igual a curses.A_BLINK
```

Para actualisar la configuracion de un usuario, hay que simplemente modificar los atributos mencionados, de la siguiente manera:

```python
>>> user = User('Juan', 'juan123')
>>> user.animation_config
12
>>> user.animation_config = 0
>>> user.animation_config
0
```

En cuanto al `flicker` es diferente:
```python
>>> user = User('Juan', 'juan123')
>>> import curses
>>> user.flicker_config == curses.A_BLINK
True
>>> user.flicker_config = 'A_STANDOUT'
>>> user.flicker_config == curses.A_STANDOUT
True
>>> user.flicker_config
65536
```

Son atributos normales y corrientes, asi de simple...

----------

> **ADVERTENCIA:**
>
> Dicha implementacion se logro mediante **descriptores de datos**, cada ves que se accede o modifica un atributo, se estan haciendo consultas SQL a la base de datos. Entonces, no abusen y accedan como locos a los atributos pues estan haciendo consultas SQL a lo loco, y puede afectar el redimiento de la aplicasion. Cabe recalcar que dudo que pase esto pero si el cliente tiene una maquina lenta puede afectar.

------------

**Utilidades de la clase User:**

La clase `User` tiene dos **metodos de clase**, que son utilidades o se denominan asi, pues fueron creadas para eso, para ser utiles:

- Metodo `generate_password_hash()`:
    - Genera un hash de contraseña que es pasada como argumento, y la devuelve. Se puede dar una situacion que requiera generar el hash de una contraseña de un usuario.

    - Ejemplo de como usuarlo:

    ```python
    >>> User.generate_password_hash('contraseña')
    '4c882dcb24bcb1bc225391a602feca7c'
    ```

----------------------

**Nota:**

*En la base de datos se guarda el hash de la contraseña no la contraseña como tal.
Asi que el sistema de autenticasion es seguro.*

*Progresivamente se estara mejorando el codigo y añadiendo mas funcionalidades. Atentamente: JCVBS / 67.*
