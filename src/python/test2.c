#include <stdio.h>
#include <stdlib.h>
#include <string.h> // Tambahan untuk memset

/* =========================
   BAGIAN 1: LOGIKA ASLI ANDA (JANGAN DIHAPUS)
   ========================= */

typedef struct Node {
    int value;
    struct Node* next;
} Node;

static Node* global_list = NULL;

void* my_alloc(size_t size) {
    return malloc(size);
}

void my_free(void* ptr) {
    free(ptr);
}

void StorePointerInGlobalList(void* ptr) {
    Node* n = (Node*)ptr;
    n->next = global_list;
    global_list = n;
}

void process_and_free(int x) {
    Node* n = (Node*)my_alloc(sizeof(Node));
    n->value = x;
    my_free(n);
}

void process_and_store(int x) {
    Node* n = (Node*)my_alloc(sizeof(Node));
    n->value = x;
    StorePointerInGlobalList(n);
}

/* =========================
   BAGIAN 2: TAMBAHAN VISUALISASI (MASSIF DEMO)
   ========================= */
// Fungsi ini ditambahkan agar grafiknya terlihat naik-turun cantik

#define DEMO_BLOCKS 10
#define DEMO_SIZE 500000 // 500KB

void burn_cpu_cycles() {
    volatile int sum = 0; 
    for (int i = 0; i < 3000000; i++) sum += i; // Loop berat untuk delay
}

void run_visual_demo_spike() {
    printf("\n--- [START] Visual Demo (Massif Spike) ---\n");
    int* ptrs[DEMO_BLOCKS];

    // GRAFIK NAIK
    for(int i=0; i<DEMO_BLOCKS; i++) {
        ptrs[i] = malloc(DEMO_SIZE);
        if(ptrs[i]) memset(ptrs[i], 0, DEMO_SIZE); // Pakai memori fisik
        burn_cpu_cycles();
    }
    
    printf(">> Puncak Memori Tercapai (Lihat Puncak Grafik)\n");
    burn_cpu_cycles();

    // GRAFIK TURUN
    for(int i=0; i<DEMO_BLOCKS; i++) {
        free(ptrs[i]);
        burn_cpu_cycles();
    }
    printf("--- [END] Visual Demo Selesai ---\n");
}

/* =========================
   ENTRY POINT
   ========================= */

int main() {
    // 1. Jalankan Logika Bisnis Asli (Cepat, grafik datar)
    printf(">> Menjalankan Logika Linked List...\n");
    process_and_free(10);     
    process_and_store(20);    
    process_and_store(30);    

    // 2. Jalankan Demo Visualisasi (Lambat, grafik gunung)
    run_visual_demo_spike();

    /* Program berakhir tanpa cleanup global_list (LEAK disengaja dari logika asli) */
    return 0;
}