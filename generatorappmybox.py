from fileinput import filename
from mailbox import linesep
import random
from timeit import repeat
import sys

url = "http/www.appmybox.com/mobile/?4102&00194"
nl = "\n"
# Change the number after range to set the number off links to be generated
for i in range(10):
    first = chr(random.randint(ord("A"), ord("Z")))
    second = chr(random.randint(ord("A"), ord("Z")))
    third = chr(random.randint(ord("A"), ord("Z")))
    thourd = chr(random.randint(ord("A"), ord("Z")))
    urlo = url+first+second+third+thourd
    urlt = urlo, nl
    # Print URLs into file
    with open("urls.txt", "a") as f:
        f.writelines(urlt)
# I would recommend to use the website qrbatch.com to generate the QR-Codes

# Made by Liande Guo aka LyrikTasche
