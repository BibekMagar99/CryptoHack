import base64
a="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
b=bytes.fromhex(a)
b=base64.b64encode(b).decode()
print(b)
