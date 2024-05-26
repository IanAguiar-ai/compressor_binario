# compressor_binario

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

# bitpack

Comprime inteiros em bites

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

### Criar objeto

```
sua_variavel = bitpack()
```

### Comprimir

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

Ou ainda:

```
a = bitpack([14, 29, 875, 18])

b = bitpack()
b.decompress(a)
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
b.decompress(a)
```

### Salvar texto comprimido em binario

Salvar o texto:

```
a = bitpack([14, 29, 875, 18])
a.save(name = "teste")

b = bitpack(a.lenth_bites, name = "teste")
```

