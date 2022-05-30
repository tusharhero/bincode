import bincode as bc

for n in range(1024):
    name = "./images/" + str(n) + ".png"
    bc.mkbincodeimg(n).save(name)

# Command to convert all the images to animated gif(only linux🐧)
# convert -delay 120 -loop 0 ./images/*.png 0to1023.gif
