"""
Biblioteca que comprime inteiros em bites
"""

class bitpack:
    __slots__ = ("__bytes", "memory", "__lenth", "lenth_bites", "real", "fixed_size")
    def __init__(self, values = None, lenth_bites:list = []) -> None:
        """
        Ultima modificação: 0.0.2 
        """
        self.__bytes:int = 1
        self.memory:str = None
        self.__lenth:int = None
        if lenth_bites == []:
            self.fixed_size = False
        else:
            self.fixed_size = True
        self.lenth_bites:list = lenth_bites
        self.real:bin = None
        if values != None:
            self.compress(values)

    def __calculate_lenth(self) -> None:
        """
        Ultima modificação: 0.0.1
        """
        while len(self.memory) % 8 != 0:
            self.memory += "0"
        self.__lenth:int = int(len(self.memory)/8)
    
    def compress(self, values:list) -> None:
        """
        Ultima modificação: 0.0.2
        """
        self.memory:str = ""
        i = 0
        for value in values:
            new_text = str(bin(value))[2:]
            if self.fixed_size:
                new_text = f"{(self.lenth_bites[i] - len(new_text)) * '0'}{new_text}"
            self.memory += new_text
            if not self.fixed_size:
                self.lenth_bites.append(len(new_text))
            i += 1
        self.__calculate_lenth()
        self.__to_bin()

    def __to_bin(self) -> None:
        """
        Ultima modificação: 0.0.1
        """
        integer_value:int = int(self.memory, 2)
        byte_value:bytes = integer_value.to_bytes(self.__lenth, byteorder='big')
        self.real:int = byte_value

    def save(self, name:str = "compress") -> None:
        """
        Ultima modificação: 0.0.1
        """
        if self.real == None:
            self.__to_bin()
        with open(f"{name}.bin", 'wb') as file:
            file.write(self.real)
        self.real = None

    def read(self, lenth_bytes:list, name:str = "compress") -> list:
        """
        Ultima modificação: 0.0.1
        """
        with open(f"{name.replace('.bin','')}.bin", "rb") as arq:
            file = arq.read()
        return self.decompress(file, lenth_bytes)

    def decompress(self, value:str, lenth_bytes:list = None) -> list:
        """
        Ultima modificação: 0.0.1
        """
        if type(value) == bitpack:
            if value.real == None:
                value.__to_bin()
            lenth_bytes:list = value.lenth_bites
            value:str = value.real
            
        binary_representation:str = ''.join(format(byte, '08b') for byte in value)
        print(binary_representation)
        binary:list = []
        init:int = 0
        end:int = 0
        for n in lenth_bytes:
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
        """
        return self.__lenth    
