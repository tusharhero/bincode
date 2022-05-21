import bincode as bc

n = 0

while n <= 1023:
    name = "./images/" + str(n) + ".png"
    bc.mkbincodeimg(n).save(name)
    n += 1

##command to convert all the images to animated gif(only linux🐧)
#convert -delay 120 -loop 0 ./images/*.png 0to1023.gif