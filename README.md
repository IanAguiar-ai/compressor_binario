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
``

### Comprimir em tamanho fixo

```
a = bitpack([14, 29, 875, 18], [6, 7, 20, 7])
print(a.real)

b = bitpack()
b.decompress(a)
```

