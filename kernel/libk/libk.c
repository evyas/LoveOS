#include <libk.h>


uint32_t strlen(const char *string) {
    uint32_t length = 0;

    while (string[length]) {
        length++;
    }

    return length;
}

int pow(int x, unsigned int y) {
    if (y == 0) {
        return 1;
    } else {
        if (y % 2 == 0) {
            return pow(x, y / 2) * pow(x, y / 2);
        }
    } 
    
    return x * pow(x, y);
}
