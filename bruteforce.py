#importamos librerias necesarias
import time

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
    print(f"el tiempo de ejecucion fue: {final_tiempo}")
