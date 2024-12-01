# Importación de módulos necesarios
from lattice_cryptography.lm_one_time_sigs import *  # Importa las funciones necesarias de la librería de criptografía de retículas
from timeit import default_timer  # Importa el temporizador para medir el tiempo de ejecución

# Definición de un conjunto de cadenas con diferentes letras del alfabeto
arr = 'abcdefghijklmnopqrstuvwxyz'  # Una cadena con el alfabeto en minúsculas
cadenas = []  # Lista vacía para almacenar las cadenas generadas

# Generación de cadenas repetidas para cada letra del alfabeto
for letter in arr:
    tmp = ''  # Inicializa una cadena vacía temporal
    for i in range(15):  # Repite 15 veces la letra
        tmp += letter  # Agrega la letra a la cadena temporal
    cadenas.append(tmp)  # Añade la cadena generada a la lista 'cadenas'

# Inicialización de las variables para medir el tiempo total de firma y verificación
timeFirma = 0  # Variable para almacenar el tiempo total de la firma
timeVerificacion = 0  # Variable para almacenar el tiempo total de la verificación

# Función que realiza la firma y verificación usando el esquema ML-DSA
def MLDSAdifr(mensaje):
    # 'mensaje' es la entrada que será firmada y verificada (cadena de texto)

    message: str = mensaje  # Se asegura que 'mensaje' sea de tipo str (cadena)

    # Generación de parámetros públicos para el sistema de criptografía
    public_parameters = make_setup_parameters(secpar=256)  # Genera parámetros públicos con un nivel de seguridad de 256 bits

    # Generación de las claves pública y privada para la firma
    secret_seed, signing_key, verification_key = keygen(pp=public_parameters, num_keys_to_gen=1)[0]  # Se generan las claves necesarias

    # Medición del tiempo de la firma
    tInit = default_timer()  # Inicia el temporizador antes de firmar
    signature = sign(pp=public_parameters, otk=(secret_seed, signing_key, verification_key), msg=message)  # Se firma el mensaje
    tFin = default_timer()  # Detiene el temporizador después de firmar
    timeFirma = tFin - tInit  # Calcula el tiempo de la firma

    # Intento de verificar la firma generada
    try:
        tInit = default_timer()  # Inicia el temporizador antes de verificar
        verify(pp=public_parameters, otvk=verification_key, sig=signature, msg=message)  # Se verifica la firma
        tFin = default_timer()  # Detiene el temporizador después de verificar
        timeVerificacion = tFin - tInit  # Calcula el tiempo de la verificación
    except (ValueError):  # Si la verificación falla, maneja la excepción
        timeVerificacion = tFin - tInit  # (Aunque no se debe llegar aquí si todo va bien)
    
    return timeFirma, timeVerificacion  # Devuelve los tiempos de firma y verificación

# Bucle que recorre todas las cadenas generadas
for cadena in cadenas:
    # Llama a la función MLDSAdifr para cada mensaje en 'cadenas'
    time_tmp1, time_tmp2 = MLDSAdifr(cadena)  # Obtiene los tiempos de firma y verificación para la cadena actual

    # Suma los tiempos de firma y verificación
    timeFirma += time_tmp1
    timeVerificacion += time_tmp2

# Cálculo y despliegue del tiempo promedio de firma y verificación
print('Tiempo promedio de Firma con ML-DSA', timeFirma / len(arr))  # Tiempo promedio de firma
print('Tiempo promedio de Verificacion con ML-DSA', timeVerificacion / len(arr))  # Tiempo promedio de verificación


