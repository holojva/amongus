import rsa
import flask
from base64 import b64encode
import json
with open("tss.json", "r") as f:
   data = json.load(f)

(pubkey, privkey) = rsa.newkeys(512)
message = 'Haha go to hell!'.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
print(crypto)
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
app = flask.Flask(__name__)
waitlist = dict()
@app.route("/", methods=['GET', 'POST'])
def hello_world(*args, **kwargs):
    gotit = dict(flask.request.form)["input"]
    print(gotit)
    logi = gotit.split()
    if len(logi) == 3 :
        if gotit[:5] == "login":

            if logi[1] in data["users"].keys():

                if logi[2] == data["users"][logi[1]]:

                    return doing_work("Login is successful, I can't describe how securely we send messages. If you want to know how, read about RSA.")
                
                return ["The password isn't right"]
            
            return ["There is no such user"]
        elif gotit[:8] == "register" :
            if logi[1] and logi[2]:
                data["users"][logi[1]] = logi[2]
        else :
            pass
    
    
    if logi[0] == "start" :
        
        if "getter" in dict(flask.request.form).keys() :
            if dict(flask.request.form)["getter"] in data["users"] :
                return doing_work("You are now connected to " + logi[1])
    if "getter" in dict(flask.request.form).keys() :
        if dict(flask.request.form)["getter"] in data["users"] :
            waitlist[[dict(flask.request.form)["getter"]]][dict(flask.request.form)["logined_as"]] = gotit
    if gotit == "check" :
        for i in waitlist[dict(flask.request.form)["logined_as"]] :
            for j in i :
                print(j)
    else :
        return ["Not a full command"]
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

