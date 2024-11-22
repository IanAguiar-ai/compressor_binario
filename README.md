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

# `frequentist_compressor.py`

Compressão que usa a informação de frequência de caracteres em um texto, salvando o dicionário de caracteres e o próprio texto comprimido.

A principal inovação dessa técnica desenvolvida por mim, é que, em vez de utilizar uma lista de bits gerada por uma árvore binária convencional, emprega-se uma árvore desbalanceada composta por sequências de zeros e uns onde um caracter pode ser um valor no meio da árvore e ainda ter filhos. Dessa forma, quanto menor a entropia dos dados, mais eficiente é a compressão. Um exemplo típico onde essa abordagem se destaca são os textos, já que a compressão se beneficia da estrutura de frequência dos caracteres.

A vantagem fundamental desta técnica é o uso eficiente da porção intermediária da árvore. Por exemplo, a atribuição de valores binários ocorre da seguinte maneira:

- valor 1 = 01 (caractere de maior frequência)
- valor 2 = 001
- valor 3 = 011
- valor 4 = 0001
- valor 5 = 0011
- valor 6 = 0111
- valor 7 = 00001
- valor 8 = 00011
- valor 9 = 00111
- valor 10 = 01111

### Pior caso para a quantidade de bits usados em média para \( n \) caracteres com entropia absoluta:

$$ sum_{n = 1}^k n * (n - 1) = sum_{n = 1}^k n² - n = sum_{n = 1}^k n² - sum_{n = 1}^k n = sum_{n = 1}^k n² - (k² + k) / 2 = (k² + k) * (k - 1) / 3 $$

### Quantidade máxima de bits para `x`, sendo o número de caracteres diferentes usados:

$$ ((n - 1)² + (n - 1)) / 2 = (n² - 2n + 1 + n - 1) / 2 = (n² - n) / 2 = x $$

## Uso padrão

### Instanciar

```
fc = Frequentist_Compressor()
```

### Compressão

Com dicionário de compressão ótimo:

```
SEU_TEXTO:str = "Teste para compressor 123456789100 "*1000
comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

print(f"Original: {len(SEU_TEXTO)} bytes\nComprimido: {len(comprimido)}  + {len(str(dicionario_bits))} bytes")
print(f"Ganho de {(1 - (len(comprimido) + len(str(dicionario_bits)))/len(SEU_TEXTO)) * 100:0.2f}%")

print(f"Comprimido {comprimido}")
print(f"Dicionario de bits: {dicionario_bits}")
```

Com dicionário de compressão reutilizado:

```
comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO, dict_bins = SEU_DICIONARIO_BITS)
```

### Salvar compressão

Gera dois arquivos, um *.frcp*.

```
fc.save(name = "exemplo")
```

### Abrir arquivo salvo

```
comprimido, dicionario_compressao = fc.open(name = "exemplo")
```

### Descomprimir

```
descomprimido = fc.decompress(text = comprimido, dict_bins = dicionario_compressao)

print(descomprimido)
```

## Uso no modo texto

Uma etapa adicional é incluída caso o usuário deseje utilizar o modo texto. Para ativar este modo, basta especificá-lo no momento da instância da classe da seguinte forma:

```
fc_modo_texto = Frequentist_Compressor(text_mode = True)
```

## Funções auxiliares

### ```to_latin1```

O texto é convertido para a codificação latin-1, que utiliza 1 byte por caractere.

```
SEU_TEXTO:str = "seu texto aqui"
SEU_TEXTO = to_latin1(text = SEU_TEXTO)
```

# `low_compressor_iot.py`

Mesma forma de uso do `frequentist_compressor.py`, mas sem o modo 'text', ganha 1 byte na compressão, ideal para pacotes entre 90 bytes e 300 bytes, ou seja, dentro do range de aplicações de IoT.
