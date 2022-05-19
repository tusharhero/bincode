#Generates bincodes which store binary numbers(for now just one number)

from PIL import Image

##create the base images

#This image is all white and each white box ⬜ is 0, which means this is 0
img0 = Image.new("1", (1000,100),1)

#This image is a small black box ⬛ and it is the block we are going to use denote 1
img1 = Image.new("1", (100,100))

##we need a function to convert a given number into binary
#I dont think this is a good idea, but i am going to try it anyway

##fist we need bin2int
def bin2int(binnum):#the bin must be inverted for this to work
    number = 0
    n = 0

    #all of the values of binary places, this is from left to right instead of right to left
    binnumvalues = [1,2,4,8,16,32,64,128,256,512,1024]

    #loops until the number fully complete
    while n < len(binnum):
        number += binnum[n]*binnumvalues[n]#number = binnum(1) * 2^place ...
        n += 1
    
    return number

##now lets learn more about it.

def int2bin(number):# https://en.m.wikipedia.org/wiki/Binary_number#Decimal_to_Binary
    q = number
    r = 0
    binnum = []
    n = 0
    while q > 0:
        r = q%2
        q = q//2
        binnum.append(r)
    return binnum
print(int2bin(4))






##dormant old code
'''
def int2bin(number):
    number = int(number)
    binnum = [0,0,0,0,0,0,0,0,0,0]
    guessnum = 0
    n = 0
    while guessnum < number:
        if binnum[n] == 1:
            binnum[n] = 0
            binnum[n+1] = 1
        if binnum[n] == 0:
            binnum[n] = 1
        n += 1
        guessnum = bin2int(binnum)
    while guessnum > number:
        if binnum[n] == 1:
            binnum[n] = 1
            binnum[n+1] = 0
        if binnum[n] == 0:
            binnum[n] = 0
        n -= 1
        guessnum = bin2int(binnum)
    return binnum
'''