# Resolución tarea técnica Product Ops
# Parte 1 - Pregunta C

En este repositorio les dejo el script para poder obtener el User según el Amount pasado como input de la función. 

Este lo encontrarán en el .py llamado find_payment_user.

# Modo de resolución

Opté por una solución sencilla, tomando el set de datos desde un archivo en local a fines de que pueda ser más rápido probar con este repo.
Luego con FastAPI, cree un endpoint para poder pasar el amount como parámetro y que este nos devuelva la el conjunto de:
{
    'amount': int ,
    'user' : str
}

# ¿Cómo probarlo?

 * En primer lugar haz un clone de el repositorio en tu computador.
 * Luego, una vez dentro del proyecto y cuando hayas activado el ambiente venv, ejecuta el comando 
 ``` uvicorn main:app --reload ```
esto levantará un servidor local para poder probarlo.
* Abre el puerto en el navegador, y podrás ver la respuesta del endopint root en tu navegador. Esto indica que el código funciona.
* Para probar conseguir un user_id, tienes que ir al path /find_user/{amount}. El parámetro amount es un entero que recibirá el Amount del payment_intent que estamos buscando. 
* Si existe uno, o más, payments_intents con ese amount serán listados en un JSON. De no exisitir ninguno, la respuesta será [].


# Mejoras posibles
* Integrar API de GSheet para poder levantar el archivo desde un file en el cloud.

