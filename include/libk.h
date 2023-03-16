#ifndef __LIBK_H
#define __LIBK_H 1

#define NULL ((void *)0)
#define LLONG_MAX     9223372036854775807
#define LLONG_MIN   (-9223372036854775807 - 1)
#define true 1
#define false 0
#define va_start(v, l) __builtin_va_start(v, l)
#define va_end(v) __builtin_va_end(v)
#define va_arg(v, l) __builtin_va_arg(v, l)
#define va_copy(d, s) __builtin_va_copy(d, s)
typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int uint32_t;
typedef  int int32_t;
typedef unsigned long long uint64_t;
typedef uint32_t size_t;
typedef uint32_t uintptr_t;
typedef _Bool bool;
typedef __builtin_va_list va_list;

#endif // libk.h