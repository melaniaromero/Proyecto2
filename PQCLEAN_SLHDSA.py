import time
import tracemalloc
from pqclean.dilithium2 import generate_keypair, sign, verify                                                                                                   # type: ignore

def measure_memory_and_time(operation_name, operation, *args):
    """Función para medir tiempo y memoria de una operación."""
    tracemalloc.start()
    start_time = time.time()
    result = operation(*args)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"{operation_name} - Tiempo: {end_time - start_time:.6f} segundos")
    print(f"{operation_name} - Memoria actual: {current / 1024:.2f} KB; Pico de memoria: {peak / 1024:.2f} KB")
    return result

def main():
    # Generación de claves
    print("Generando claves...")
    public_key, private_key = measure_memory_and_time("Generación de claves", generate_keypair)

    # Mensaje a firmar
    message = "Prueba de firma post-cuántica"

    # Firma
    print("\nFirmando mensaje...")
    signature = measure_memory_and_time("Firma", sign, message, private_key)

    # Verificación
    print("\nVerificando firma...")
    is_valid = measure_memory_and_time("Verificación", verify, message, signature, public_key)

    print(f"\nResultado de la verificación: {'Válida' if is_valid else 'Inválida'}")

if __name__ == "__main__":
    main()

