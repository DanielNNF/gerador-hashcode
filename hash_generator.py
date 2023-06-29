import os
import hashlib

def hash_file(filename):
    with open(filename, 'rb') as f:
        hasher = hashlib.sha256()
        while True:
            data = f.read(65536)
            if not data:
                break
            hasher.update(data)
        return hasher.hexdigest()

def hash_directory(path):
    hasher = hashlib.sha256()
    for root, dirs, files in os.walk(path):
        for file in files:
            filename = os.path.join(root, file)
            hasher.update(hash_file(filename).encode('utf-8'))
    return hasher.hexdigest()

root_path = "/exemplo" #Rota da pasta que deseja gerar um hash

root_hash = hash_directory(root_path)
print("Hash da pasta raiz:", root_hash)
