import sys
sys.path.insert(1, '/home/tusharhero/Documents/bincode/')
import bincode as bc
from PIL import Image

def looplol():
    n = 1
    GIF = []
    while n < 69:
        GIF.append(bc.mkbincodeimg(n))
        n += 1
    return GIF
gif = looplol()
gif[0].save('temp_result.gif', save_all=True,optimize=False, append_images=gif[1:], loop=0)