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
    def encode(arg) -> str:
        result = ''
        char_number = -1
        arg_str = ''.join(format(ord(char), '08b') for char in str(arg))
        length_bits = len(arg_str)
        padding = length_bits % 6
        if padding != 0:
            arg_str = arg_str + (6 - padding) * "0" 
        
        for i in range(0, length_bits, 6):
            char_number = int(arg_str[i:i+6], 2)
            result = result + CONST.BASE64_CHARS[char_number]
        
        if padding != 0:
            result = result + (3 - padding//2) * CONST.PADDING_CHAR 
        
        return result
        
if __name__ == "__main__":
    print(Base64ToolKit.encode("Hello World")) # SGVsbG8gV29ybGQ=
    print(Base64ToolKit.encode("Hello")) # SGVsbG8=
    print(Base64ToolKit.encode("Hell")) # SGVsbA==
    