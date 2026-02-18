"""
I have just read about how base64 works so I thought in order to test my understanding of it, 
I would write my own implementation of it in Python. 
"""
from typing import Any, Final

class Constants:
    __BASE64_CHARS: Final[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    __BYTES_IN_BASE64_CHAR: Final[int] = 6
    __PADING_CHAR = "="
    
    @property
    def BASE64_CHARS(self) -> str:
        return self.__BASE64_CHARS

    @property
    def BASE64_BYTES(self):
        return self.__BYTES_IN_BASE64_CHAR
    
    @property
    def PADDING_CHAR(self):
        return self.__PADING_CHAR

CONST = Constants()

class Base64ToolKit:
    @staticmethod
    def encode(arg: Any) -> str:
        result = ''
        char_number = -1
        arg_str = ''.join(format(ord(char), '08b') for char in str(arg))
        length_bits = len(arg_str)
        padding = length_bits % CONST.BASE64_BYTES
        if padding != 0:
            arg_str = arg_str + (CONST.BASE64_BYTES - padding) * "0" 
        
        for i in range(0, length_bits, CONST.BASE64_BYTES):
            char_number = int(arg_str[i:i+CONST.BASE64_BYTES], 2)
            result = result + CONST.BASE64_CHARS[char_number]
        
        if padding != 0:
            result = result + (CONST.BASE64_BYTES - padding) // 2 * CONST.PADDING_CHAR 
        
        return result
    