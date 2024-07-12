versao = [0, 0, 1]
"""
Funções para comprimir e descomprimir texto, o funcionamento da biblioteca é a seguinte:

1) Um texto é selecionado, por exemplo, "cab";

2) As letras usadas no texto são passadas para uma lista, ["a", "b", "c"];

3) As letras tem seus valores como os index, sabendo disso o texto é re-escrito, por exemplo, [0, 1, 2];

4) É avaliado quantos bites conseguem coonter todas as letras, nesse caso apenas 2, por exemplo, [00, 01, 10];

5) Agora o texto é reescrito usando só os bites necessários, por exemplo, 100001;

6) Ele é passado para ascii, nesse caso por exemplo,100001 = 33 = '!', logo o texto comprimido é "!";

7) Também é salvo um arquivo de correção, que indica quais as correções e tamanho de bits são usados.

As duas funções principais são "comprimir" e "descomprimir"...
No final, esperasse que o programa consiga ganhar de 2%~30% de bits a menos, depende do tamanho do texto passado.
"""

from json import dumps, load
from os.path import getsize as size
from os.path import join
from time import sleep

def pegar_caracteres(texto:str) -> list:
    """
    Pega todos os caracteres usados no texto
    """
    return sorted(set(texto))

def passar_para_valor(caracteres:list, texto:str) -> list:
    """
    Passa para o texto para os seus respectivos valores dado a lista de caracteres usados
    """
    return [caracteres.index(char) for char in texto]

def concatenar_bits(caracteres:list, lista:list, bits:int = 5) -> str:
    """
    Concatena os bits que representam cada caracter na string
    """
    maximo:int = len(caracteres)
    resultado:str = ""
    for valor in lista:
        resultado += format(valor, f"0{bits}b")
    return resultado

def escrever_texto(resultado:str, intervalo:int = 7) -> str:
    """
    Escreve o novo texto em ASCII (7-bits) dado a concatenação feita
    """
    novo_texto:str = ""
    for i in range(0, len(resultado), intervalo):
        bits:list = resultado[i:i+intervalo]
        if bits:  # Verifica se há bits suficientes para formar um caractere
            valor:int = int(bits, 2)  # Converte os 7 bits para um inteiro
            novo_texto += chr(valor)  # Converte o inteiro para um caractere ASCII
    return novo_texto

def desconcatenar_bits(caracteres:list, texto:str, bits:int = 5) -> str:
    """
    Dado o texto novo que está em binário, ele desconcatena e transforma no bit ASCII correto
    """
    maximo:int = len(caracteres)
    resultado:str = ""
    for i in range(0, len(texto), bits):
        valor:list = texto[i:i + bits]
        if valor:
            try:
                resultado += caracteres[int(valor, 2)]
            except IndexError:
                resultado += "?"
    return resultado

def passar_para_binario(texto:str) -> str:
    """
    Passa o texto para binário
    """
    resposta:str = ""
    for i in texto:
        resposta += format(ord(i), f"0{7}b")
    return resposta

def conferir_compressao(texto_esperado:str, texto_final:str) -> (bool, str, float, list):
    """
    Confere a acurácia da compressão além de entregar uma lista de correções
    """
    resposta:str = ""
    correto:bool = True
    proporcao:list = [0, 0]
    correcao:list = []
    for i in range(len(texto_esperado)):
        try:
            if texto_esperado[i] == texto_final[i]:
                resposta += texto_esperado[i]
                proporcao[0] += 1
            else:
                resposta += "_"
                correto:bool = False
                proporcao[1] += 1
                correcao.extend([i, texto_esperado[i]])
        except IndexError:
            resposta += "_"
            correto:bool = False
            proporcao[1] += 1
            correcao.extend([i, texto_esperado[i]])
    return correto, resposta, proporcao, correcao

def ler_arquivo(arquivo:str) -> str:
    """
    Lê o arquivo
    """
    with open(arquivo, "r") as arq:
        texto:str = arq.read()
    return texto

def escrever_arquivo(arquivo:str, texto:str) -> None:
    """
    Escreve o arquivo
    """
    with open(arquivo, "w") as arq:
        arq.write(texto)

def comprimir(nome_arquivo:str, pasta:str) -> None:
    """
    Comprimi o arquivo
    """
    #Pega o texto original:
    tamanho_original:int = size(nome_arquivo)
    texto_antigo:str = ler_arquivo(nome_arquivo)

    num_correcoes_iniciais:int = 0 #Número de correções feitas no arquivo
    while True:
        texto:str = texto_antigo[0]*num_correcoes_iniciais + texto_antigo #Novo texto que será tratado
        caracteres:list = pegar_caracteres(texto) #Vê os caracteres que estão sendo usados no texto

        #Passa o texto para a lista de valores e vê quantos bits são necessários para a escritra de todos esses caracteres:
        lista_valores:list = passar_para_valor(caracteres, texto)
        tamanho_bits:int = len(str(bin(len(caracteres)))) - 2

        #Concatena e escreve o novo texto comprimido:
        resposta:list = concatenar_bits(caracteres, lista_valores, tamanho_bits)
        nome_arq_comprimido:str = f"{nome_arquivo}_comprimido"
        escrever_arquivo(join(pasta, nome_arq_comprimido), escrever_texto(resposta))
        resposta:str = passar_para_binario(ler_arquivo(join(pasta, nome_arq_comprimido)))
        tamanho_comprimido:int = size(join(pasta, nome_arq_comprimido))

        # Confere se o que foi comprimido precissa de correção:
        resposta_de_volta:str = desconcatenar_bits(caracteres, resposta, tamanho_bits)
        a, b, c, correcoes = conferir_compressao(texto, resposta_de_volta)
        print(f"{c[0]}/{sum(c)} = {c[0]/sum(c):.03f}", end = "")

        #Se precissa de correções cria um arquivo de correção:
        nome_arq_correcao:str = nome_arquivo + "_correcao.json"
        arq_json = dumps([caracteres, [*correcoes, tamanho_bits, num_correcoes_iniciais]])
        escrever_arquivo(join(pasta, nome_arq_correcao), arq_json)
        tamanho_correcao:int = size(join(pasta, nome_arq_correcao))

        #Calcula de deve tentar comprimir de novo mudando o primeiro caracter ou a compressão é o sufuciente:
        bytes_ganho:int = tamanho_original - (tamanho_comprimido + tamanho_correcao) - num_correcoes_iniciais
        print(f" | {bytes_ganho/tamanho_original * 100 :.02f}%")
        if (bytes_ganho > 20 and tamanho_original >= 350) or (c[0]/sum(c) == 1 and tamanho_original < 350):
            print(f"Tamanho arquivo original (bytes): {tamanho_original}\nTamanho arquivo comprimido (bytes): {tamanho_comprimido}\nTamanho arquivo correcao (bytes): {tamanho_correcao}\nGanho de espaço (bytes): {tamanho_original - (tamanho_comprimido + tamanho_correcao) - num_correcoes_iniciais}")
            print(f"Ganho de {bytes_ganho/tamanho_original * 100 :.02f}%")
            break

        num_correcoes_iniciais += 1
        sleep(0.5)

def descomprimir(nome_arquivo:str, pasta:str) -> None:
    """
    Descomprime o texto
    """
    #Pega o texto original e o arquivo de correcao:
    texto:str = ler_arquivo(f"{nome_arquivo}_comprimido")
    with open(f"{nome_arquivo}_correcao.json", "r") as arquivo:
        correcao:list = load(arquivo)
    caracteres:list = correcao[0]
    correcao:list = correcao[1]
    tamanho_bits:int = correcao[-2]
    tirar:int = correcao[-1]
    texto:str = passar_para_binario(texto)

    texto:str = desconcatenar_bits(caracteres, texto, tamanho_bits)
    texto:list = list(texto)
    for i in range(int(len(correcao)/2) - 1):
        texto[correcao[i*2]] = correcao[i*2 + 1]
    texto:str = "".join(texto[tirar:])

    escrever_arquivo(nome_arquivo, texto)
    
if __name__ == "__main__":
    nome_arquivo:str = "texto_1"
    salvar_em:str = "comprimidos"
    comprimir(nome_arquivo, salvar_em)

    nome_arquivo = f"comprimidos/{nome_arquivo}"
    descomprimir(nome_arquivo, salvar_em)
