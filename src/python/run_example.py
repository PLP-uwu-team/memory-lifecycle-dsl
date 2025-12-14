import sys
import os
import subprocess
from antlr4 import CommonTokenStream, FileStream
from MemoryPolicyLexer import MemoryPolicyLexer
from MemoryPolicyParser import MemoryPolicyParser
from policy_loader import PolicyLoader

# --- 1. LOADER DSL ---
def load_policy(path):
    # Pastikan file policy ada
    if not os.path.exists(path):
        raise FileNotFoundError(f"File policy tidak ditemukan: {path}")
        
    input_stream = FileStream(path)
    lexer = MemoryPolicyLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MemoryPolicyParser(tokens)
    tree = parser.policy()

    loader = PolicyLoader()
    loader.visit(tree)
    return loader

# --- 2. VALGRIND VALIDATOR (SAFETY CHECK) ---
def check_memory_with_valgrind(executable_path, policy_pairs):
    if not os.path.exists(executable_path):
        print(f"[!] Binary '{executable_path}' not found.")
        return

    print(f"\n>> [1/2] Safety Check (Memcheck) pada: {executable_path}...")
    
    cmd = ["valgrind", "--leak-check=full", executable_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stderr

    print("-" * 50)
    # Cek 1: Memory Leak
    if "definitely lost: 0 bytes" not in output and "definitely lost:" in output:
        print("[!!!] LEAK DETECTED: Ada memori yang lupa di-free!")
    else:
        print("[OK]  No Memory Leaks detected.")

    # Cek 2: Mismatched Free
    if "Mismatched free" in output:
        print("[!!!] MISMATCH DETECTED: Pasangan Alloc/Dealloc salah!")
        print("      Cek aturan pair di policy Anda:")
        for alloc, dealloc in policy_pairs.items():
            print(f"      - {alloc} harusnya dengan {dealloc}")
    else:
        print("[OK]  Pasangan Alloc/Dealloc sesuai runtime.")
    print("-" * 50)

# --- 3. MASSIF VISUALIZER (PERFORMANCE CHECK) ---
def analyze_heap_with_massif(executable_path):
    print(f"\n>> [2/2] Visualisasi Memori (Massif)...")
    
    output_file = f"massif.out.temp"
    if os.path.exists(output_file): os.remove(output_file)

    # Jalankan Massif
    cmd = ["valgrind", "--tool=massif", f"--massif-out-file={output_file}", executable_path]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Cetak Grafik
    if os.path.exists(output_file):
        print("      Menggambar grafik penggunaan RAM...\n")
        print("=" * 50)
        # Gunakan ms_print untuk render grafik
        subprocess.run(["ms_print", output_file]) 
        print("=" * 50)
        os.remove(output_file)
    else:
        print("[!] Gagal membuat grafik Massif.")

# --- 4. MAIN EXECUTION ---
if __name__ == "__main__":
    # A. Load Policy
    try:
        policy_path = "../../examples/e1.policy"
        policy = load_policy(policy_path)
        # Ganti kode lama dengan ini:
        print("ALLOCATE:", list(policy.pairs.keys()))
        print("DEALLOCATE:", list(policy.pairs.values()))
        print("TRANSFER:", policy.transfer)
        
        print(f"--- POLICY LOADED: {policy_path} ---")
        print(f"Aturan Pasangan (Pairs):")
        for alloc, dealloc in policy.pairs.items():
            print(f"  * {alloc} -> {dealloc}")
    except Exception as e:
        print(f"Error loading policy: {e}")
        sys.exit(1)

    # B. Run Verification
    binary_target = "./test2" 
    
    # 1. Cek Safety (Leak & Mismatch)
    check_memory_with_valgrind(binary_target, policy.pairs)
    
    # 2. Cek Visual (Grafik)
    analyze_heap_with_massif(binary_target)