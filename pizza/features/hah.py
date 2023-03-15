from urllib import request, parse
data = parse.urlencode({"msg":"nothing"}).encode()
req =  request.Request("http://localhost:80", data=data, method="POST") # this will make the method "POST"
resp = request.urlopen(req)