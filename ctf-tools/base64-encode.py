import base64

s = input()

result = base64.b64encode(s.encode('utf-8'))

print(result)