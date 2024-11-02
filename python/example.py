from bitpack import bitpack
from frequentist_compressor import Frequentist_Compressor

if __name__ == "__main__":
##    b = bitpack()
##    resposta = b.decompress(b"8\xe8\x01\xb5\x92", [6, 7, 20, 7])
##    print(resposta)
##        
##    example = "meu teste de exemplo para testar 12345678900"
##    with open("bitpack.py", "r") as arq:
##        example = arq.read()
##        
##    print(f"Tamanho texto original: {len(example)}")
##    
##    c = Frequentist_Compressor()
##    a, b = c.compress(example)
##    print(f"Tamanho novo texto: {len(a)}\nTexto: {a}")
##    print(f"Dict:{b}")
##    print(f"Usado: {len(a)/len(example)}")
##
##    c.save("teste")
##
##    a, b = c.open("teste")
##
##    d = Frequentist_Compressor()
##    e = d.decompress(text = a, dict_bins = b)
##    print(e)
##    print(c.chars_count)

    fc = Frequentist_Compressor()

    SEU_TEXTO:str = "Teste para compressor 123456789100 "*1000
    comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

    print(f"Original: {len(SEU_TEXTO)} bytes\nComprimido: {len(comprimido)}  + {len(str(dicionario_bits))} bytes")
    print(f"Ganho de {(1 - (len(comprimido) + len(str(dicionario_bits)))/len(SEU_TEXTO)) * 100:0.2f}%")

    print(f"Comprimido {comprimido}")
    print(f"Dicionario de bits: {dicionario_bits}")

    fc.save(name = "exemplo")
    print("Salvo!")
    
    comprimido, dicionario_compressao = fc.open(name = "exemplo")
    print("Pego arquivos salvos!")

    descomprimido = fc.decompress(text = comprimido, dict_bins = dicionario_compressao)

    print(descomprimido)
    
