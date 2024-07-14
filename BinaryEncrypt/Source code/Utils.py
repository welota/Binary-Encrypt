from time import sleep as wait

class Utils:
    def CharToAscii(char: str) -> int:
        return ord(char)
    
    def AsciiToChar(Ascii: int) -> str:
        return chr(Ascii)
    
    def NumberToBin(Number: int) -> str:
        return bin(Number)[2:]
    
    def NumberToHex(Number: int) -> str:
        return hex(Number)[2:]
    
    def BinToNumber(Bin: str) -> int:
        result = 0
        for i, digit in enumerate(Bin[::-1]):
            result += int(digit) * (2 ** i)
        return result
    
    def ReverseBinary(Binary: str) -> int:
        result: str = ""
        for Bit in Binary:
            if Bit != " ":
                result += str(int(not int(Bit)))
            else:
                result += " "
        return result

    def TextToBin(Text: str) -> str:
        return ' '.join(format(ord(char), '08b') for char in Text)

    def BinToText(Bin: str) -> str:
        return ''.join(chr(int(binary, 2)) for binary in Bin.split())