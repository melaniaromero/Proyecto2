import time
import psutil
import os
from slhdsa import KeyPair, PublicKey
from slhdsa.lowlevel.parameters import shake_256f  # Import the desired parameter set

# Function to get current memory usage in bytes
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss  # in bytes

# Measure time and memory usage for key generation
start_time = time.time()
initial_memory = get_memory_usage()  # Memory before key generation
kp = KeyPair.gen(shake_256f)  # Generate key pair
keygen_time = (time.time() - start_time) * 1_000_000  # Convert to microseconds
memory_after_keygen = get_memory_usage()  # Memory after key generation

# Measure time for signing
start_time = time.time()
sig = kp.sign(b"Hello World!")  # Sign the message
sign_time = (time.time() - start_time) * 1_000_000  # Convert to microseconds
memory_after_signing = get_memory_usage()  # Memory after signing

# Measure time for verification
start_time = time.time()
is_verified = kp.verify(b"Hello World!", sig)  # Verify the signature
verify_time = (time.time() - start_time) * 1_000_000  # Convert to microseconds
memory_after_verification = get_memory_usage()  # Memory after verification

# Get the digest of the public key
digest = kp.pub.digest()

# Reconstruct the public key using the digest
pub = PublicKey.from_digest(digest, shake_256f)

# Verify with the reconstructed public key
pub.verify(b"Hello World!", sig)

# Get final memory usage
final_memory = get_memory_usage()  # Memory after everything

# Calculate memory used during each operation
memory_used_keygen = memory_after_keygen - initial_memory
memory_used_signing = memory_after_signing - memory_after_keygen
memory_used_verification = memory_after_verification - memory_after_signing
memory_used_total = final_memory - initial_memory  # Total memory used

# Print the results
print(f"Key generation time: {keygen_time:.1f} microseconds")
print(f"Signing time: {sign_time:.1f} microseconds")
print(f"Verification time: {verify_time:.1f} microseconds")

# Hex-encoded output for seed, public key, secret key, message, context, and signature
print(f"Seed      : {digest.hex()}")
print(f"Pubkey    : {kp.pub.digest().hex()}")
print(f"Seckey    : {kp.sec.digest().hex()}")
print(f"Message   : {b'Hello World!'.hex()}")
print(f"Context   : {b'Context for verification'.hex()}")
print(f"Signature : {sig.hex()}")
print(f"Verified  : {str(is_verified).lower()}")

# Print memory usage details
print(f"Memory used during key generation: {memory_used_keygen} bytes")
print(f"Memory used during signing: {memory_used_signing} bytes")
print(f"Memory used during verification: {memory_used_verification} bytes")
print(f"Total memory used: {memory_used_total} bytes")
