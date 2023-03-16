#include <boot.h>
#include <libk.h>


uint32_t *framebuffer_addr;
uint32_t framebuffer_pitch;
uint32_t framebuffer_width;
uint32_t framebuffer_height;
extern KERNEL_END;


void hal_hlt() {
    asm volatile("hlt");
}


static void multiboot_main(multiboot_info_t *info) {
    multiboot_module_t *start = (multiboot_module_t*)info->mods_addr;

    if (start) {
        for (uint32_t i = 0; i < info->mods_count; i++) {
        }
    }
}


void hal_init(multiboot_info_t *ebx) {
    // Тут менеджер же надо инитить?
    //mm_init(KERNEL_END);
    
    // Настраиваем FPU
    //asm volatile("fldcw %0;"::"m"((uint16_t)0x37F)); 

    framebuffer_addr = (uint32_t*)ebx->framebuffer_addr;
    framebuffer_pitch = ebx->framebuffer_pitch;
    framebuffer_width = ebx->framebuffer_width;
    framebuffer_height = ebx->framebuffer_height;

    uint8_t n = 255;
    // Эвя, это не нормально
    for (size_t y = 0; y < framebuffer_height; y++) {
        for (size_t x = 0; x < framebuffer_width; x++) {
            framebuffer_addr[x + y * (framebuffer_pitch / 4)] =  ((0xB0B0B0 - (x * y + 1) * 255) & 0xFEFEFE) >> 1;
        }
    }


    multiboot_main(ebx);
    kernel_main();
}