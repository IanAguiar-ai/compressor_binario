from ast import literal_eval
from copy import deepcopy, copy

FILE_TYPE = "ifc"
DIVISION = chr(169) * 2

def to_latin1(text:str) -> str:
    text_latin1 = text.encode("latin-1", errors="replace")
    return text_latin1.decode("latin-1")

class Frequentist_Compressor:
    """
    Compressor that generates the list of characters and compression
    according to the frequency of each character.

    Compression follows the pattern of sequential zeros and ones.

    The most used characters will have representation in smaller bits.
    """

    __slots__ = ("chars_to_bin", "bin_to_chars", "chars_count", "reduce_text", "reduce_text_inverse", "chars_not_have", "reduce_repetition", "__temporary", "__text_mode")
    def __init__(self, text_mode:bool = False) -> None:
        self.chars_count:dict = {}
        self.chars_to_bin:dict = {}
        self.bin_to_chars:dict = {}
        self.reduce_text:dict = {}
        self.reduce_repetition:dict = {}
        self.chars_not_have:set = set([chr(i) for i in range(255)])
        self.__temporary:tuple = None
        self.__text_mode:bool = text_mode

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

        if self.__text_mode:
            self.chars_not_have:set = self.chars_not_have - set(text)
            text:str = self.text_frequentist_reducer(text) # PLUS

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

    def counter_text(self, text:str) -> list:
        """
        Count number of text
        """
        intermediate_characters:tuple = ("\n",
                                         "?", "!",
                                         ";", ":",
                                         ",", ".",
                                         "{", "}", "[", "]", "(", ")",
                                         "\t")
        
        for ic in intermediate_characters:
            text = text.replace(ic, " ")
        text = text.split(" ")

        dict_text = {}
        for word in text:
            if not word in dict_text:
                dict_text[word] = 1
            else:
                dict_text[word] += 1

        return sorted([(key, dict_text[key], (len(key) - 2) * dict_text[key]) for key in dict_text.keys()], key = lambda x : x[2], reverse = True)

    def text_frequentist_reducer(self, text:str) -> str:
        """
        Plus to text
        """
        # Word reducer
        text_freq = self.counter_text(text)

        chr_not:list = sorted(list(self.chars_not_have), reverse = True)

        inverse_reduce_text:dict = {}
        n = 0
        for chr_, qnt, points in text_freq:
            if qnt > 3 and points > 30 and n < len(chr_not):
                self.reduce_text[chr_not[n]] = chr_
                inverse_reduce_text[chr_] = chr_not[n]
                self.chars_not_have.remove(chr_not[n])
                n += 1

        self.bin_to_chars["##"] = {}
        for key in inverse_reduce_text.keys():
            text = text.replace(key, inverse_reduce_text[key])
            self.bin_to_chars["##"][inverse_reduce_text[key]] = key

        # Repetition reducer
        numbers_repetition:dict = {}
        for i in range(len(text) - 1):
            repetition = self.number_of_repetition(text[i:])
            if repetition >= 6:
                if not repetition in numbers_repetition:
                    numbers_repetition[repetition] = 1
                else:
                    numbers_repetition[repetition] += 1

        list_numbers_repetition = []
        for key in numbers_repetition.keys():
            list_numbers_repetition.append((key, numbers_repetition[key]))
        list_numbers_repetition = sorted(sorted(list_numbers_repetition, key = lambda x : x[0], reverse = True), key = lambda x : x[1], reverse = True)

        temp_l_n = set()
        final_repetition = []

        for item in list_numbers_repetition:
            if item[1] not in temp_l_n:
                final_repetition.append(item)
                temp_l_n.add(item[1])
        final_repetition = sorted(final_repetition, key = lambda x : x[0], reverse = True)

        inverse_reduce:dict = {}
        chr_not:list = sorted(list(self.chars_not_have), reverse = True)
        for i in range(len(final_repetition)):
            if i < len(chr_not):
                self.reduce_repetition[chr_not[i]] = final_repetition[i][0]
                inverse_reduce[final_repetition[i][0]] = chr_not[i]
                self.chars_not_have.remove(chr_not[i])

        final_text:str = ""
        n:int = 0
        try:
            max_value:int = max(list(self.reduce_repetition.values()))
        except ValueError:
            max_value:int = 0
        
        len_text:int = len(text)
        while n < len_text:
            repetition = self.number_of_repetition(text[n: min(n + max_value + 1, len_text)])
            if repetition in inverse_reduce:
                final_text += text[n] + inverse_reduce[repetition]
                n += repetition + 1
            else:
                final_text += text[n]
                n += 1

        self.bin_to_chars["++"] = self.reduce_repetition

        return final_text

    def number_of_repetition(self, text:str) -> int:
        """
        Count repetition of character
        """
        repetition:int = 0
        for i in range(1, len(text)):
            if text[0] == text[i]:
                repetition += 1
            else:
                return repetition
        return repetition
    
    def save(self, name:str) -> None:
        """
        Save the compression
        """
        _bin = ""
        for key in self.__temporary[1]:
            if not type(self.__temporary[1][key]) == dict:
                _bin += self.__temporary[1][key]

        if "##" in self.__temporary[1]:
            _bin += "||" + str(self.__temporary[1]["##"]).replace(": ", ":").replace(", ", ",")

        if "++" in self.__temporary[1]:
            _bin += "++" + str(self.__temporary[1]["++"]).replace(": ", ":").replace(", ", ",")

        _bin += DIVISION + self.__temporary[0]
            
        with open(f"{name}.{FILE_TYPE}", "wb") as arq:
            arq.write(_bin.encode("latin-1"))

    def open(self, name:str) -> (str, dict):
        """
        Open archive compression
        """
        with open(f"{name}.{FILE_TYPE}", "rb") as arq:
            dict_compress_temp = arq.read().decode("latin-1")

        text_compress:str = dict_compress_temp[dict_compress_temp.find(DIVISION) + 2:]
        dict_compress_temp:str = dict_compress_temp[:dict_compress_temp.find(DIVISION)]
        print(f">>>>>>>>>>>>>{dict_compress_temp}<<<<<<<<<<<<<,")

        if dict_compress_temp.find("||") > -1:
            dict_compress_text = dict_compress_temp[dict_compress_temp.find("||") + 2: dict_compress_temp.find("++")]
            dict_compress_times = dict_compress_temp[dict_compress_temp.find("++") + 2 :]
            dict_compress_temp = dict_compress_temp[:dict_compress_temp.find("||")]
        
        bits = self.generate_bins()
        dict_compress = {}
        for i in range(len(dict_compress_temp)):
            dict_compress[bits[i]] = dict_compress_temp[i]

        if "dict_compress_text" in locals():
            dict_compress["##"] = literal_eval(dict_compress_text)

        if "dict_compress_times" in locals():
            dict_compress["++"] = literal_eval(dict_compress_times)

        return text_compress, dict_compress
    
