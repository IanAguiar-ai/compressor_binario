from low_compressor_iot import Low_Compressor_IOT, to_latin1

import zipfile
import io

from random import random

TEST_ZIP:bool = True
TEST_7Z:bool = True
TEST_IOT:bool = True

if TEST_7Z:
    import pylzma

if TEST_IOT:
    import zlib

if __name__ == "__main__":

    TEXTOS = []
    
    SEU_TEXTO:str = """A programacao e uma das habilidades mais valiosas no mercado de trabalho atual. Com a crescente digitalizacao das empresas e a expansao das tecnologias, dominar linguagens de programacao pode abrir muitas portas. Profissionais que entendem como criar algoritmos, desenvolver solucoes e automatizar processos ganham destaque, ja que essas habilidades sao aplicaveis em diversos setores, como finance, marketing, saude e educacao.
Linguagens como Python, JavaScript e C++ sao populares por conta de suas versatilidades e funcionalidades. Python, por exemplo, e amplamente usado em analise de dados e aprendizado de maquina, areas que estao em alta demanda. JavaScript e muito presente no desenvolvimento web, possibilitando a criacao de sites interativos e dinamicos, enquanto o C++ e comumente utilizado para criar aplicacoes de alto desempenho, como jogos e sistemas operacionais.
A evolucao da tecnologia nao para e, com isso, as oportunidades para quem sabe programar tambem aumentam. Alem de aumentar a capacidade de resolver problemas complexos, a programacao promove o raciocinio logico e a criatividade. Aprender a programar pode parecer desafiador no inicio, mas com persistencia, qualquer pessoa consegue avancar e descobrir o prazer de construir algo do zero.
A capacidade de adaptar-se rapidamente e um diferencial importante nos dias de hoje. Com tantas mudancas acontecendo em todas as areas, ser flexivel e estar aberto ao aprendizado continuo pode fazer a diferenca. Profissionais que buscam desenvolver novas habilidades e atualizar-se regularmente conseguem acompanhar as novas demandas e contribuir de forma mais efetiva em suas carreiras. Essa postura proativa e fundamental para lidar com os desafios modernos e aproveitar as oportunidades.
Na area de tecnologia, por exemplo, a inovacao acontece em ritmo acelerado. Todos os dias, surgem novas ferramentas, metodologias e paradigmas que impactam como o trabalho e realizado. Profissionais de TI que se mantem atualizados sobre essas novidades podem usar as novas tendencias a seu favor, agregando valor a suas equipes e projetos. Dessa forma, conseguem nao apenas executar suas tarefas, mas tambem melhorar processos e criar solucoes mais eficientes.
Outro ponto relevante e o networking, ou seja, a criacao de redes de contatos profissionais. Ter uma rede solida de contatos e importante para quem deseja expandir suas possibilidades. Alem de compartilhar conhecimentos e experiencias, o networking ajuda a abrir portas para novas parcerias e oportunidades de trabalho. Pessoas bem conectadas e engajadas em suas redes acabam sendo lembradas em oportunidades de colaboracao e recomendadas em projetos importantes.
O gerenciamento de tempo e um dos pilares para uma rotina produtiva e equilibrada. Saber definir prioridades e distribuir as atividades ao longo do dia ajuda a evitar a sobrecarga e aumenta a eficiencia. Uma tecnica popular e a do Pomodoro, onde voce trabalha intensamente por 25 minutos e faz uma pausa de cinco minutos. Esse metodo ajuda a manter o foco e a energia ao longo das tarefas, permitindo que o cerebro descanse e volte com mais disposicao para o proximo ciclo."""
    
    for i in [10*i for i in range(1, 25)]:
        TEXTOS.append(SEU_TEXTO[:i])

    for i in [i*4 for i in range(1, 5)]:
        telefone = ""
        for _ in range(i):
            telefone += "5519 "
            for __ in range(4):
                telefone += str(int(random()*10))
            telefone += " "
            for __ in range(4):
                telefone += str(int(random()*10))
            telefone += "\n"
        TEXTOS.append(telefone)

    for i in [i for i in range(1, 5)]:
        TEXTOS.append("a"*10*i + "b"*3*i + " "*5*i + "c"*15*i + " paralelepipedos")

    TEXTOS.append("ab" + "c"*20)
    TEXTOS.append("ab" + "c"*50)
    TEXTOS.append("ab" + "c"*100)
    TEXTOS.append("ab" + "c"*200)

    for i in range(len(TEXTOS)):
        TEXTOS[i] = to_latin1(TEXTOS[i])

    resultados = {"ORIGINAL":[],
                  "MY_IOT":[],
                  "ZIP":[],
                  "7Z":[],
                  "IOT":[]}

    ##############################################################################################################

    for SEU_TEXTO in TEXTOS:
        resultados["ORIGINAL"].append(len(SEU_TEXTO))
    
        fc = Low_Compressor_IOT()
        comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

        print(f"Original: {len(SEU_TEXTO)} bytes\nComprimido: {len(comprimido)} + {len(dicionario_bits) + 1} bytes = {len(comprimido) + len(dicionario_bits) + 1} bytes (NORMAL MODE)")
        print(f"Ganho de {(1 - (len(comprimido) + len(dicionario_bits) + 1)/len(SEU_TEXTO)) * 100:0.2f}%")
        resultados["MY_IOT"].append(len(comprimido) + len(dicionario_bits) + 1)

##        contagem = [(i[0], i[1]) for i in zip(fc.chars_count.keys(), fc.chars_count.values())]
##        contagem = sorted(contagem, key = lambda x:x[1], reverse = True)
##
##        descomprimido = fc.decompress(comprimido, dicionario_bits)
##        print(f"Descomprimido: {descomprimido == SEU_TEXTO}")
##
##        total_acumulado = 0
##        total = sum(fc.chars_count.values())
##        print(f"Dicionario de bits:")
##        n = 0
##        for c in contagem:
##            n += 1
##            total_acumulado += c[1]
##            proporcao = total_acumulado/total
##            bits = int(-0.5 + (0.25 - 2 * (-n))**(1/2) + 1.999)
##            bits_total = bits/8*c[1]
##            if c[0] != "\n":
##                print(f"\t'{c[0]}' ({n:3.0f} : {proporcao*100:2.03f}% : {c[1]/total*100:5.02f}%): {c[1]:7} -> {bits:3}:{bits_total:10} ({bits_total/len(comprimido) *100:0.02f}%)")
##            else:
##                print(f"\t'\\n'({n:3.0f} : {proporcao*100:2.03f}% : {c[1]/total*100:5.02f}%): {c[1]:7} -> {bits:3}:{bits_total:10} ({bits_total/len(comprimido) *100:0.2f})")
##
##        name_file = "teste_" + str(len(comprimido) + len(dicionario_bits) + 1)
##        fc.save(name_file)
##        
##        fc = Low_Compressor_IOT()
##        a, b = fc.open(name_file)
##        c = fc.decompress(a, b)
##        print(f"Possível salvar: {c == SEU_TEXTO}")
##        print(SEU_TEXTO)
##        print(c)

        ##############################################################################################################
        #ZIP
        if TEST_ZIP:
            # Criar um buffer de bytes para armazenar o arquivo comprimido
            buffer = io.BytesIO()

            # Criar um arquivo ZIP e adicionar o texto como um arquivo dentro do ZIP
            with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.writestr("seu_texto.txt", SEU_TEXTO)

            # Obter o conteúdo do buffer
            conteudo_zip = buffer.getvalue()

            print(f"Comprimido: {len(conteudo_zip)} bytes")
            print(f"Ganho de {(1 - len(conteudo_zip)/len(SEU_TEXTO)) * 100:0.2f}% (ZIP)")
            resultados["ZIP"].append(len(conteudo_zip))

        ##############################################################################################################
        #7z
        # Criar um buffer de bytes para armazenar o arquivo comprimido
        if TEST_7Z:
            buffer = io.BytesIO()

            # Comprimir o texto usando LZMA (7z)
            conteudo_comprimido = pylzma.compress(SEU_TEXTO.encode("utf-8"))

            # Escrever o conteúdo comprimido no buffer
            buffer.write(conteudo_comprimido)

            # Obter o conteúdo do buffer
            conteudo_7z = buffer.getvalue()

            print(f"Comprimido: {len(conteudo_7z)} bytes")
            print(f"Ganho de {(1 - len(conteudo_7z)/len(SEU_TEXTO)) * 100:0.2f}% (7z)")
            resultados["7Z"].append(len(conteudo_7z))

        ##############################################################################################################
        #IOT
        # Criar um buffer de bytes para armazenar o arquivo comprimido
        if TEST_IOT:
            IOT_Z = zlib.compress(SEU_TEXTO.encode("latin-1"))
            IOT_Z = IOT_Z.decode("latin-1")

            print(f"Comprimido: {len(IOT_Z)} bytes")
            print(f"Ganho de {(1 - len(IOT_Z)/len(SEU_TEXTO)) * 100:0.2f}% (Zlib IOT Deflate)")
            resultados["IOT"].append(len(IOT_Z))
        
        print("#" * 70)

    print(resultados)
