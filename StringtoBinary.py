#converts given string to binary and prints to console
def StringToBinary(string) :
    length = len(string)
    bin = ""
    for i in range(length):
        bin += characterToBinary(ord(string[i])) + " "
    print(bin)

#converts given character to binary and returns it
def characterToBinary(character):
    binaryVal = bin(character)
    formattedBin = binaryVal[2:]
    return formattedBin
    


#main

#accepts input from user
string = input()
#executes conversion
StringToBinary(string)
