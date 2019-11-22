# import load_input
# content = load_input.load(2015, 4)
import hashlib
content = 'bgvyzdsv'
mdpass = hashlib.md5(str(content).encode("utf-8")).hexdigest()
i = -1
while not mdpass.startswith('00000'): # task 1
# while not mdpass.startswith('000000'): # task 2
    i +=1
    rawdata = str(content) + str(i)
    mdpass = hashlib.md5(rawdata.encode("utf-8")).hexdigest()
print(mdpass)
print(i)
