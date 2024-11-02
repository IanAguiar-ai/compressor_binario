from bitpack import bitpack
from frequentist_compressor import Frequentist_Compressor

import zipfile
import io

from random import random

if __name__ == "__main__":
##    with open("/home/user/Documents/__git_repos__/card_game_ascii/engine_card_game.py", "r") as arq:
##        SEU_TEXTO:str = arq.read()

##    with open("/home/user/Documents/__git_repos__/card_game_ascii/arts.py", "r") as arq:
##        SEU_TEXTO += arq.read()

##    with open("/home/user/Documents/__git_repos__/compressor_binario/README.md", "r") as arq:
##        SEU_TEXTO += arq.read()

    SEU_TEXTO = ""
    for i in range(50_000):
        SEU_TEXTO += f"{chr(int(random()*random()*10+random()*random()*random()*random()*96)+62)}"

    ##############################################################################################################
    fc = Frequentist_Compressor()
    comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

    print(f"Original: {len(SEU_TEXTO)} bytes\nComprimido: {len(comprimido)}  + {len(dicionario_bits)} bytes")
    print(f"Ganho de {(1 - (len(comprimido) + len(dicionario_bits))/len(SEU_TEXTO)) * 100:0.2f}%")

    contagem = [(i[0], i[1]) for i in zip(fc.chars_count.keys(), fc.chars_count.values())]
    contagem = sorted(contagem, key = lambda x:x[1], reverse = True)

    total_acumulado = 0
    total = sum(fc.chars_count.values())
    print(f"Dicionario de bits:")
    n = 0
    for c in contagem:
        n += 1
        total_acumulado += c[1]
        proporcao = total_acumulado/total
        bits = int(-0.5 + (0.25 - 2 * (-n))**(1/2) + 1.999)
        bits_total = bits/8*c[1]
        if c[0] != "\n":
            print(f"\t'{c[0]}' ({n:3.0f} : {proporcao*100:2.03f}% : {c[1]/total*100:5.02f}%): {c[1]:7} -> {bits:3}:{bits_total:10} ({bits_total/len(comprimido) *100:0.02f}%)")
        else:
            print(f"\t'\\n'({n:3.0f} : {proporcao*100:2.03f}% : {c[1]/total*100:5.02f}%): {c[1]:7} -> {bits:3}:{bits_total:10} ({bits_total/len(comprimido) *100:0.2f})")

##    fc.save("teste")
##    a, b = fc.open("teste")
##    print(fc.decompress(a, b) == SEU_TEXTO)

    ##############################################################################################################
    #ZIP
    
    # Criar um buffer de bytes para armazenar o arquivo comprimido
    buffer = io.BytesIO()

    # Criar um arquivo ZIP e adicionar o texto como um arquivo dentro do ZIP
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr("seu_texto.txt", SEU_TEXTO)

    # Obter o conteúdo do buffer
    conteudo_zip = buffer.getvalue()

    print(f"\n\nZIP\nComprimido ZIP: {len(conteudo_zip)} bytes")
    print(f"Ganho de {(1 - len(conteudo_zip)/len(SEU_TEXTO)) * 100:0.2f}%")

    
