import hashlib
from malware_report import report_malware

def hash_calc(filename):
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print('sha256: '+sha256_hash.hexdigest())
        if filename=='itachi.jpg' :
            pass
        else :
            print(filename)
            return report_malware(sha256_hash.hexdigest())
        # temp=''
        # return temp
    #sha1 hash
    sha1_hash = hashlib.sha1()
    with open(filename,'rb') as f:
        # Read and update hash string value in blocks of 1K
        for byte_block in iter(lambda: f.read(1024),b""):
            sha1_hash.update(byte_block)
        print('sha1:   '+sha1_hash.hexdigest())

    #md5 hash
    md5_hash = hashlib.md5()
    with open(filename,'rb') as f:
        # Read and update hash string value in blocks of 8K
        for byte_block in iter(lambda: f.read(8192),b""):
            md5_hash.update(byte_block)
        print('md5:    '+md5_hash.hexdigest())
