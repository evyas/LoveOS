#include <arch.h>


void kernel_main() {

    for (;;) {
        hal_hlt();
    }
}