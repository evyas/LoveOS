#include <boot.h>
#include <libk.h>


static inline unsigned long long rdtsc() {
    unsigned long long int x;
    asm volatile(".byte 0x0f, 0x31"
                 : "=A"(x));
    return x;
}