import os
import time
import hashlib
from malware_report import report_malware
from hash_calculator import hash_calc
def latest_download_file():
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
                hashes=hash_calc(filename)
                return hashes
                
hash()

