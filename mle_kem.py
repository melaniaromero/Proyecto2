# Key encapsulation Python example with benchmarking and memory usage
import oqs
from pprint import pprint
import time
import tracemalloc

print("liboqs version:", oqs.oqs_version())
print("liboqs-python version:", oqs.oqs_python_version())
print("Enabled KEM mechanisms:")
kems = oqs.get_enabled_kem_mechanisms()
pprint(kems, compact=True)

# Create client and server with sample KEM mechanism
kemalg = "Kyber512"
with oqs.KeyEncapsulation(kemalg) as client:
    with oqs.KeyEncapsulation(kemalg) as server:
        print("\nKey encapsulation details:")
        pprint(client.details)

        # Start tracking memory usage
        tracemalloc.start()

        # Benchmark key pair generation
        start_time = time.time()
        public_key_client = client.generate_keypair()
        end_time = time.time()
        print(f"Keypair generation time: {end_time - start_time:.6f} seconds")

        # Memory usage for key pair generation
        current, peak = tracemalloc.get_traced_memory()
        print(f"Memory usage after keypair generation: Current={current / 10**6:.6f} MB, Peak={peak / 10**6:.6f} MB")

        # Benchmark encapsulation
        start_time = time.time()
        ciphertext, shared_secret_server = server.encap_secret(public_key_client)
        end_time = time.time()
        print(f"Encapsulation time: {end_time - start_time:.6f} seconds")

        # Memory usage for encapsulation
        current, peak = tracemalloc.get_traced_memory()
        print(f"Memory usage after encapsulation: Current={current / 10**6:.6f} MB, Peak={peak / 10**6:.6f} MB")

        # Benchmark decapsulation
        start_time = time.time()
        shared_secret_client = client.decap_secret(ciphertext)
        end_time = time.time()
        print(f"Decapsulation time: {end_time - start_time:.6f} seconds")

        # Memory usage for decapsulation
        current, peak = tracemalloc.get_traced_memory()
        print(f"Memory usage after decapsulation: Current={current / 10**6:.6f} MB, Peak={peak / 10**6:.6f} MB")

        # Stop tracking memory
        tracemalloc.stop()

        # Validate shared secrets
        print("\nShared secrets coincide:", shared_secret_client == shared_secret_server)
