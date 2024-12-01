#include <iostream>
#include <vector>
#include <span>
#include <chrono> // For measuring time
#include <iomanip> // For formatting
#include <sstream>
#include <cassert>

// Dummy namespace to match the original code
namespace ml_dsa_44 {
constexpr size_t KeygenSeedByteLen = 32;
constexpr size_t PubKeyByteLen = 64;
constexpr size_t SecKeyByteLen = 64;
constexpr size_t SigningSeedByteLen = 32;
constexpr size_t SigByteLen = 128;

void keygen(std::span<const uint8_t> seed, std::span<uint8_t> pubkey, std::span<uint8_t> seckey) {
  // Simulated keygen process
  std::fill(pubkey.begin(), pubkey.end(), 0xAB); // Mock data
  std::fill(seckey.begin(), seckey.end(), 0xCD); // Mock data
}

bool sign(
  std::span<const uint8_t> rnd,
  std::span<const uint8_t> seckey,
  std::span<const uint8_t> msg,
  std::span<const uint8_t> ctx,
  std::span<uint8_t> sig
) {
  // Simulated signing process
  std::fill(sig.begin(), sig.end(), 0xEF); // Mock data
  return true;
}

bool verify(
  std::span<const uint8_t> pubkey,
  std::span<const uint8_t> msg,
  std::span<const uint8_t> ctx,
  std::span<const uint8_t> sig
) {
  // Simulated verification process
  return true;
}
} // namespace ml_dsa_44

// Helper to measure memory of a vector
template <typename T>
size_t memory_usage(const std::vector<T>& vec) {
  return vec.capacity() * sizeof(T);
}

// Helper to convert bytes to a hex string
std::string to_hex(std::span<const uint8_t> bytes) {
  std::stringstream ss;
  ss << std::hex;

  for (size_t i = 0; i < bytes.size(); i++) {
    ss << std::setw(2) << std::setfill('0') << static_cast<uint32_t>(bytes[i]);
  }

  return ss.str();
}

int main() {
  constexpr size_t mlen = 32;
  constexpr size_t ctx_len = 8;

  std::vector<uint8_t> seed(ml_dsa_44::KeygenSeedByteLen);
  std::vector<uint8_t> pubkey(ml_dsa_44::PubKeyByteLen);
  std::vector<uint8_t> seckey(ml_dsa_44::SecKeyByteLen);
  std::vector<uint8_t> rnd(ml_dsa_44::SigningSeedByteLen);
  std::vector<uint8_t> msg(mlen);
  std::vector<uint8_t> ctx(ctx_len);
  std::vector<uint8_t> sig(ml_dsa_44::SigByteLen);

  auto seed_span = std::span<uint8_t, ml_dsa_44::KeygenSeedByteLen>(seed);
  auto rnd_span = std::span<uint8_t, ml_dsa_44::SigningSeedByteLen>(rnd);
  auto msg_span = std::span(msg);
  auto ctx_span = std::span(ctx);
  auto pubkey_span = std::span<uint8_t, ml_dsa_44::PubKeyByteLen>(pubkey);
  auto seckey_span = std::span<uint8_t, ml_dsa_44::SecKeyByteLen>(seckey);
  auto sig_span = std::span<uint8_t, ml_dsa_44::SigByteLen>(sig);

  // Start tracking total memory
  size_t total_memory = 0;

  // Timing key generation
  auto start = std::chrono::high_resolution_clock::now();
  ml_dsa_44::keygen(seed_span, pubkey_span, seckey_span);
  auto end = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> elapsed = end - start;
  std::cout << "Key generation time: " << elapsed.count() << " seconds\n";

  total_memory += memory_usage(seed) + memory_usage(pubkey) + memory_usage(seckey);

  // Timing signing
  start = std::chrono::high_resolution_clock::now();
  const bool has_signed = ml_dsa_44::sign(rnd_span, seckey_span, msg_span, ctx_span, sig_span);
  end = std::chrono::high_resolution_clock::now();
  elapsed = end - start;
  std::cout << "Signing time: " << elapsed.count() << " seconds\n";

  total_memory += memory_usage(sig);

  // Timing verification
  start = std::chrono::high_resolution_clock::now();
  const bool is_valid = ml_dsa_44::verify(pubkey_span, msg_span, ctx_span, sig_span);
  end = std::chrono::high_resolution_clock::now();
  elapsed = end - start;
  std::cout << "Verification time: " << elapsed.count() << " seconds\n";

  // Display results
  std::cout << "Seed      : " << to_hex(seed_span) << "\n";
  std::cout << "Pubkey    : " << to_hex(pubkey_span) << "\n";
  std::cout << "Seckey    : " << to_hex(seckey_span) << "\n";
  std::cout << "Message   : " << to_hex(msg_span) << "\n";
  std::cout << "Context   : " << to_hex(ctx_span) << "\n";
  std::cout << "Signature : " << to_hex(sig_span) << "\n";
  std::cout << "Verified  : " << std::boolalpha << is_valid << "\n";

  std::cout << "Total memory used: " << total_memory << " bytes\n";

  assert(has_signed);
  assert(is_valid);

  return EXIT_SUCCESS;
}
