import subprocess

def convertToAlpha(bin):
    tab = bin.split()
    word =""
    for i in tab:
       convertToDecimal = int(i,2)
       convertToascii = chr(convertToDecimal)
       word += convertToascii
    return word

convertToAlpha("01101010 00100111 01101001 01110010 01100001 01101001 00100000")

def convertToHexa(decimal):
    hexaNumber = hex(decimal)
    return hexaNumber.replace("0x","")

convertToHexa(3499)

def convertToAlpha_2(hexa):
    convertToByte = bytes.fromhex(hexa)
    convertToAscii = convertToByte.decode()
    return convertToAscii
  
convertToAlpha_2("65722073757220766f7320746f6d6265732021")

def concatenate (a,b,c):
    decodedBinary = convertToAlpha(a)
    decodedDecimal = convertToHexa(b)
    decodedHexa = convertToAlpha_2(c)
    solution = decodedBinary + decodedDecimal + decodedHexa
    return solution
  
solution = concatenate("01101010 00100111 01101001 01110010 01100001 01101001 00100000",3499,"65722073757220766f7320746f6d6265732021")

subprocess.run(["unrar", "e", "tresor2.rar", "-p" + solution])
