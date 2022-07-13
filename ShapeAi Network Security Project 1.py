import hashlib

#using Hexdigest()
print(hashlib.md5("Adnan".encode('utf-8')).hexdigest())

#using digest()
print(hashlib.md5("Adnan".encode('utf-8')).digest())