import subprocess
import sys
import os

def check_memory_with_valgrind(executable_path):
    """
    Menjalankan executable dengan Valgrind dan mengecek apakah ada leak.
    """
    
    # Cek apakah file executable ada
    if not os.path.exists(executable_path):
        print(f"[ERROR] File '{executable_path}' tidak ditemukan.")
        return

    print(f"--- [ANALISIS DINAMIS] Memeriksa: {executable_path} ---")

    # Command untuk menjalankan Valgrind
    # --error-exitcode=42 : Ini triknya! Jika Valgrind nemu error, dia akan return code 42.
    # --leak-check=full   : Cek memory leak secara menyeluruh.
    valgrind_cmd = [
        "valgrind",
        "--leak-check=full",
        "--error-exitcode=42", 
        "./" + executable_path
    ]

    try:
        # Jalankan subprocess
        # capture_output=True agar output Valgrind tidak langsung nyampur ke terminal
        result = subprocess.run(
            valgrind_cmd, 
            capture_output=True, 
            text=True
        )

        # Cek Return Code
        if result.returncode == 42:
            print("\n[!!!] HASIL: VALGRIND MENEMUKAN MEMORY LEAK!")
            print("------------------------------------------------")
            # Tampilkan output error dari Valgrind (biasanya ada di stderr)
            print(extract_summary(result.stderr))
            print("------------------------------------------------")
            print("Kesimpulan: Aturan DSL Anda harusnya mendeteksi ini sebagai ERROR.")
            
        elif result.returncode == 0:
            print("\n[OK] HASIL: Program Aman (Clean).")
            print("Kesimpulan: Valgrind tidak menemukan masalah.")
            
        else:
            # Error lain (misal program crash / segfault)
            print(f"\n[ERROR] Program crash dengan return code: {result.returncode}")
            print(result.stderr)

    except FileNotFoundError:
        print("[ERROR] Valgrind tidak terinstall di sistem ini (WSL).")

def extract_summary(valgrind_output):
    """
    Hanya mengambil bagian 'HEAP SUMMARY' dan 'ERROR SUMMARY' biar rapi.
    """
    lines = valgrind_output.splitlines()
    summary = []
    capture = False
    for line in lines:
        if "HEAP SUMMARY" in line:
            capture = True
        if capture:
            summary.append(line)
    return "\n".join(summary)

if __name__ == "__main__":
    # Ganti ini dengan nama binary hasil compile Anda
    target_program = "example_valgrind" 
    check_memory_with_valgrind(target_program)