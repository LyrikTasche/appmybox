from fileinput import filename
import random
from timeit import repeat

filename = "generated"
myfile = open(filename, "w")

url = "http/www.appmybox.com/mobile/?4102&00194"

# Change the number after range to set the number off links to be generated
for i in range(10):
    first = chr(random.randint(ord("A"), ord("Z")))
    second = chr(random.randint(ord("A"), ord("Z")))
    third = chr(random.randint(ord("A"), ord("Z")))
    thourd = chr(random.randint(ord("A"), ord("Z")))
    print(url+first+second+third+thourd)

# I would recommend to use the website qrbatch.com to generate the QR-Codes
