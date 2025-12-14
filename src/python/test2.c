
#include <stdio.h>
#include <stdlib.h>

/* =========================
   GLOBAL STORAGE (TRANSFER TARGET)
   ========================= */

typedef struct Node {
    int value;
    struct Node* next;
} Node;

static Node* global_list = NULL;

/* =========================
   ALLOCATION
   ========================= */

void* my_alloc(size_t size) {
    return malloc(size);
}

/* =========================
   DEALLOCATION
   ========================= */

void my_free(void* ptr) {
    free(ptr);
}

/* =========================
   TRANSFER OWNERSHIP
   ========================= */

void StorePointerInGlobalList(void* ptr) {
    Node* n = (Node*)ptr;
    n->next = global_list;
    global_list = n;
}

/* =========================
   NORMAL FLOW: ALLOC + FREE
   ========================= */

void process_and_free(int x) {
    Node* n = (Node*)my_alloc(sizeof(Node));
    n->value = x;

    /* ownership stays here */
    my_free(n);
}

/* =========================
   TRANSFER FLOW: ALLOC + TRANSFER
   ========================= */

void process_and_store(int x) {
    Node* n = (Node*)my_alloc(sizeof(Node));
    n->value = x;

    /* ownership transferred */
    StorePointerInGlobalList(n);
}

/* =========================
   GLOBAL CLEANUP (OPTIONAL)
   ========================= */

void cleanup_global_list() {
    Node* cur = global_list;
    while (cur) {
        Node* next = cur->next;
        free(cur);
        cur = next;
    }
    global_list = NULL;
}

/* =========================
   ENTRY POINT
   ========================= */

int main() {
    process_and_free(10);     // SAFE
    process_and_store(20);    // OWNERSHIP TRANSFERRED
    process_and_store(30);    // OWNERSHIP TRANSFERRED

    /* program ends without calling cleanup_global_list */
    return 0;
}
