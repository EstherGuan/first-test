#coding=utf-8
import random

#randnum = random.randint(10, 20)
#print randnum

#print 'COM: Guess what I think?'
#inputnum = int(raw_input())

def guessNum(inputnum, randnum):
    
    while inputnum != randnum:
        print inputnum
        if inputnum > randnum:
            print 'COM: Too Big!!!'
            inputnum = int(raw_input())
        elif inputnum < randnum:
            print 'COM: Too Small!!!'
            inputnum = int(raw_input())
    print 'COM: BinGo!!!'

def main():
    
    randnum = random.randint(0, 20)
    print 'COM: Guess what I think?'
    inputnum = int(raw_input())
    guessNum(inputnum, randnum)
    
if __name__ == '__main__':

    print '*' * 70
    print 'This is small game for guess number. '
    print 'The range of number you guess should between %d and %d.' % (0, 20)
    print 'Press Enter to continue...'
    raw_input()
    print '*' * 70

    main()
