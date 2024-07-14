from Utils import Utils

Input = input("Write text to encrypt or decrypt: ").upper()
IsDebugMode = str(input("Do you want to enable debug mode? (Yes/No): ")).lower()

BinaryText: str = Utils.TextToBin(Input)
EncryptedBinaryText: str = str(Utils.ReverseBinary(BinaryText))
EncryptedText: str = Utils.BinToText(EncryptedBinaryText)

DebugMode: bool = False

if IsDebugMode == "yes":
    DebugMode = True
elif IsDebugMode == "no":
    DebugMode = False
else:
    print("Answer out of range (for default is false)")

print(f"Text in binary: {BinaryText}\nReverted text in binary: {EncryptedBinaryText}") if DebugMode else DebugMode
print(f"Text: {EncryptedText} (Result may contain errors because of legibility motives)")

input("Press enter to leave...")