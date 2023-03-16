#ifndef __ARCH_H
#define __ARCH_H 1

#include <libk.h>

void      hal_hlt();
void      hal_int_on();
void      hal_int_off();
void      hal_task_on();
void      hal_task_off();
uint32_t *hal_get_framebuffer();



#endif // arch.h