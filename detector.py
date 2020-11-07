import os
import time
import hashlib
from malware_report import report_malware
from hash_calculator import hash_calc
from file_report import fileReport
from malware_report import report_malware

filePath = 'D:/SYSTEM DATA/Downloads/'
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
                continue
            else : 
                fname=newest
                filename = fname
                print('Hello')
                hashes=hash_calc(filename)
                return hashes
                # if fname != '':
                #     print(hashes)
                #     return hashes
                    # if hashes['response_code'] != 0 :
                    #     return hashes
                    # else : 
                    #     data = fileReport(filename, filePath)
                    #     prev_time =time.perf_counter()
                    #     new_time =time.perf_counter()
                    #     while 1:
                    #         # print('hello2')
                    #         new_time = time.perf_counter()
                    #         if new_time - prev_time > 70.0 :
                    #             reportFile=report_malware(data['scan_id'])
                    #             print(reportFile)
                    #             return reportFile
                
# hash()

