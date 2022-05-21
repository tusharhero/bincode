import bincode as bc

n = 0

while n <= 64:
    name = "./images/" + str(n) + ".png"
    bc.mkbincodeimg(n).save(name)
    n += 1