#include <stdio.h>

__declspec(dllexport) int add(int a, int b) {
    return a + b;
}

__declspec(dllexport) void show_message() {
    printf("Hello from C library!\n");
}
