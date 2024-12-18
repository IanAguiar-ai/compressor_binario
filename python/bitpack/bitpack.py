"""
Biblioteca que comprime inteiros em bites
"""

def decompress(text:str, lenth_bites:list) -> list:
    """
    Recebe uma string e converte nos números corretos
    """
    

class bitpack:
    __slots__ = ("__bytes", "memory", "__lenth", "lenth_bites", "real", "__fixed_size")
    def __init__(self, values = None, lenth_bites:list = []) -> None:
        """
        Ultima modificação: 0.0.2
        """
        self.__bytes:int = 1
        self.memory:str = None
        self.__lenth:int = None
        if lenth_bites == []:
            self.__fixed_size = False
        else:
            self.__fixed_size = True
        self.lenth_bites:list = lenth_bites
        self.real:bin = None
        if values != None:
            self.compress(values)

    def __calculate_lenth(self) -> None:
        """
        Ultima modificação: 0.0.1
        Calcula quantos byts são usados para armazenar a informação
        """
        while len(self.memory) % 8 != 0:
            self.memory += "0"
        self.__lenth:int = int(len(self.memory)/8)

    def compress(self, values:list) -> None:
        """
        Ultima modificação: 0.0.2
        Comprime a informação
        """
        self.memory:str = ""
        i = 0
        for value in values:
            new_text = str(bin(value))[2:]
            if self.__fixed_size:
                new_text = f"{(self.lenth_bites[i] - len(new_text)) * '0'}{new_text}"
            self.memory += new_text
            if not self.__fixed_size:
                self.lenth_bites.append(len(new_text))
            i += 1
        self.__calculate_lenth()
        self.__to_bin()

    def __to_bin(self) -> None:
        """
        Ultima modificação: 0.0.1
        Passa a informação armazenada na memoria para binario
        """
        integer_value:int = int(self.memory, 2)
        byte_value:bytes = integer_value.to_bytes(self.__lenth, byteorder='big')
        self.real:int = byte_value

    def save(self, name:str = "compress") -> None:
        """
        Ultima modificação: 0.0.1
        Salva em um arquivo binario
        """
        if self.real == None:
            self.__to_bin()
        with open(f"{name.replace('.bin','')}.bin", 'wb') as file:
            file.write(self.real)
        self.real = None

    def read(self, lenth_bites:list, name:str = "compress") -> list:
        """
        Ultima modificação: 0.0.1
        Lê um arquivo binario salvo no computador
        """
        with open(f"{name.replace('.bin','')}.bin", "rb") as arq:
            file = arq.read()
        return self.decompress(file, lenth_bites)

    def decompress(self, value:str, lenth_bites:list = None) -> list:
        """
        Ultima modificação: 0.0.1
        Descomprime uma informação que já foi comprimida
        """
        if type(value) == bitpack:
            if value.real == None:
                value.__to_bin()
            lenth_bites:list = value.lenth_bites
            value:str = value.real

        binary_representation:str = ''.join(format(byte, '08b') for byte in value)
        print(binary_representation)
        binary:list = []
        init:int = 0
        end:int = 0
        for n in lenth_bites:
            end += n
            binary.append(binary_representation[init:end])
            init += n
        print(binary)

        for i in range(len(binary)):
            binary[i] = int(binary[i], 2)

        return binary

    def __len__(self) -> int:
        """
        Ultima modificação: 0.0.1
        Mostra o tamanho em byts usado para armazenar a informação
        """
        return self.__lenth  
