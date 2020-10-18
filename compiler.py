'''
Python compiler for Brainflub

Language by Snorepion
https://github.com/snorepion

Compiler made by Aryan Garg
https://gitnub.com/ARYANTECH123



'''


#The accumulator
a = 0

#Self explanatory, its the source code!
code = '++--:|'

#Private input and output strings
inp = ''
out = ''

#Messy compiler stuff down there
#           |
#           |
#           |
#           V

for symbol in code:

    if(symbol == '+'):
        a += 1
    elif(symbol == 's'):
        a = a ** 2
    elif(symbol == 'd'):
        a = a * 2
    elif(symbol == '-'):
        a -= 1
    elif(symbol == '='):
        out += chr(a)
    elif(symbol == '~'):
        a = 0

    elif(symbol == ':'):
        out = code
        print(out)
        break
    
    elif(symbol == '.'):
        print(out)
    elif(symbol == ','):
        out = ''
    elif(symbol == ','):
        out = ''

    elif(symbol == ' '):
        inp = input()
    elif(symbol == '*'):
        out += inp    

    elif(symbol == '|'):
        break
