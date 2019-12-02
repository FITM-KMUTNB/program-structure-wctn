def main():
     sentence = 0
     letter = 0
     line = 0
     upper = 0
     lower = 0
     special = 0 
     infile = open('Loop.txt','r+')
     file = infile.read()
     list(file)

     Sentence(file,sentence)
     Word(file)
     Letter(file,letter)
     Line(file,line)
     Upper(file,upper)
     Lower(file,lower)
     Special(file,special)

def Sentence(file,sentence):
    sentence = file.split('.')
    print(len(sentence)-1)

def Word(file):
    print(len(file.split()))

def Letter(file,letter):
    for k in file:
        if k.isalpha() == True:
            letter += 1
    print(letter)

def Line(file,line):
    print(len(file.split('\n')))

def Upper(file,upper):
    for k in file :
        if  k.split() is True:
            upper += 1
    print(upper)

def Lower(file,lower):
    for k in file :
        if k.split() is True:
            lower += 1
    print(lower)

def Special(file,special) :
    for k in file :
        if k == "." or k == "," or k == ";" or k == "-" or k == ":" or k == "(" or k == "/" or k == ")" :
            special += 1 
    print(special) 



main()