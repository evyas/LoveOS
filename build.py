#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Сборщик ядра LoveOS

(c) Эвелина Миронова и Арен Елчинян
"""


import os
import glob
import shutil
import argparse
import shutil


SRC_TARGETS = []
BIN_TARGETS = []
LIMINE_DEPLOY = "limine-deploy"


def exec_cmd(cmd):
    print(cmd)
    if os.system(cmd) != 0:
        exit(1)


def build_all(ARCH):
    CC = f"{ARCH}-elf-gcc"  #  -march=i586
    LD = f"{ARCH}-elf-ld"  #  -march=i586
    CC_PROTECT = "-mno-sse -ffreestanding -fno-stack-protector -nostdlib -w"
    CC_FLAGS = f"{CC_PROTECT} -I include// -I arch//{ARCH}//inc// -c "

    LD_FLAGS = f"-T arch//{ARCH}//link.ld -nostdlib -O0 "


    files = glob.glob(f"arch//{ARCH}//**//*.s", recursive=True) + \
            glob.glob(f"arch//{ARCH}//**//*.c", recursive=True) + \
            glob.glob("kernel//**//*.c", recursive=True)

    for i in range(len(files)):
        SRC_TARGETS.append(files[i])
        BIN_TARGETS.append(os.path.join("bin//kernel//", os.path.basename(SRC_TARGETS[i]) + '.o '))

    shutil.rmtree("bin", ignore_errors=True)

    if not os.path.exists("isodir/user/"):
        os.mkdir("isodir/user/")

    if not os.path.exists("bin/"):
        os.mkdir("bin/")

    if not os.path.exists("bin/kernel/"):
        os.mkdir("bin/kernel/")

    for i in range(0, len(SRC_TARGETS)):
        exec_cmd(f"{CC} {CC_FLAGS} {SRC_TARGETS[i]} -o {BIN_TARGETS[i]}")
    
    #BIN_TARGETS.append("bin//font_psf.o")

    #exec_cmd(f"{LD} -r -b binary -o bin//font_psf.o kernel/src/graf/font.psf")
    exec_cmd(f"{CC} {LD_FLAGS} -o isodir//kernel.elf {' '.join(str(x) for x in BIN_TARGETS)}")
    

    pass


''' Сборка ISO '''
def build_iso():
    print("Сборка ISO")
    LIMINE_LIST = [
        "BOOTIA32.EFI", "BOOTX64.EFI", "limine-cd-efi.bin", 
        "limine.sys", "limine-cd.bin"
    ]

    if not os.path.exists("isodir/limine-cd.bin"):
        os.system(
                "git clone https://github.com/limine-bootloader/limine.git" \
                " --branch=v3.0-branch-binary" \
                " --depth=1")
        for i in LIMINE_LIST:
            shutil.copy(f"limine/{i}", "isodir/")
    
    exec_cmd("""xorriso -as mkisofs -b limine-cd.bin \
          -no-emul-boot -boot-load-size 4 -boot-info-table \
          --efi-boot limine-cd-efi.bin \
          -efi-boot-part --efi-boot-image --protective-msdos-label \
          isodir -o LoveOS.iso""")
    
    os.system(f"{LIMINE_DEPLOY} LoveOS.iso")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SynapseOS build helper')
    parser.add_argument('-arch',   help='build with generate docs(doxygen)')
    parser.add_argument('-noqemu',   help='build with generate docs(doxygen)')
    args = parser.parse_args()

    if args.arch != None:
        build_all(args.arch)
    else:
        build_all("i686")

    build_iso()

    if args.noqemu == 0 or args.noqemu == None:
        if args.arch == "i686":
            QEMU_DEV = "-device rtl8139,id=nic0"
            QEMU = f"qemu-system-i386 -m 128 -d guest_errors -no-reboot -hda hda.img"

            if not os.path.exists("hda.img"):
                exec_cmd("qemu-img create hda.img 2M")
            exec_cmd(f"{QEMU} -monitor stdio -cdrom LoveOS.iso -serial file:serial.log")
