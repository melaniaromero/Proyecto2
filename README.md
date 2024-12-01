# Post-Quantum Cryptography: ML-DSA, ML-KEM, and SLH-DSA Implementations

This repository contains implementations of **ML-DSA Signature Scheme**, **ML-KEM Key Encapsulation Mechanism**, and **SLH-DSA Signature Scheme**. These algorithms are part of the post-quantum cryptographic field and are designed to provide security against potential quantum computer attacks. They are alternative cryptographic schemes that are considered secure even in the presence of quantum computers.

## Algorithms Implemented

The repository includes the following post-quantum cryptographic schemes:

### 1. **ML-DSA (Multivariate Lattice Digital Signature Algorithm)**

ML-DSA is a digital signature scheme based on multivariate polynomials over lattices. It offers quantum-resistant security, making it a promising candidate for future-proof digital signatures. The scheme includes key generation, signing, and verification algorithms.

### 2. **ML-KEM (Multivariate Lattice Key Encapsulation Mechanism)**

ML-KEM is a key encapsulation mechanism that relies on the hardness of multivariate polynomial problems over lattices. It is used to securely exchange cryptographic keys in a post-quantum context. The scheme includes key encapsulation and decapsulation operations.

### 3. **SLH-DSA (Syndrome-LWE-based Digital Signature Algorithm)**

SLH-DSA is a digital signature scheme based on the Syndrome-LWE (Learning With Errors) problem, which is a well-studied problem in lattice-based cryptography. It provides security against quantum computers and is suitable for scenarios requiring digital signatures.

Each algorithm is implemented to allow for testing, benchmarking, and comparison of their performance and security features.

## Installation

Follow the steps below to set up and run the code locally:

### Prerequisites

- **Java** (JDK 11 or newer) and **Python** (for Python-based implementations).
- **pip** (for Python) to manage dependencies.


### Clone the Repository

```bash
git clone https://github.com/melaniaromero/Proyecto2.git
