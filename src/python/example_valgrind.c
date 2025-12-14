#include <stdlib.h>
#include <stdio.h>

// Anggap ini fungsi yang Anda daftarkan di DSL sebagai "allocate_by"
void* my_alloc(size_t size) {
    return malloc(size);
}

// Anggap ini fungsi yang Anda daftarkan di DSL sebagai "deallocate_by"
void my_free(void* ptr) {
    free(ptr);
}

int main(int argc, char* argv[]) {
    printf("Running victim program...\n");

    // Skenario 1: Alokasi tapi LUPA di-free (LEAK!)
    void* p1 = my_alloc(100);

    // Skenario 2: Alokasi dan di-free (AMAN)
    void* p2 = my_alloc(50);

    // Kita sengaja tidak mem-free p1 untuk memancing Valgrind
    return 0;
}
