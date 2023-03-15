import rsa
import flask
(pubkey, privkey) = rsa.newkeys(512)
message = 'Haha go to hell!'.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
print(crypto)
import ngrok
app = flask.Flask(__name__)

@app.route("/")
def hello_world(request):
    gotit = request.args
    print(gotit)
    return "<p>Hello, World!</p>"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
