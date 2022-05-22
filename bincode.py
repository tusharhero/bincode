#Generates bincodes which store binary numbers(for now just one number)

from PIL import Image

##create the base images

#This image is all white and each white box ⬜ is 0, which means this is 0
img0 = Image.new("1", (800,800),1)

#This image is a small black box ⬛ and it is the block we are going to use denote 1
img1 = Image.new("1", (100,100))


##coordinates for every block
locationy = [0]*8 + [100]*8 + [200]*8 + [300]*8 + [400]*8 + [500]*8 + [600]*8 + [700]*8
locationx = [0, 100, 200, 300, 400, 500, 600, 700]*8

##we need a function to convert a given number into binary
#I dont think this is a good idea, but i am going to try it anyway

##fist we need bin2int
def bin2int(binnum):#the bin must be inverted for this to work
    number = 0
    n = 0

    #all of the values of binary places, this is from left to right instead of right to left
    binnumvalues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968, 72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904, 9223372036854775808, 18446744073709551616]

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

def mkbincodeimg(number): #makes the bincode image :D
    n = 0
    binnum = int2bin(number) #converts the number into binary first
    bincode = img0.copy() # makes a copy of the image
    while n < len(binnum):#until the entire number is finished
        if binnum[n] == 1:#If the number is 1
            #locationx = (100*n)#get location of the spot
            bincode.paste(img1,(locationx[n],locationy[n]))#past black into the place
        n += 1
    return bincode

def rdbincodeimg(bincode):#reads the bincode image 
    #bincode = Image.open(bincode)
    bincodedata = bincode.load()# loads the bincode
    n = 0
    binnum = []
    color = 0
    while n < 8:#a bincode (for now) contains 8 bits
        color = bincodedata[(100*(n+1)-50),0]#100*(n+1)-50  #This gets the color values of each bit.
        #color = bincodedata[locationy[n],locationx[n]]
        #print(color)
        if color > 0:#if the color is not 0 then it will append a 0 into the binnum
            binnum.append(0)
        if color == 0:#if it is 0 then it will append a 1 into the bincode
            binnum.append(1)
        n += 1
    #number = bin2int(binnum) #We have to make design decision. So I have commented this for now.
    return binnum

def opbincode(dir):#a function for opening bincodes and converting them to 1 bit format
    bincode = Image.open(dir)
    bincode = bincode.convert("1")
    return bincode