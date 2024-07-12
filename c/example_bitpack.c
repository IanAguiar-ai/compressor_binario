//Dependencias:

#include "bitpack.h"

//------------------------------------------------------------------------------------------
//Exemplo:

int main() {
    // Lista de valores e seus comprimentos em bits
    uint32_t values[] = {6, 7, 140, 15};
    size_t bit_lengths[] = {3, 3, 8, 4};
    size_t num_values = sizeof(values)/sizeof(values[0]);

    // Calcula o comprimento total da string binária
    size_t total_bit_length = 0;
    for (size_t i = 0; i < num_values; ++i) {
        total_bit_length += bit_lengths[i];
    }

    // Aloca memória para a string binária
    char* bin_string = (char*)malloc(total_bit_length + 1);  // +1 para o terminador nulo

    // Converte a lista de inteiros para a string binária
    compress(values, num_values, bit_lengths, bin_string);

    // Exibe a string binária resultante
    printf("String binária: %s\n", bin_string);

    // Aloca memória para a lista de inteiros descomprimida
    uint32_t* decompressed_values = (uint32_t*)malloc(num_values * sizeof(uint32_t));

    // Converte a string binária de volta para a lista de inteiros
    decompress(bin_string, decompressed_values, num_values, bit_lengths);

    // Exibe os valores descomprimidos
    printf("Valores descomprimidos:\n");
    for (size_t i = 0; i < num_values; ++i) {
        printf("%u ", decompressed_values[i]);
    }
    printf("\n");

    // Libera a memória alocada
    free(bin_string);
    free(decompressed_values);

    return 0;
}

