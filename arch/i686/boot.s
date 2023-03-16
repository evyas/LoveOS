# 32х битный код
.code32
# Размер стека
# 4096 * 16 * 8 = 524288 байт. 
# 524288 байт = 512 килобайт
# 4 * 16 = 64 килобайт. 
.set STACK_SIZE, 1024 * 4

# Multiboot флаги
# Multiboot константы
.set MB_MAGIC, 0x1BADB002
.set MB_FLAGS, (1 << 0) | (1 << 1) | (1<<2)
.set MB_CHECKSUM, (0 - (MB_MAGIC + MB_FLAGS))

# Объявляем мультизагрузочный заголовок, который помечает программу как ядро.
# Это магические значения, которые задокументированы в стандарте мультизагрузки.
# Загрузчик будет искать этот заголовок в первых 8 килобайтах файла ядра, выровненного по 32-битной границе.
# Подпись находится в отдельном разделе, поэтому заголовок можно принудительно разместить в первых 8 килобайтах файла ядра.
.section .multiboot, "aw"
multiboot_start:
    .align 4
    .long MB_MAGIC
    .long MB_FLAGS
    .long MB_CHECKSUM
    .long 0, 0, 0, 0, 0
    .long 0
    .long 1024, 768, 32
multiboot_end:
 
.section .bss
    .align 16
    stack_bottom:
        .skip STACK_SIZE 
    stack_top:


.section .text
.global _start
_start:
    cli
    finit
    mov $stack_top, %esp
    push %ebx
    call hal_init
_fuckup:
    cli
    hlt
    jmp _fuckup

.comm _stack, STACK_SIZE
