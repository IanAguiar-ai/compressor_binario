from bitpack import bitpack
from frequentist_compressor import Frequentist_Compressor, to_latin1

import zipfile
import io

from random import random

TEST_7Z:bool = False
if TEST_7Z:
    import pylzma

if __name__ == "__main__":

    TEXTOS = []
    
    SEU_TEXTO = ""
    for i in range(50_000):
        SEU_TEXTO += f"{chr(int(random()*random()*10+random()*random()*random()*random()*96)+62)}"
    TEXTOS.append(SEU_TEXTO)
    
    with open("bitpack.py", "r") as arq:
        SEU_TEXTO:str = arq.read()
    TEXTOS.append(SEU_TEXTO)

    with open("compressor_binario.py", "r") as arq:
        SEU_TEXTO:str = arq.read()
    TEXTOS.append(SEU_TEXTO)

    try:
        with open("/home/user/Documents/__git_repos__/compressor_binario/README.md", "r") as arq:
            SEU_TEXTO:str = arq.read()
        TEXTOS.append(SEU_TEXTO)
        
        with open("/home/user/Documents/estudos/palestras/palestra/roteiro", "r") as arq:
            SEU_TEXTO:str = arq.read()
        TEXTOS.append(SEU_TEXTO)

        with open("/home/user/Documents/__git_repos__/card_game_ascii/arts.py", "r") as arq:
            SEU_TEXTO:str = arq.read()
        TEXTOS.append(SEU_TEXTO)

        with open("/home/user/Documents/__git_repos__/card_game_ascii/engine_card_game.py", "r") as arq:
            SEU_TEXTO:str = arq.read()
        TEXTOS.append(SEU_TEXTO)
    except:
        pass

    SEU_TEXTO:str = """A programacao e uma das habilidades mais valiosas no mercado de trabalho atual. Com a crescente digitalizacao das empresas e a expansao das tecnologias, dominar linguagens de programacao pode abrir muitas portas. Profissionais que entendem como criar algoritmos, desenvolver solucoes e automatizar processos ganham destaque, ja que essas habilidades sao aplicaveis em diversos setores, como finance, marketing, saude e educacao.
Linguagens como Python, JavaScript e C++ sao populares por conta de suas versatilidades e funcionalidades. Python, por exemplo, e amplamente usado em analise de dados e aprendizado de maquina, areas que estao em alta demanda. JavaScript e muito presente no desenvolvimento web, possibilitando a criacao de sites interativos e dinamicos, enquanto o C++ e comumente utilizado para criar aplicacoes de alto desempenho, como jogos e sistemas operacionais.
A evolucao da tecnologia nao para e, com isso, as oportunidades para quem sabe programar tambem aumentam. Alem de aumentar a capacidade de resolver problemas complexos, a programacao promove o raciocinio logico e a criatividade. Aprender a programar pode parecer desafiador no inicio, mas com persistencia, qualquer pessoa consegue avancar e descobrir o prazer de construir algo do zero.
A capacidade de adaptar-se rapidamente e um diferencial importante nos dias de hoje. Com tantas mudancas acontecendo em todas as areas, ser flexivel e estar aberto ao aprendizado continuo pode fazer a diferenca. Profissionais que buscam desenvolver novas habilidades e atualizar-se regularmente conseguem acompanhar as novas demandas e contribuir de forma mais efetiva em suas carreiras. Essa postura proativa e fundamental para lidar com os desafios modernos e aproveitar as oportunidades.
Na area de tecnologia, por exemplo, a inovacao acontece em ritmo acelerado. Todos os dias, surgem novas ferramentas, metodologias e paradigmas que impactam como o trabalho e realizado. Profissionais de TI que se mantem atualizados sobre essas novidades podem usar as novas tendencias a seu favor, agregando valor a suas equipes e projetos. Dessa forma, conseguem nao apenas executar suas tarefas, mas tambem melhorar processos e criar solucoes mais eficientes.
Outro ponto relevante e o networking, ou seja, a criacao de redes de contatos profissionais. Ter uma rede solida de contatos e importante para quem deseja expandir suas possibilidades. Alem de compartilhar conhecimentos e experiencias, o networking ajuda a abrir portas para novas parcerias e oportunidades de trabalho. Pessoas bem conectadas e engajadas em suas redes acabam sendo lembradas em oportunidades de colaboracao e recomendadas em projetos importantes.
O gerenciamento de tempo e um dos pilares para uma rotina produtiva e equilibrada. Saber definir prioridades e distribuir as atividades ao longo do dia ajuda a evitar a sobrecarga e aumenta a eficiencia. Uma tecnica popular e a do Pomodoro, onde voce trabalha intensamente por 25 minutos e faz uma pausa de cinco minutos. Esse metodo ajuda a manter o foco e a energia ao longo das tarefas, permitindo que o cerebro descanse e volte com mais disposicao para o proximo ciclo.
Outro aspecto fundamental e o planejamento de metas a longo prazo. Definir objetivos claros e mensuraveis oferece uma direcao e facilita a organizacao das atividades diarias para alcanca-los. Pequenos passos constantes geralmente trazem melhores resultados do que esforcos esporadicos e intensos. Registrar as metas e revisar periodicamente o progresso tambem ajuda a manter a motivacao em alta, permitindo ajustes quando necessario.
A automotivacao e uma habilidade poderosa para se manter alinhado com seus planos e metas. Muitas vezes, esperar por fatores externos para se sentir motivado pode ser um erro. Buscar fontes de inspiracao, ter uma rotina estruturada e valorizar os proprios avancos sao estrategias que contribuem para uma mente positiva e focada. Pessoas que desenvolvem uma automotivacao constante conseguem lidar melhor com os desafios e transformam obstaculos em oportunidades de crescimento.
A comunicacao eficaz e um elemento essencial em qualquer ambiente, seja ele profissional ou pessoal. Saber expressar ideias de forma clara e objetiva facilita o entendimento e promove a colaboracao entre as pessoas. No ambiente de trabalho, essa habilidade ajuda a evitar mal-entendidos, reduz conflitos e permite que as equipes alcancem resultados melhores. Alem disso, escutar ativamente os outros tambem faz parte de uma boa comunicacao e contribui para o respeito mutuo e para um clima harmonioso.
A empatia e outra habilidade muito importante para as relacoes interpessoais. Colocar-se no lugar do outro e entender suas perspectivas ajuda a criar uma convivencia mais positiva e compreensiva. A empatia permite que as pessoas desenvolvam conexoes mais profundas e autenticas, pois demonstra que ha uma preocupacao genuina com o bem-estar alheio. Em equipes de trabalho, essa qualidade favorece a colaboracao e cria um ambiente mais saudavel e produtivo.
Por fim, a resiliencia e essencial para lidar com os desafios e as adversidades do dia a dia. Pessoas resilientes conseguem enfrentar situacoes dificeis de maneira positiva, mantendo o foco e a determinacao. A capacidade de se recuperar e aprender com experiencias desafiadoras fortalece o individuo e o prepara melhor para futuros obstaculos. Desenvolver a resiliencia e uma forma de crescer emocionalmente, ampliando a habilidade de lidar com as diversas situacoes que a vida apresenta.
Ayrton Senna da Silva ONM • ComRB • CvMA • OME (São Paulo, 21 de março de 1960 – Bolonha, 1 de maio de 1994) foi um piloto de Fórmula 1, empresário e filantropo brasileiro. Senna foi campeão da categoria de piloto três vezes, em 1988, 1990 e 1991. Começou sua carreira competindo no kart em 1973 e em "carros de fórmula" em 1981, quando venceu as Fórmulas Ford 1600 e 2000. Em 1983 alcançou o título de campeão do Campeonato Britânico de Fórmula 3 batendo vários recordes. Seu desempenho impulsionou sua ascensão à Fórmula 1, fazendo sua primeira aparição na categoria no Grande Prêmio do Brasil de 1984 pela equipe Toleman-Hart. Em sua primeira temporada, Senna pontuou em cinco corridas, fechando o ano com treze pontos e a nona posição na classificação geral dos pilotos. No ano seguinte, ingressou na Lotus-Renault, pela qual venceu seis grandes prêmios ao longo de três temporadas.
Em 1988, juntou-se ao francês Alain Prost na McLaren-Honda, com o qual teve grande rivalidade. Senna venceu oito etapas daquela temporada e sagrou-se campeão mundial pela primeira vez. Após a polêmica final de 1989 com Prost que resultou na segunda colocação do torneio, ele retomou o título em 1990, vencendo novamente na temporada seguinte, tornando-se o piloto mais jovem a conquistar um tricampeonato na Fórmula 1 até então. Em 1993, Senna foi vice-campeão, vencendo cinco corridas. Transferiu-se para a Williams em 1994, onde disputou apenas três etapas, a última sendo o Grande Prêmio de San Marino, onde se acidentou e morreu, no Circuito de Ímola. Ao todo, Senna participou de 161 grandes prêmios na Fórmula 1, alcançando 41 vitórias, 80 pódios, 65 pole positions e 19 voltas mais rápidas.
Além das corridas de carros, Senna dedicava-se a jet skis, motos, aeromodelos e principalmente helicópteros. Também administrava diversas marcas e empreendimentos, além de ter patrocinado vários programas de assistência filantrópica, principalmente os ligados a crianças carentes. Depois de morrer, sua irmã, Viviane Senna, fundou o Instituto Ayrton Senna, uma organização não governamental que oferece oportunidades de desenvolvimento humano a crianças e jovens de baixa renda. Além disso, o personagem Senninha foi criado com a intenção de atingir o público infantil com os ideais do piloto, como a superação, dedicação e o gosto pela vitória.
Sua morte, assim como o funeral e velório, provocou uma das maiores comoções da história do Brasil, bem como repercussão mundial. Em pesquisas feitas com jornalistas especializados, pilotos e torcedores, foi amplamente considerado o melhor piloto da história da Fórmula 1 e um dos maiores automobilistas de todos os tempos.[6][7][8][9][10][11][12] Em 1999, foi eleito pela revista Isto É o esportista do século XX no Brasil. No auge de sua carreira, era considerado o maior ídolo brasileiro, posto que mantém mesmo depois de três décadas após a sua morte.
Em 1º de maio de 2024, o Globoplay lança uma série documental intitulada Senna por Ayrton. Nessa atração, foram usadas cerca de 150 horas de gravações de entrevistas de Senna para que a narração do documentário fosse feita em primeira pessoa, com ele narrando a própria história.
A Segunda Guerra Mundial foi um conflito militar global que durou de 1939 a 1945, envolvendo a maioria das nações do mundo — incluindo todas as grandes potências — organizadas em duas alianças militares opostas: os Aliados e o Eixo. Foi a guerra mais abrangente da história, com mais de 100 milhões de militares mobilizados. Em estado de "guerra total", os principais envolvidos dedicaram toda sua capacidade econômica, industrial e científica a serviço dos esforços de guerra, deixando de lado a distinção entre recursos civis e militares. Marcado por um número significante de ataques contra civis, incluindo o Holocausto e a única vez em que armas nucleares foram utilizadas em combate, foi o conflito mais letal da história da humanidade, resultando entre 50 a mais de 70 milhões de mortes.
Geralmente considera-se o ponto inicial da guerra como sendo a invasão da Polônia pela Alemanha Nazista em 1 de setembro de 1939 e subsequentes declarações de guerra contra a Alemanha pela França e pela maioria dos países do Império Britânico e da Commonwealth. Alguns países já estavam em guerra nesta época, como Etiópia e Reino de Itália na Segunda Guerra Ítalo-Etíope e China e Japão na Segunda Guerra Sino-Japonesa.[2] Muitos dos que não se envolveram inicialmente acabaram aderindo ao conflito em resposta a eventos como a invasão da União Soviética pelos alemães e os ataques japoneses contra as forças dos Estados Unidos no Pacífico em Pearl Harbor e em colônias ultra marítimas britânicas, que resultaram em declarações de guerra contra o Japão pelos Estados Unidos, Países Baixos e o Commonwealth Britânico.[3][4]
A guerra terminou com a vitória dos Aliados em 1945, alterando significativamente o alinhamento político e a estrutura social mundial. Enquanto a Organização das Nações Unidas (ONU) era estabelecida para estimular a cooperação global e evitar futuros conflitos, a União Soviética e os Estados Unidos emergiam como superpotências rivais, preparando o terreno para uma Guerra Fria que se estenderia pelos quarenta e seis anos seguintes (1945–1991). Nesse ínterim, a aceitação do princípio de autodeterminação acelerou movimentos de descolonização na Ásia e na África, enquanto a Europa ocidental dava início a um movimento de recuperação econômica e integração política.
O primeiro dia de setembro de 1939 é geralmente considerado o início da guerra, com a invasão alemã da Polônia; o Reino Unido e a França declararam guerra à Alemanha nazista dois dias depois. Outras datas para o início da guerra incluem o início da Segunda Guerra Sino-Japonesa, em 7 de julho de 1937.[5][6]
Outros seguem o historiador britânico A. J. P. Taylor, que considerava que a Guerra Sino-Japonesa e a guerra na Europa e em suas colônias ocorreram de forma simultânea e posteriormente se fundiram em 1941. Este verbete utiliza a data convencional. Outras datas por vezes utilizadas para o início da Segunda Guerra Mundial incluem a invasão italiana da Abissínia em 3 de outubro de 1935.[7][nota 1] O historiador britânico Antony Beevor vê o início da Segunda Guerra Mundial nas batalhas de Khalkhin Gol, travadas entre o Império do Japão e a União Soviética de maio a setembro de 1939.[9]
Também não existe consenso quanto à data exata do fim da guerra. Tem sido sugerido que a guerra terminou no armistício de 14 de agosto de 1945 (Dia V-J), ao invés da rendição formal do Japão em 2 de setembro de 1945; alguns apontam o fim da guerra no dia 8 de maio de 1945 (Dia V-E). No entanto, o tratado de paz com o Japão não foi assinado até 1951,[10] enquanto o acordo de paz com a Alemanha não foi ratificado até 1990.
A Primeira Guerra Mundial alterou radicalmente o mapa geopolítico da Europa, com a derrota dos Impérios Centrais (Áustria-Hungria, Alemanha e Império Otomano) e a tomada do poder pelos bolcheviques em 1917 na Rússia. Os aliados vitoriosos, como França, Bélgica, Itália, Grécia e Romênia ganharam territórios, enquanto novos Estados foram criados a partir do colapso da Áustria-Hungria e dos impérios russo e otomano. Apesar do movimento pacifista após o fim da guerra,[13][14] as perdas causaram um nacionalismo irredentista e revanchista em vários países europeus. O irredentismo e revanchismo eram fortes na Alemanha por causa das significativas perdas territoriais, coloniais e financeiras incorridas pelo Tratado de Versalhes. Pelo tratado, a Alemanha perdeu cerca de 13% do seu território e todas as suas colônias ultramarinas, foi proibida de anexar outros Estados, teve que pagar indenizações e sofreu limitações quanto ao tamanho e a capacidade das suas forças armadas.[15] Enquanto isso, a Guerra Civil Russa levava à criação da União Soviética.[16]
O Império Alemão foi dissolvido durante a Revolução Alemã de 1918–1919 e um governo democrático, mais tarde conhecido como República de Weimar, foi criado. O período entreguerras foi marcado pelo conflito entre os partidários da nova república e de opositores radicais, tanto de direita quanto de esquerda. Embora a Itália como aliado Entente tenha feito alguns ganhos territoriais, os nacionalistas do país ficaram irritados com as promessas feitas pelo Reino Unido e França para garantir a entrada italiana na guerra, que não foram cumpridas com o acordo de paz. De 1922 a 1925, o movimento fascista, liderado por Benito Mussolini, tomou o poder na Itália com uma agenda nacionalista, totalitária e de colaboração de classes, que aboliu a democracia representativa, reprimiu os socialistas, a esquerda e as forças liberais, e seguiu uma política externa agressiva destinada a forjar, através da força, o país como uma potência mundial — um "Novo Império Romano"[17] (ver: Grande Itália). 
Space Exploration Technologies Corp., cujo nome comercial é SpaceX, é uma fabricante estadunidense de sistemas aeroespaciais, transporte espacial e comunicações com sede em Hawthorne, Califórnia. A SpaceX foi fundada em 2002 por Elon Musk com o objetivo de reduzir os custos de transporte espacial para permitir a colonização de Marte. A SpaceX fabrica os veículos de lançamento Falcon 9 e Falcon Heavy, vários tipos motores de foguetes, cápsulas de carga Dragon, espaçonaves tripuladas e satélites de comunicação Starlink.
As conquistas da SpaceX incluem o primeiro foguete de combustível líquido com financiamento privado a alcançar a órbita (Falcon 1 em 2008), a primeira empresa privada a lançar, orbitar e recuperar com sucesso uma espaçonave (Dragon em 2010), a primeira empresa privada a enviar uma espaçonave para a Estação Espacial Internacional (Dragon em 2012), a primeira decolagem vertical e pouso propulsivo vertical para um foguete orbital (Falcon 9 em 2015), a primeira reutilização de um foguete orbital (Falcon 9 em 2017) e a primeira empresa privada para enviar astronautas para a órbita e para a Estação Espacial Internacional (SpaceX Crew Dragon Demo-2 em 2020). A SpaceX já lançou e reutilizou a série de foguetes Falcon 9 mais de 100 vezes.
A SpaceX está desenvolvendo uma megaconstelação de satélite chamada Starlink para fornecer serviço comercial de internet. Em janeiro de 2020, a constelação Starlink se tornou a maior constelação de satélites do mundo. A SpaceX também está desenvolvendo o Starship, um sistema de lançamento superpesado, totalmente reutilizável e com financiamento privado, para voos espaciais interplanetários. O Starship pretende se tornar o veículo orbital primário da SpaceX assim que estiver operacional, suplantando a frota Falcon 9, Falcon Heavy e Dragon existentes. O Starship será totalmente reutilizável e terá a maior capacidade de carga útil de qualquer foguete orbital já em sua estreia de seu voo orbital programado para o primeiro semestre de 2O22.
As principais conquistas da SpaceX são a reutilização de veículos de lançamento da classe orbital e a redução de custos na indústria de lançamentos espaciais. O mais notável deles são os pousos e relançamentos contínuos do primeiro estágio do Falcon 9 após um programa de vários anos para desenvolver a tecnologia reutilizável. Em maio de 2021, a SpaceX usou dois foguetes auxiliares de primeiro estágio separados, B1049 e B1051, nove e dez vezes, respectivamente.[83] Elon Musk passou a dizer que continuará a empurrar o foguete auxiliar, B1051, além da meta original de dez lançamentos.[84] A SpaceX é uma empresa espacial privada com a maioria de suas realizações como resultado de esforços de desenvolvimento autofinanciados, não desenvolvidos por contratos tradicionais de custo acrescido do governo dos Estados Unidos. Como resultado, muitas de suas conquistas também são consideradas inéditas para uma empresa privada.
A problematização, geralmente composta por duas perguntas dadas ao final da aula anterior, não forneceu informações suficientes, pois as perguntas foram apresentadas sem explicações adicionais. Embora tenha faltado conteúdo informativo, a problematização foi interessante como exercício de raciocínio lógico, "preparando" os alunos para o início efetivo da atividade.
Por outro lado, o texto inicial desta atividade ofereceu informações suficientes para contextualizar e iniciar as tarefas. Cabe destacar que esta foi a atividade 4, e a atividade anterior, que abordava a distribuição de energia na Terra, incluiu um texto complementar que, por meio de outra abordagem, já introduzia a questão climática.
Sim, a relação entre precipitação e temperatura, considerando a proximidade com o mar onde a umidade atua como um 'freio' nas variações de temperatura, era algo que já havia observado, mas nunca havia associado de maneira tão clara.
Os aspectos mais importantes nesta tarefa foram o entendimento e a associação entre temperatura e clima, levando em conta a distribuição de energia da Terra (latitude dos pontos), a proximidade do mar, bem como a relação entre o clima e a precipitação, além da inflexão das isotermas em função tanto da precipitação quanto da latitude.
Não, pelo mesmo motivo mencionado na atividade de 19 de setembro. Desta vez, nem o texto complementar acima das perguntas ofereceu informações completas, na minha opinião. O segundo parágrafo da problematização menciona que "os ventos podem transportar energia e vapor d'água de um lugar para outro", esclarecendo a ocorrência de certos fenômenos. No entanto, esse conceito não é abordado diretamente nas perguntas.
De fato, nunca havia refletido sobre o motivo da direção dos ventos. Fiquei impressionado ao descobrir, com a atividade, que os ventos se deslocam do local mais frio (de maior pressão) para o mais quente (de menor pressão), pois eu acreditava que o local mais quente teria maior pressão.
Graças às aulas anteriores, o conceito de monções ficou bastante claro. Além disso, ao final da aula, foram abordados temas um pouco além da atividade como a formação de furacões e as chuvas torrenciais na Índia, assuntos que eu desconhecia, assim como a explicação sobre a curvatura dos ventos alísios.
Todo o conteúdo desta atividade foi relevante. Eu nunca havia visto um mapa com as linhas isóbaras, nem tinha conhecimento sobre a Zona de Convergência Intertropical e os ventos alísios.
O texto complementar intitulado Clima e circulação atmosférica aborda o tema do clima e da temperatura, com foco nos controles climáticos e na distinção entre elementos estáticos e aspectos dinâmicos que influenciam essas mudanças.
Durante todo o meu ensino fundamental e médio, a única questão semelhante ao tema abordado que estudei foi o princípio de que o ar quente é mais leve e sobe, enquanto o ar frio desce. Isso me levou a refletir sobre a estrutura atual do ensino de geografia e como é plenamente possível incluir esses conceitos no ensino médio. No entanto, temas como geografia política, que já são amplamente tratados na disciplina de história, acabam sobrepondo grande parte dos conteúdos de geociências, com exceção de assuntos como rochas e placas tectônicas.
Minha conclusão com essa atividade é que o conteúdo de geociências dentro da geografia do ensino médio é bastante limitado atualmente. Considero isso a partir da minha experiência em uma escola pública, mas, como o ensino médio é amplamente pautado pelo Enem, presumo que o ensino de geociências seja igualmente fraco em outras instituições.
A problematização apresenta duas perguntas: "Por que os alísios têm uma trajetória curva?" e "O que acontece com o movimento do ar depois que os alísios convergem para a ZCIT?". Essas perguntas levantam questões pertinentes para a atividade 6, que aborda o padrão mundial de circulação atmosférica.
Como as respostas para essas perguntas foram discutidas em aula, elas contribuíram significativamente para a atividade. Quando o mapa do padrão geral de circulação atmosférica foi apresentado, o entendimento do desenho foi muito mais rápido, já que, por exemplo, já conhecíamos a resposta da segunda pergunta da problematização.
A atividade começa com a discussão sobre os alísios, depois aborda a circulação atmosférica na ZCIT e em faixas de latitudes específicas, em seguida questiona sobre precipitações, e, por fim, pede uma avaliação das vantagens e limitações do modelo de circulação atmosférica em comparação com os outros mapas apresentados em aula. Isso faz bastante sentido como última pergunta, pois permite uma avaliação retroativa não só do que foi trabalhado nesta atividade, mas também nas demais.
A atividade proporcionou conhecimentos relevantes, especialmente sobre a formação natural de regiões desérticas em torno dos 30 graus de latitude. Aprendi que essas regiões normalmente apresentam padrões de circulação e umidade típicos de áreas desérticas. Esse fenômeno ocorre devido ao movimento das massas de ar, que sobem úmidas na linha do Equador, resfriam-se e precipitam antes de atingir os 30 graus de latitude. Ao descerem, essas massas de ar, agora secas, aquecem durante o percurso descendente, resultando em ventos quentes e secos ao final do trajeto.
O texto complementar aborda em detalhes a distribuição de energia conforme a forma e os movimentos da Terra, que juntos influenciam a circulação atmosférica, como ocorre, por exemplo, pelo efeito Coriolis.
O texto também explora quais fenômenos ocorrem na troposfera e na estratosfera, tratando de temas como temperatura e circulação atmosférica. Além disso, ele discute a reflexão de energia pela Terra, o padrão global de pressão e circulação atmosférica, e a influência dos continentes e oceanos no padrão dos ventos, sendo este último já abordado em aula.
Exceto pelo efeito Coriolis, que eu já conhecia, e o último tema discutido em aula, eu não tinha conhecimento detalhado dos demais assuntos. Eu tinha algumas noções sobre a formação de ciclones, mas desconhecia o padrão da circulação atmosférica.
Com os temas abordados, questões principalmente relacionadas a precipitação e clima ficaram mais claras, proporcionando-me um entendimento de aspectos que antes não tinha considerado.
"""
    for i in [100, 500, 1000, 2000, 4000, 8000, 16000, len(SEU_TEXTO)]:
        TEXTOS.append(SEU_TEXTO[:i])

    palavra = ["paralelepipedo", "quando", "assim", "exemplo", "outros", "mesmo", "concerteza", "outras", "qualidade", "headset", "mouse", "teclado"]
    for i in [2**i for i in range(1, 15)]:
        texto = "abcdefghij "
        for _ in range(i):
            texto += f"{palavra[int(random()*len(palavra))]} "
        TEXTOS.append(texto)

    for i in [2**i for i in range(14)]:
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

    for i in [2**i for i in range(5)]:
        TEXTOS.append("a"*10*i + "b"*3*i + " "*5*i + "c"*15*i + " paralelepipedos")

    for i in [2**i for i in range(5, 16)]:
        temp = ""
        for _ in range(i):
            temp += str(int(random()*random()*random()*10))
        TEXTOS.append(temp)

    TEXTOS.append("ab" + "c"*100)
    TEXTOS.append("ab" + "c"*1000)

    for i in range(len(TEXTOS)):
        TEXTOS[i] = to_latin1(TEXTOS[i])

    resultados = {"ORIGINAL":[],
                  "FC_NORMAL_MODE":[],
                  "FC_TEXT_MODE":[],
                  "ZIP":[],
                  "7Z":[]}

    ##############################################################################################################

    for SEU_TEXTO in TEXTOS:
        resultados["ORIGINAL"].append(len(SEU_TEXTO))
    
        fc = Frequentist_Compressor(text_mode = False)
        comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

        print(f"Original: {len(SEU_TEXTO)} bytes\nComprimido: {len(comprimido)} + {len(dicionario_bits)} bytes = {len(comprimido) + len(dicionario_bits)} bytes (NORMAL MODE)")
        print(f"Ganho de {(1 - (len(comprimido) + len(dicionario_bits))/len(SEU_TEXTO)) * 100:0.2f}%")
        resultados["FC_NORMAL_MODE"].append(len(comprimido) + len(dicionario_bits))


        fc = Frequentist_Compressor(text_mode = True)
        comprimido, dicionario_bits = fc.compress(text = SEU_TEXTO)

        print(f"Comprimido: {len(comprimido)} + {len(dicionario_bits) + len(str(dicionario_bits['++'])) + len(str(dicionario_bits['##']))} bytes = {(len(comprimido) + len(dicionario_bits) + len(str(dicionario_bits['++'])) + len(str(dicionario_bits['##'])))} bytes (TEXT MODE)")
        print(f"Ganho de {(1 - (len(comprimido) + len(dicionario_bits) + len(str(dicionario_bits['++'])) + len(str(dicionario_bits['##'])))/len(SEU_TEXTO)) * 100:0.2f}%")
        resultados["FC_TEXT_MODE"].append((len(comprimido) + len(dicionario_bits) + len(str(dicionario_bits['##']))))


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
##        name_file = "teste_" + str(int(random()*100_000))
##        fc.save(name_file)
##
##        fc_2 = Frequentist_Compressor()
##        a, b = fc_2.open(name_file)
##        c = fc_2.decompress(a, b)
##        print(f"Possível salvar: {c == SEU_TEXTO}")

        ##############################################################################################################
        #ZIP
        
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
        
        print("#" * 70)

    print(resultados)
