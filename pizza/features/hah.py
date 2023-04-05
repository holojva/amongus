import requests
import rsa
dat = dict()
def doing_work(words) :
    num = 512
    the_biggest = 50
    while True :
        if len(words) > the_biggest :
            num *= 2
            the_biggest *= 2
        else :
            break
    (pubkey, privkey) = rsa.newkeys(num)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(pubkey.save_pkcs1('PEM'))

    with open('keys/privateKey.pem', 'wb') as d:
        d.write(privkey.save_pkcs1('PEM'))
    message = words.encode("latin-1")
    crypto = rsa.encrypt(message, pubkey)
    with open("keys/publicKey.pem", "rb") as image:
        f = image.read()
        pbk = bytearray(f)
    with open('keys/privateKey.pem', 'rb') as image:
        f = image.read()
        prk = bytearray(f)
    
    return [int.from_bytes(crypto, "big"), int.from_bytes(prk, "big"), int.from_bytes(pbk, "big"), len(prk), len(pbk), len(crypto)]
while True :
    inp = input("MSG:/")
    if "input" in dat.keys() :
        prev = dat["input"]
    else :
        dat["input"] = inp
        prev = inp
    if "start" in inp :
        dat["getter"] = inp.split()[1]
    r = requests.post('http://192.168.0.14:80', data = dat)
    if len(r.json()) < 6 :
        print(r.json()[0])
        

    else :
        cipher, priv, pub, prl, pbl, cry = r.json()
        cipher = int.to_bytes(cipher, cry, "big")
        priv = int.to_bytes(priv, prl, "big")
        gotit = rsa.PrivateKey.load_pkcs1(priv)
        hi = rsa.decrypt(cipher, gotit).decode("latin-1")
        if "Login is success" in hi :
            dat["logined_as"] = prev.split()[1]
            dat["pwd"] = prev.split()[2]
        
        print(hi)
    # else:
    #     print(r.json()[0])