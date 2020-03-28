

## Usuarios (`users.py`)

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

**Ejemplo de un login simple:**

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

**Nota:**

*En la base de datos se guarda el hash de la contraseña no la contraseña como tal.
Asi que el sistema de autenticasion es seguro.*


## Base De Datos (`base.py`)

La clase `DatabaseManagementSystem` tiene *dos metodos de clase*.

- Metodo `initilize_tables()`:
    - Inicialisa o crea las tablas necesarias en la base de datos.

    - Ejemplo de como insialisar las tablas:

      ```python
      DatabaseManagementSystem.initilize_tables()
      ```

- Metodo `run_query()`:
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
