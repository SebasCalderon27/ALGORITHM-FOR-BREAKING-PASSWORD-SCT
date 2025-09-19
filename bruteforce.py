#importamos librerias necesarias
import time
import turtle

#definimos variables clave
intentos= 0

password= "acf5"

minusculas="abcdefghijklmnopqrstuvwxyz"
mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros="0123456789"
digitos="!#$%&/()='?¿¡*-+-.,_:;][}{}<>|°~¨"

abecedario=(mayusculas+minusculas+numeros+digitos)

encontrar=False

#creamos el cronometro
iniciar_tiempo = time.time()


#bucsar e intentar contraseñas aleatorias

def bruteforce(posible):
    global intentos, encontrar
    intentos +=1
    if posible == password:
        return posible
    
    if len(posible) < len(password):
        for letra in abecedario:
            encontrado= bruteforce(posible+letra)
            if encontrado:
                return encontrado
    return None

segura = bruteforce("")
final_tiempo =time.time() - iniciar_tiempo

if segura:
    print(f"la contraseña que se encontro fue: {segura}")
    print(f"los intentos totales fueron: {intentos}")
    print(f"el tiempo de ejecucion fue: {final_tiempo:.2f}")


if not tiempos or not contador_intentos:
    print("no existe datos para grafica")
    
else:

    pantalla = turtle.Screen()
    pantalla.title(f"Intentos vs Tiempo - Encontrado: {posible} ({intentos} intentos)")
    pantalla.setup(width=1000, height=750)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    left_margin = -450
    bottom_margin = -280
    width = 900
    height = 520

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

    maximo_tiempo = max(tiempos)
    maximo_intentos = max(contador_intentos)
    escala_x = width / maximo_tiempo if maximo_tiempo > 0 else 1
    escala_y = height / maximo_intentos if maximo_intentos > 0 else 1

    t.color("black")
    t.penup()

    for i in range(6):
        valor = (max_tiempo / 5) * i
        x = left_margin + valor * escala_x
        t.goto(x, bottom_margin - 10)
        t.write(f"{valor:.2f}", align="center", font=("Calibri", 8, "normal"))
        t.goto(x, bottom_margin)
        t.pendown()
        t.goto(x, bottom_margin + 6)
        t.penup()

    for i in range(6):
        valor = (max_intentos / 5) * i
        y = bottom_margin + valor * escala_y
        t.goto(left_margin - 8, y - 4)
        t.write(f"{int(valor)}", align="right", font=("Arial", 8, "normal"))
        t.goto(left_margin, y)
        t.pendown()
        t.goto(left_margin + 6, y)
        t.penup()

    t.goto(left_margin + width / 2, bottom_margin - 40)
    t.write("Tiempo que transcurrio", align="center", font=("Calibri", 10, "bold"))
    t.goto(left_margin - 60, bottom_margin + height / 2)
    t.write("Intentos", align="center", font=("Calibri", 10, "bold"))

    t.color("blue")
    t.penup()
    for i in range(len(tiempos)):
        x = left_margin + tiempos[i] * escala_x
        y = bottom_margin + contador_intentos[i] * escala_y
        t.goto(x, y)
        if i == 0:
            t.pendown()

    if posible:
        t.color("red")
        t.goto(left_margin + tiempos[-1] * escala_x, bottom_margin + contador_intentos[-1] * escala_y)
        t.dot(10)
        t.penup()
        t.goto(left_margin + tiempos[-1] * escala_x + 12, bottom_margin + contador_intentos[-1] * escala_y + 6)
        t.write(f"{posible} ({intentos} intentos, {tiempo_total:.4f}s)", font=("Calibri", 9, "normal"))

    pantalla.mainloop()
