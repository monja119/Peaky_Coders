
'''import bz2, os, sys


filename_in = "example.pdf"
filename_out = "compressed_data.bz2"

with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
    fout.write(fin.read())

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
print(f"Compressed size: {os.stat(filename_out).st_size}")

with bz2.open(filename_out, "rb") as fin:
    data = fin.read()
    print(f"Decompressed size: {sys.getsizeof(data)}")

'''


import os, sys, shutil, gzip


filename_in = "teste"
filename_out = "compressed_data.tar.gz"

with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:   
    shutil.copyfileobj(fin, fout)

#print(f"Uncompressed size: {os.stat(filename_in).st_size}")
#print(f"Compressed size: {os.stat(filename_out).st_size}")

with gzip.open(filename_out, "rb") as fin:
    data = fin.read()
    
    ##Aficher la taille du fichier Decompresser
    print(f"Decompressed size: {sys.getsizeof(data)}")

