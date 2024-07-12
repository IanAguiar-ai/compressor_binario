#ifndef BITPACK_H
#define BITPACK_H

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

uint32_t pow_2(uint32_t exponent);
void compress(const uint32_t* values, size_t num_values, size_t* bit_lengths, char* buffer);
void decompress(const char* buffer, uint32_t* values, size_t num_values, size_t* bit_lengths);

#endif // BITPACK_H
