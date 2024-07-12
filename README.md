# ```compressor_binario.py```

Compressor que trabalha com a redução de bits de um arquivo.

## Funcionamento

1. Um texto é selecionado, por exemplo, "cab";

2. As letras usadas no texto são passadas para uma lista, `["a", "b", "c"]`;

3. As letras têm seus valores como os índices, sabendo disso o texto é reescrito, por exemplo, `[0, 1, 2]`;

4. É avaliado quantos bits conseguem conter todas as letras, nesse caso apenas 2, por exemplo, `[00, 01, 10]`;

5. Agora o texto é reescrito usando apenas os bits necessários, por exemplo, `100001`;

6. Ele é passado para ASCII, nesse caso, por exemplo, `100001 = 33 = '!'`, logo o texto comprimido é "!";

7. Também é salvo um arquivo de correção, que indica quais as correções e tamanho de bits são usados.

As duas funções principais são `comprimir` e `descomprimir`...

No final, espera-se que o programa consiga ganhar de 2% a 30% de bits a menos, dependendo do tamanho do texto passado.


# ```bitpack.py```

Comprime inteiros em bites.

## Funcionamento

Objeto:

```
instancia = bitpack()
```

Variáveis do objeto:

```
instancia.memory:str ; EX: "0011100011101000000000011011010110010010"
instancia.lenth_bites:list ; EX: [6, 7, 20, 7]
instancia.real:bin ; EX: b"8\xe8\x01\xb5\x92"
```

Funções do objeto:

```
instancia.compress(values:list)
instancia.save(name:str)
instancia.read(lenth_bytes:list, name:str)
instancia.decompress(value:str, lenth_bytes:list)
len(instancia)
```

## Exemplo


### Compressão

Usando a menor quantidade de bits possível:

```
valores:list = [14, 29, 875, 18]

a = bitpack()
a.compress(valores)
```

Ou ainda:

```
valores:list = [14, 29, 875, 18]

a = bitpack(valores)
```

### Descomprimir

Conhecendo o objeto de compressão:

```
a = bitpack()
a.compress([23, 41, 21, 255])
print(a.real)

b = bitpack()
resp = b.decompress(a.real, a.lenth_bites)
print(resp)
```

Ou:

```
a = bitpack([14, 29, 875, 18])

b = bitpack()
b.decompress(a)
```

Ou ainda:

```
tamanho = [5, 6, 9, 6]
a = bitpack([14, 29, 875, 18])

string = a.real

b = bitpack()
b.decompress(string, tamanho)
```

### Comprimir em tamanho fixo

É passado já na criação da instancia do objeto o tamanho em bits para cada variável:

```
tamanho:list = [6, 7, 20, 7]
#000000 0000000 00000000000000000000 0000000 <- 40 bits ou 5 bytes
#2**6 = 64, 2^7 = 128, 2^20 = 1048576 -> 6 = 0~63 ; 7 = 0~128 ; 20 = 0~1048575

a = bitpack(values = [14, 29, 875, 18], lenth_bites = tamanho)
print(a.real)

b = bitpack()
b.decompress(a.real, tamanho)
```

### Salvar texto comprimido em binario

Salvar o texto:

```
a = bitpack([14, 29, 875, 18])
a.save(name = "teste")

b = bitpack()
b.read(a.lenth_bites, name = "teste")
```

# ```bitpack.c/bitpack.h```

Compressor de números inteiros para binário.

## Funções

### void compress(const uint32_t* values, size_t num_values, size_t* bit_lengths, char* buffer)

Função de compressão, recebe:

- ```values```: é o uma lista de valores de 32 bits;

- ```num_values```: é a quantidade de valores na lista;

- ```bit_lenths```: é uma lista com o tamanho em bits de cada valor, para calcular basta arredondar para cima log_2(values[i]), o ideal é já definir na aplicação;

- ```buffer```: é o buffer onde será escrito o binário, é uma lista de chars.

### void decompress(const char* buffer, uint32_t* values, size_t num_values, size_t* bit_lengths)

Função de descompressão, recebe:

- ```buffer```: é o buffer onde será escrito o binário, é uma lista de chars;

- ```values```: é o uma lista de valores de 32 bits;

- ```num_values```: é a quantidade de valores na lista;

- ```bit_lenths```: é uma lista com o tamanho em bits de cada valor, para calcular basta arredondar para cima log_2(values[i]), o ideal é já definir na aplicação.


### Exemplo de uso:

```
#include "bitpack.h"

int main() {
    // Lista de valores e seus comprimentos em bits
    uint32_t values[] = {6, 7, 140, 15, 20};
    size_t bit_lengths[] = {3, 3, 8, 4, 5};
    size_t num_values = sizeof(values)/sizeof(values[0]);

    // Calcula o comprimento total da string binária
    size_t total_bit_length = 0;
    for (size_t i = 0; i < num_values; ++i)
    {
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
```

Resposta esperada:

```
>>> gcc -o bitpack bitpack.c
>>> ./bitpack

String binária: �3�
Valores descomprimidos:
6 7 140 15 20
```



