El script comienza preparando contadores y dos listas para guardar cuánto tiempo ha pasado y cuántos intentos se hicieron, 
luego lanza una función recursiva que prueba combinacione, en cada llamada suma un intento, registra el tiempo transcurrido 
y comprueba si la cadena probada es la contraseña, ssi no lo es y todavía falta longitud por añadir, intenta añadir cada carácter
del alfabeto y vuelve a probar, cuando termina muestra en la consola si encontró la contraseña, cuántos intentos hizo y cuánto 
duró todo, si se almacenaron datos, dibuja con turtle una gráfica que muestra cómo fueron aumentando los intentos en función del 
tiempo y marca en rojo el punto donde se encontró la contraseña.

Qué hace el script?

Prepara contadores y dos listas vacías: una para los tiempos y otra para los intentos.

Lanza la función de fuerza bruta que construye cadenas poco a poco.

En cada intento: aumenta el contador y guarda el tiempo que ha pasado desde el inicio.

Comprueba si la cadena actual coincide con la contraseña; si sí, para y devuelve el resultado.

Si la cadena aún es más corta que la contraseña, añade cada carácter posible y prueba de nuevo (recursión).

Al acabar, imprime en pantalla la contraseña encontrada, el número total de intentos y el tiempo total.

Por ultimo si hay datos, crea una gráfica con turtle que muestra la relación Intentos vs Tiempo y marca en rojo el punto final.

Caso 1 — contraseña corta (ej. "abc"):
La contraseña que se encontró fue: abc
Los intentos totales fueron: 1543
El tiempo de ejecución fue: 0.3154 segundos

Reflexión: ¿qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?
Si la contraseña tiene 8 o más caracteres y usa mayúsculas, números y símbolos, el número de combinaciones posibles crece de forma exponencial
y el tiempo para romperla con fuerza bruta puede ser de años o siglos, dependiendo de la velocidad de los intentos, esto muestra por qué las contraseñas largas y variadas son mucho más seguras frente a este tipo de ataques.
