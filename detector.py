import os
import time
import hashlib

def latest_download_file():
    # print('1')
    path = 'D:/SYSTEM DATA/Downloads/'
    os.chdir(path)
    files = sorted(os.listdir(path), key=os.path.getmtime)
    newest = files[-1]
    return newest

def hash():
    fname=''
    prev_time =time.perf_counter()
    new_time =time.perf_counter()
    while 1:
        new_time = time.perf_counter()
        if new_time - prev_time > 2.0 :
            prev_time = new_time
            newest=latest_download_file()
            if fname==newest:
                pass
            else : 
                fname=newest
                filename = fname
                return filename
                # sha256_hash = hashlib.sha256()
                # with open(filename,"rb") as f:
                #     # Read and update hash string value in blocks of 4K
                #     for byte_block in iter(lambda: f.read(4096),b""):
                #         sha256_hash.update(byte_block)
                #     print('sha256: '+sha256_hash.hexdigest())

                # #sha1 hash
                # sha1_hash = hashlib.sha1()
                # with open(filename,'rb') as f:
                #     # Read and update hash string value in blocks of 1K
                #     for byte_block in iter(lambda: f.read(1024),b""):
                #         sha1_hash.update(byte_block)
                #     print('sha1:   '+sha1_hash.hexdigest())

                # #md5 hash
                # md5_hash = hashlib.md5()
                # with open(filename,'rb') as f:
                #     # Read and update hash string value in blocks of 8K
                #     for byte_block in iter(lambda: f.read(8192),b""):
                #         md5_hash.update(byte_block)
                #     print('md5:    '+md5_hash.hexdigest())
                # print('\n')

hash()

