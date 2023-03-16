ENTRY(_start)


SECTIONS {
    . = 2M;
    KERNEL_BEGIN = .;
    
    .multiboot : ALIGN(4K) {
        *(.multiboot)
    }

    .text ALIGN(4K) : AT (ADDR(.text)) {
        *(.text)
    }

    .rodata ALIGN(4K) : AT (ADDR(.rodata)) {
        *(.rodata)
    }

    .data ALIGN(4K) : AT (ADDR(.data)) {
        *(.data)
    }
    
    .bss ALIGN(4K) : AT (ADDR(.bss)) {
        *(COMMON)
        *(.bss)
    }

	/DISCARD/ : {
		*(.note.gnu.build-id)
	}

    KERNEL_END = .; 
    KERNEL_SIZE = KERNEL_END - KERNEL_BEGIN;
}
