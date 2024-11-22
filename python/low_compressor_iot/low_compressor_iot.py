from ast import literal_eval
from copy import deepcopy, copy

FILE_TYPE = "LCIOT"

def to_latin1(text:str) -> str:
    text_latin1 = text.encode("latin-1", errors="replace")
    return text_latin1.decode("latin-1")

class Low_Compressor_IOT:
    """
    Compressor that generates the list of characters and compression
    according to the frequency of each character.

    Compression follows the pattern of sequential zeros and ones.

    The most used characters will have representation in smaller bits.
    """

    __slots__ = ("chars_to_bin", "bin_to_chars", "chars_count", "reduce_text", "reduce_text_inverse", "chars_not_have", "reduce_repetition", "__temporary", "__text_mode")
    def __init__(self) -> None:
        self.chars_count:dict = {}
        self.chars_to_bin:dict = {}
        self.bin_to_chars:dict = {}
        self.chars_not_have:set = set([chr(i) for i in range(255)])
        self.__temporary:tuple = None

    def compress(self, text:str, dict_bins:dict = None) -> (str, dict):
        """
        Return:
            string of compress text
            dict of bins
        """

        try:
            text.encode("latin-1")
        except UnicodeEncodeError:
            raise ValueError("The text is not representable in latin-1!")

        # If you not have a dict of bins
        if dict_bins == None:
            self.counter(text)
        else:
            self.chars_count:dict = dict_bins

        list_chars_count:list = self.organize()

        for char in list_chars_count:
            self.chars_to_bin[char[0]] = char[2]
            self.bin_to_chars[char[2]] = char[0]

        text_compress = ""
        for char in text:
            text_compress += self.chars_to_bin[char]

        text_compress += "0"
        while len(text_compress)/8 != len(text_compress)//8:
            text_compress += "0"

        compress_text = ""
        for i in range(0, len(text_compress), 8):
            temp_bin = text_compress[i : i+8]
            compress_text += chr(int(temp_bin, 2))

        self.__temporary = (compress_text, deepcopy(self.bin_to_chars))

        return compress_text, self.bin_to_chars

    def decompress(self, text:str, dict_bins:dict = None) -> str:
        """
        Return:
            text of decompress
        """
        if "##" in dict_bins:
            convert_text:dict = deepcopy(dict_bins["##"])
            convert_repetitions:dict = deepcopy(dict_bins["++"])
            del dict_bins["##"]
            del dict_bins["++"]

        bin_text_char = ""
        for char in text:
            bin_ = str(bin(ord(char)))[2:]
            bin_text_char += (8 - len(bin_)) * "0" + str(bin(ord(char)))[2:]

        text_decompress:str = ""
        k = 0 
        for i in range(len(bin_text_char)):
            if k <= 1:
                try:
                    while bin_text_char[i + k] == "0":
                        k += 1
                    while bin_text_char[i + k] == "1":
                        k += 1

                    to_decompress = dict_bins[bin_text_char[i : i + k]]
                    text_decompress += to_decompress
                except IndexError:
                    pass
            else:
                k -= 1

        if "convert_text" in locals():
            for char in convert_text.keys():
                text_decompress = text_decompress.replace(char, convert_text[char])

        if "convert_repetitions" in locals():
            text_temp:str = copy(text_decompress)
            text_decompress:str = ""
            for i in range(len(text_temp)):
                if not text_temp[i] in convert_repetitions:
                    text_decompress += text_temp[i]
                else:
                    text_decompress += text_temp[i-1] * convert_repetitions[text_temp[i]]

        return text_decompress

    def generate_bins(self) -> list:
        """
        Generate list of bins
        """
        bins = []
        for i in range(1, 23 + 1): #x = 23 -> (x^2 + x)/2 >= 256 and x is a int
            for j in range(1, i + 1):
                bins.append("0"*(i - j + 1) + "1"*j)

        return bins

    def organize(self) -> list:
        """
        Return:
            List with the chars and count in order
        """
        bins = self.generate_bins()

        list_chars_count = [[key, self.chars_count[key]] for key in self.chars_count.keys()]
        list_chars_count = sorted(list_chars_count, key = lambda x: x[1], reverse = True)

        for i in range(len(list_chars_count)):
            list_chars_count[i].append(bins[i])

        return list_chars_count        

    def counter(self, text:str) -> None:
        """
        Count number of chr
        """
        for char in list(text):
            if not char in self.chars_count:
                self.chars_count[char] = 1
            else:
                self.chars_count[char] += 1
    
    def save(self, name:str) -> None:
        """
        Save the compression
        """
        _bin = ""
        for key in self.__temporary[1]:
            if not type(self.__temporary[1][key]) == dict:
                _bin += self.__temporary[1][key]

        _bin += _bin[0] + self.__temporary[0]
            
        with open(f"{name}.{FILE_TYPE}", "wb") as arq:
            arq.write(_bin.encode("latin-1"))

    def open(self, name:str) -> (str, dict):
        """
        Open archive compression
        """
        with open(f"{name}.{FILE_TYPE}", "rb") as arq:
            dict_compress_temp = arq.read().decode("latin-1")

        DIVISION:str = dict_compress_temp[0]
        text_compress:str = dict_compress_temp[dict_compress_temp[1:].find(DIVISION) + 2:]
        dict_compress_temp:str = dict_compress_temp[:1+dict_compress_temp[1:].find(DIVISION)]
        
        bits = self.generate_bins()
        dict_compress = {}
        for i in range(len(dict_compress_temp)):
            dict_compress[bits[i]] = dict_compress_temp[i]

        if "dict_compress_text" in locals():
            dict_compress["##"] = literal_eval(dict_compress_text)

        if "dict_compress_times" in locals():
            dict_compress["++"] = literal_eval(dict_compress_times)

        return text_compress, dict_compress
    
