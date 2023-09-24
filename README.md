# ## Login con Flask, Python y Mysql

Este proyecto demuestra cómo crear un sistema de inicio de sesión básico utilizando Flask, Python y MySQL, aplicando conceptos como restricción de rutas, gestión de sesiones y cierre de sesión. Todo esto se logra mediante el uso del microframework Flask y otras bibliotecas relacionadas.




## Deployment

Para comenzar, sigue estos pasos después de clonar el repositorio y verificar que tienes Python instalado:

1. Abre una terminal PowerShell o CMD en la carpeta del proyecto y ejecuta el siguiente comando para crear un entorno virtual dentro del proyecto:

```bash
  python -m virtualenv env

```


2. Luego, activa el entorno virtual con el siguiente comando:


```bash
  .\env\Scripts\activate
```
Si ves en tu terminal algo similar a lo siguiente, significa que el entorno virtual se ha activado correctamente:

```bash
  (env) PS C:\Users\myuser\Python\lf2\login-flask-mysql> 
```
3. Instala la principal biblioteca requerida con el siguiente comando:

```bash
  pip install flask
```

4. Después, verifica las bibliotecas instaladas con el siguiente comando y compara la lista con la captura de pantalla para asegurarte de que todas las bibliotecas necesarias estén presentes:

```bash
  pip list
```

![App Screenshot](https://lsabun.com/images/piplist.jpeg)

Si falta alguna biblioteca, instálala manualmente con el comando pip install seguido del nombre de la biblioteca.

```bash
  pip install Flask-Login Flask-WTF python-dotenv python-decouple
```
## Variables de entorno

Luego de que tengas todas las librerias instaladas (verificado con el comando pip list) debes configurar las variables de entorno, en el archivo .env2 se muestras las variables necesarias para la ejecucion del programa

`MYSQL_HOST`: La dirección del servidor MySQL.

`MYSQL_USER`: El nombre de usuario de MySQL.

`MYSQL_PASSWORD`: La contraseña de MySQL.

`MYSQL_DB`: El nombre de la base de datos de MySQL.

`SECRET_KEY`: Una clave secreta utilizada para codificar un token y validar el formulario de inicio de sesión.




## Soporte

Para obtener soporte, puedes enviar un correo electrónico a viagramo2011@gmail.com.


## Authors

- [@GitHub de farkot09](https://github.com/farkot09)

