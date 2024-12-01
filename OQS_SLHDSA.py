import time
import tracemalloc  # Seguimiento de memoria
import oqs  # Librería para algoritmos de criptografía post-cuántica

# Inicialización de OQS para SPHINCS+
algorithm = "SPHINCS+-sha256-256f-robust"  # Esquema de firma post-cuántica
sig = oqs.Signature(algorithm)

# Inicialización del seguimiento de memoria
tracemalloc.start()

# Generación de claves
start = time.time()
public_key = sig.generate_keypair()
private_key = sig.export_secret_key()
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Tiempo generación de claves ({algorithm}):", end - start, "segundos")
print(f"Memoria actual: {current / 1024:.2f} KB; Pico de memoria: {peak / 1024:.2f} KB")

# Firma
message = b"Prueba de firma post-cuántica"  # Mensaje en formato bytes
start = time.time()
signature = sig.sign(message)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Tiempo de firma ({algorithm}):", end - start, "segundos")
print(f"Memoria actual: {current / 1024:.2f} KB; Pico de memoria: {peak / 1024:.2f} KB")

# Verificación
start = time.time()
is_valid = sig.verify(message, signature, public_key)
end = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Tiempo de verificación ({algorithm}):", end - start, "segundos")
print(f"Memoria actual: {current / 1024:.2f} KB; Pico de memoria: {peak / 1024:.2f} KB")
print(f"Firma válida ({algorithm}):", is_valid)

# Detener el seguimiento de memoria
tracemalloc.stop()

# Limpieza
sig.close()
