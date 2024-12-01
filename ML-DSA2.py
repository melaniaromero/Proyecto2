import oqs
import time
import tracemalloc
from pprint import pprint

# Función para iniciar el seguimiento de la memoria
def start_memory_tracking():
    tracemalloc.start()  # Inicia el seguimiento de la memoria

# Función para obtener el uso de memoria actual
def get_current_memory():
    current, peak = tracemalloc.get_traced_memory()  # Obtiene la memoria actual y el uso máximo
    return current, peak

# Medición de tiempo y memoria
start_time = time.time()  # Comienza a medir el tiempo
start_memory_tracking()  # Inicia el seguimiento de la memoria

print("liboqs version:", oqs.oqs_version())
print("liboqs-python version:", oqs.oqs_python_version())
print("Enabled signature mechanisms:")
sigs = oqs.get_enabled_sig_mechanisms()
pprint(sigs, compact=True)

message = "This is the message to sign".encode()

# Crear el firmante y verificador con el mecanismo de firma seleccionado
sigalg = "ML-DSA-65"
with oqs.Signature(sigalg) as signer:
    with oqs.Signature(sigalg) as verifier:
        print("\nSignature details:")
        pprint(signer.details)

        # Firmante genera su par de claves
        signer_public_key = signer.generate_keypair()

        # Firmante firma el mensaje
        signature = signer.sign(message)

        # Verificador verifica la firma
        is_valid = verifier.verify(message, signature, signer_public_key)

        print("\nValid signature?", is_valid)

# Medición de tiempo y memoria después de la ejecución
end_time = time.time()  # Finaliza la medición del tiempo
current_memory, peak_memory = get_current_memory()  # Obtiene el uso de memoria actual

# Cálculos de tiempo
execution_time = end_time - start_time

print("\nTiempo de ejecución: {:.4f} segundos".format(execution_time))
print("Uso de memoria actual: {:.2f} MB".format(current_memory / (1024 * 1024)))  # Convierte a MB
print("Uso máximo de memoria: {:.2f} MB".format(peak_memory / (1024 * 1024)))  # Convierte a MB

# Detiene el seguimiento de la memoria
tracemalloc.stop()
