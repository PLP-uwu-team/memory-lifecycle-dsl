#include <stdlib.h>
#include <stdio.h>
#include <string.h> // Untuk memset

#define NUM_BLOCKS 10
#define BLOCK_SIZE 500000 // 500KB

// Fungsi untuk membuang waktu CPU (agar grafik melebar ke samping)
void burn_cpu_cycles() {
    volatile int sum = 0; // 'volatile' agar tidak dihapus compiler
    for (int i = 0; i < 5000000; i++) {
        sum += i;
    }
}

int main() {
    int* ptrs[NUM_BLOCKS];

    printf("--- [START] Demo Alokasi Memori ---\n");

    // FASE 1: Alokasi Bertahap (Grafik NAIK)
    printf(">> Mengalokasikan memori...\n");
    for (int i = 0; i < NUM_BLOCKS; i++) {
        // 1. Alokasi
        ptrs[i] = malloc(BLOCK_SIZE);
        
        // 2. Isi memori (Penting agar Massif mencatat ini sebagai 'Useful Heap')
        if (ptrs[i] != NULL) {
            memset(ptrs[i], 0, BLOCK_SIZE);
        }

        // 3. Buang waktu sedikit agar grafik tidak tegak lurus
        burn_cpu_cycles();
        
        printf("   + Blok %d dialokasikan (%d KB)\n", i+1, (BLOCK_SIZE * (i+1)) / 1024);
    }

    // FASE 2: Puncak (Peak)
    printf(">> Puncak Penggunaan Memori tercapai.\n");
    burn_cpu_cycles(); // Tahan sebentar di puncak

// FASE 3: Dealokasi Bertahap (Grafik TURUN)
    printf(">> Membersihkan memori...\n");
    for (int i = 0; i < NUM_BLOCKS; i++) {
        // Skenario: Lupa free blok terakhir
        if (i == NUM_BLOCKS - 1) {
            printf("   ! OOPS: Sengaja lupa free blok terakhir (untuk pancing error)\n");
            continue; 
        }

        free(ptrs[i]);
        burn_cpu_cycles(); 
        printf("   - Blok %d dibebaskan\n", i+1);
    }

    printf("--- [END] Selesai ---\n");
    return 0;
}