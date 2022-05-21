# 0to1023
This folder contains the code which was used to generate the GIF you see in the README of this repository.

## Contents
### 0to1023.py
This script generates all the .PNG bincodes.
### images
This folder contains all the .PNG barcodes.

### 0to1023.gif
This is the gif which is generated using 

`convert -delay 120 -loop 0 ./images/*.png 0to1023.gif`

Linux🐧 command.