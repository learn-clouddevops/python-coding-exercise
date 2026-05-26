'''Build a Security Audit Log Parser that:

Counts log levels (INFO, WARN, ERROR)
Extracts and validates IPs
Masks sensitive data (emails, tokens)
Generates a summary report'''
import os 
import re 
from collections import Counter


def read_log_file(filename):
    if not os.path.isfile(filename):

        return 
    

    with open(filename,"r") as files:
        my_list =[]
        # for line in files:
        #     #     yield line
        #     my_list.append(line.strip())

        # return my_list
        for line in files:
            yield line.strip()

def ip_check(ips):
    if ips.count('.') != 3:
        return False
    
    new_part = ips.split('.')
    for p in new_part:
        if not p.isdigit():
            return False
        
        num = int(p)
        if not num > 0 and num < 255:
            return False
        
    return True    

        
        


def analyze_all(res):
    levels =[]
    my_ip=[]
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    for line in res:
        parts = line.split(maxsplit=3)
        if len(parts) >=3:
            levels.append(parts[2])



        ips = re.findall(pattern, line)
        for ip in ips:
            if ip_check(ip):
                my_ip.append(ip)

    


    return {
        'levels' : Counter(levels),
        'ips': my_ip
    }






filename = "security_audit.log"

result = analyze_all(read_log_file(filename))


print(f"levels : {result['levels']}")
print(f"ips : {result['ips']}")

print(type(result))
