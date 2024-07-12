//Dependencias:

#include "bitpack.h"

//------------------------------------------------------------------------------------------
//Funções:

uint32_t pow_2(uint32_t exponent)
{//Função para calcular a potência de 2
    return 1 << exponent;
}

void compress(const uint32_t* values, size_t num_values, size_t* bit_lengths, char* buffer)
{//Faz a conversão de uma lista de valores para um buffer, lista de caracteres
	//  Recebe:
 	//  - values: é o uma lista de valores com até 32 bits por valor
	//  - num_values: é a quantidade de valores na lista
	//  - bit_lenths: é uma lista com o tamanho em bits de cada valor, para calcular basta arredondar para cima log_2(values[i]), o ideal é já definir na aplicação
	//  - buffer: é o buffer onde será escrito
  
    size_t bit_now = 0; //É o bit atual no buffer
      
    for (size_t value = 0; value < num_values; value++)
    { //Para cada valor na lista
        for (size_t bit = 0; bit < bit_lengths[value]; bit++)
        { //Percorre todos os bits de um valor específico
            if (values[value] & (1 << (bit_lengths[value] - 1 - bit)))
            { //Copia o bit atual da variável e joga no buffer, tudo isso de forma concatenada
                buffer[bit_now / 8] |= (1 << (7 - (bit_now % 8))); //Joga o valor em bit na variável
                //Perceba que usamos ou, pois o buffer está zerado, e vamos adicionando bit a bit
            }
            bit_now++;
        }
    }
}

void decompress(const char* buffer, uint32_t* values, size_t num_values, size_t* bit_lengths)
{//Função para converter uma string binária de volta para uma lista de números inteiros
	//  - buffer: é o buffer onde será escrito
	//	- values: é a lista de valores que devem estar vazios a principio, cabe até 32 bits por valor
	//	- num_values: é o número de valores que deve ser salvo na lista
	//	- bit_lenths: é a largura em bits de cada valor da lista
	
    size_t bit_now = 0; //É o bit atual no buffer
    
    for (size_t i = 0; i < num_values; ++i)
    {//Para cada valor na lista de números
        values[i] = 0; //O valor começa zerado
        size_t bit_length = bit_lengths[i]; //O tamanho da variável específica em bits
        
        for (size_t bit = 0; bit < bit_length; bit++)
        {//Para cada bit na variável
            if (buffer[bit_now / 8] & (1 << (7 - (bit_now % 8))))
            { //Caso o bite no buffer seja 1, adiciona esse 1 bite a o valor
                values[i] |= (1 << (bit_length - bit - 1));
            }
            bit_now++;
        }
    }
}
