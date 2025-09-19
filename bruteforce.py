#importamos librerias necesarias
import time
import turtle

# variables clave (sin cambios)
intentos = 0
password = "abc"

minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
digitos = "!#$%&/()='?¿¡*-+-.,_:;][}{}<>|°~¨"

abecedario = mayusculas + minusculas + numeros + digitos

# listas para graficar tiempos transcurridos y contador de intentos en cada prueba
tiempos = []
contador_intentos = []

# cronometro
iniciar_tiempo = time.time()

# búsqueda por fuerza bruta 
def bruteforce(posible):
    global intentos

    intentos += 1
    elapsed = time.time() - iniciar_tiempo
    tiempos.append(elapsed)
    contador_intentos.append(intentos)

    if posible == password:
        return posible

    if len(posible) < len(password):
        for letra in abecedario:
            encontrado = bruteforce(posible + letra)
            if encontrado:
                return encontrado
    return None

# ejecutar bruteforce
encontrada = bruteforce("")

final_tiempo = time.time() - iniciar_tiempo

if encontrada:
    print(f"La contraseña que se encontró fue: {encontrada}")
    print(f"Los intentos totales fueron: {intentos}")
    print(f"El tiempo de ejecución fue: {final_tiempo:.4f} segundos")
else:
    print("No se encontró la contraseña.")

# Si no hay datos suficientes para graficar, avisamos
if not tiempos or not contador_intentos:
    print("No existen datos para graficar.")
else:

    # --- gráfica adaptada del segundo script, usando las variables del primer script ---
    pantalla = turtle.Screen()
    pantalla.title(f"Intentos vs Tiempo - Encontrado: {encontrada} ({intentos} intentos)")
    pantalla.setup(width=1000, height=650)  # match second script height

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    left_margin = -450
    bottom_margin = -280
    width = 900
    height = 520

    # ejes
    t.penup()
    t.goto(left_margin, bottom_margin)
    t.pendown()
    t.forward(width)
    t.penup()
    t.goto(left_margin, bottom_margin)
    t.left(90)
    t.pendown()
    t.forward(height)
    t.penup()

    # escalas (nombres iguales a los del segundo script: max_tiempo, max_intentos)
    max_tiempo = max(tiempos)
    max_intentos = max(contador_intentos)
    escala_x = width / max_tiempo if max_tiempo > 0 else 1
    escala_y = height / max_intentos if max_intentos > 0 else 1

    t.color("black")
    t.penup()

    # marcas en eje x (tiempo) — fuente Arial como en el segundo script
    for i in range(6):
        valor = (max_tiempo / 5) * i
        x = left_margin + valor * escala_x
        t.goto(x, bottom_margin - 10)
        t.write(f"{valor:.2f}", align="center", font=("Arial", 8, "normal"))
        t.goto(x, bottom_margin)
        t.pendown()
        t.goto(x, bottom_margin + 6)
        t.penup()

    # marcas en eje y (intentos)
    for i in range(6):
        valor = (max_intentos / 5) * i
        y = bottom_margin + valor * escala_y
        t.goto(left_margin - 8, y - 4)
        t.write(f"{int(valor)}", align="right", font=("Arial", 8, "normal"))
        t.goto(left_margin, y)
        t.pendown()
        t.goto(left_margin + 6, y)
        t.penup()

    # títulos ejes (igual al segundo script)
    t.goto(left_margin + width / 2, bottom_margin - 40)
    t.write("Tiempo transcurrido (s)", align="center", font=("Arial", 10, "bold"))
    t.goto(left_margin - 60, bottom_margin + height / 2)
    t.write("Intentos", align="center", font=("Arial", 10, "bold"))

    # dibujar curva (tiempos vs intentos) en azul — comportamiento como el segundo script
    t.color("blue")
    t.penup()
    for i in range(len(tiempos)):
        x = left_margin + tiempos[i] * escala_x
        y = bottom_margin + contador_intentos[i] * escala_y
        t.goto(x, y)
        if i == 0:
            t.pendown()
        else:
            t.pendown()
            t.goto(x, y)
        t.penup()

    # marcar punto final (si encontrada)
    if encontrada:
        t.color("red")
        x_final = left_margin + tiempos[-1] * escala_x
        y_final = bottom_margin + contador_intentos[-1] * escala_y
        t.goto(x_final, y_final)
        t.dot(10)
        t.penup()
        t.goto(x_final + 12, y_final + 6)
        t.write(f"{encontrada} ({intentos} intentos, {final_tiempo:.4f}s)", font=("Arial", 9, "normal"))

    pantalla.mainloop()
