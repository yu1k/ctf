import base64

s = "Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9"

result = base64.b64decode(s) 

print(result)