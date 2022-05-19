#Generates bincodes which store binary numbers(for now just one number)

from PIL import Image

##create the base images

#This image is all white and each white box is 0, which means this is 0
img0 = Image.new("1", (1000,100),1)

#This image is a small black box and it is the block we are going to use denote 1
img1 = Image.new("1", (100,100))

img0.show()