# Generates bincodes which can store binary numbers and also text.

import string

from PIL import Image

# Create the base images

# This image is all white and each white box ⬜ is 0, which means this is 0
img0 = Image.new("1", (800, 800), 1)

# This image is a small black box ⬛
# and it is the block we are going to use denote 1
img1 = Image.new("1", (50, 50))


def calculate_num_bits(bincode_size, block_size):
    return int(
        (bincode_size / block_size) ** 2
    )  # they are basically finding the number of blocks per side and then squaring them to find the number of blocks.


n_bits = calculate_num_bits(800, 50)
# print(n_bits)
# Coordinates for every block
def gen_locationy(side_of_block, number_of_bits):
    n = side_of_block
    m = number_of_bits
    locationy = []
    for i in range(m):
        locationy += [
            n * i
        ] * m  # How did i get these numbers? every 16 bits will have the same coordinate.
    return locationy


locationy = gen_locationy(50, 16)

# print(locationy)


def gen_locationx(side_of_block, number_of_bits):
    n = side_of_block
    m = number_of_bits
    locationx = [
        n * i for i in range(m)
    ] * m  # And every 16th bit will have the same x coordinate.
    return locationx


locationx = gen_locationx(50, 16)


# We need a function to convert a given number into binary
# I dont think this is a good idea, but i am going to try it anyway


def createbinnumvals(bits):
    binnumvalues = []
    n = 0
    while n < bits:
        binnumvalues.append((2 ** (n)))
        # print(binnumvalues)
        n += 1
    return binnumvalues


binnumvalues = createbinnumvals(256)


# First we need bin2int
def bin2int(binnum):  # the bin must be inverted for this to work
    number = 0
    n = 0

    # all of the values of binary places, this is from left to right instead of right to left
    # binnumvalues = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472, 274877906944, 549755813888, 1099511627776, 2199023255552, 4398046511104, 8796093022208, 17592186044416, 35184372088832, 70368744177664, 140737488355328, 281474976710656, 562949953421312, 1125899906842624, 2251799813685248, 4503599627370496, 9007199254740992, 18014398509481984, 36028797018963968, 72057594037927936, 144115188075855872, 288230376151711744, 576460752303423488, 1152921504606846976, 2305843009213693952, 4611686018427387904, 9223372036854775808, 18446744073709551616]
    # binnumvalues = createbinnumvals(256)

    # loops until the number fully complete
    while n < len(binnum):
        number += binnum[n] * binnumvalues[n]  # number = binnum(1) * 2^place ...
        n += 1

    return number


# Now lets learn more about it.


def int2bin(
    number,
):  # https://en.m.wikipedia.org/wiki/Binary_number#Decimal_to_Binary
    q = number
    r = 0
    binnum = []
    n = 0
    while q > 0:
        r = q % 2
        q = q // 2
        binnum.append(r)
    return binnum


def mkbincodeimg(binnum):
    """
    Makes the bincode image :D
    """

    # binnum = int2bin(number) #converts the number into binary first
    bincode = img0.copy()  # makes a copy of the image
    trimmed_binnum = binnum[0:n_bits]
    for index, item in enumerate(binnum):
        if item == 1:
            bincode.paste(img1, (locationx[index], locationy[index]))

    return bincode


def find_major_color(image):
    # finds the majority color
    height, width = image.size
    image = image.load()
    x = gen_locationx(1, height)
    y = gen_locationy(1, width)
    n_pixels = int(height * width)
    white = 0
    black = 0
    major_color = 0
    for n in range(n_pixels):
        color = image[x[n], y[n]]
        if color == 0:
            white += 1
        else:
            black += 1
    if white > black:  # determines which one is larger
        major_color = 0
    else:
        major_color = 1
    return major_color


def get_block(image, x, y, size):
    crop_size = (x, y, x + size, y + size)
    block = image.crop(crop_size)
    return block


def rdbincodeimg(bincode):  # reads the bincode image
    # bincode = Image.open(bincode)
    # bincodedata = bincode.load()  # loads the bincode
    binnum = []
    color = 0
    for n in range(n_bits):  # number of bits calculated using calculate_num_bits
        # This gets the color values of each bit.
        color = find_major_color(get_block(bincode, locationx[n], locationy[n], 50))
        # color = bincodedata[locationx[n], locationy[n]]  # uses the x and y locations we generated to decode the bincode
        if color > 0:  # if the color is not 0 then it will append a 0 into the binnum
            binnum.append(0)
        if color == 0:  # if it is 0 then it will append a 1 into the bincode
            binnum.append(1)
    return binnum


def correctbincode(bincode):
    """
    corects the image by resizing it and converting it to 1 bit format
    """
    size = (800, 800)
    bincode = bincode.resize(size, Image.ANTIALIAS)
    bincode = bincode.convert("1")
    return bincode


def opbincode(
    dir,
):  # a function for opening bincodes
    bincode = Image.open(dir)
    bincode = correctbincode(bincode)
    return bincode


def c2l(s, dic):
    """
    Figures out the placemenet in the dictionary.
    The code is aquired from https://gist.github.com/tusharhero/a6341333ec592a8d3aca06277fe04e42
    """

    for index, item in enumerate(dic):
        if s == item:  # If it finds the s is equal to the current character
            return index  # in the dictionary it returns it

    return 0  # If not found at all returns this


def bin_length_correction(binnum, l):
    corrbin = [0] * l

    for index, item in enumerate(binnum):
        corrbin[index] = item
    return corrbin


txtindex = [
    " ",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    ":",
    "/",
    ".",
]
txtindex_divided = [
    [" ", "b", "c", "d", "e", "f", "g"],
    ["h", "i", "j", "k", "l", "m", "n"],
    ["o", "p", "q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z", "a", "1"],
    ["2", "3", "4", "5", "6", "7", "8"],
    ["9", "0", ":", "/", "."],
]


def txt2bin(txt):
    """
    Converts text into binnum (Experimmental).
    """

    binnum = []

    for item in txt:
        diccode = int(c2l(item, txtindex) / 7)
        codeindic = c2l(item, txtindex_divided[diccode])
        binnum += bin_length_correction(int2bin(diccode), 3) + bin_length_correction(
            int2bin(codeindic), 3
        )

    return binnum


def bin2txt(binnum):
    """
    Converts binnum(Experimental) into text.
    """
    txt = ""
    binnum_individual_chars = []

    for n in range(0, len(binnum), 6):
        binnum_individual_chars.append(binnum[n : n + 6])

    for n in range(len(binnum_individual_chars)):
        diccode = bin2int(binnum_individual_chars[n][0:3])
        codeindic = bin2int(binnum_individual_chars[n][3:])
        txt += txtindex_divided[diccode][codeindic]

    txt = txt.strip()
    return txt


def txt2bincode(txt):
    """
    Directly converts txt to bincodes for convenience.
    """
    return mkbincodeimg(txt2bin(txt))


def bincode2txt(bincode):
    """
    Directly converts bincode to txt for convenience.
    """
    return bin2txt(rdbincodeimg(bincode))
