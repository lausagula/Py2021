text = ["a","ABC","Rock2021"]

for palabra in text:
    cifrado = list(map(lambda x : chr(ord(x)+1),palabra))
    print(cifrado)



