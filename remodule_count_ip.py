#Extract all IP addresses from a block of text (no regex first, then with regex).


import re


text = """
Server 192.168.1.1 connected to 10.0.0.5 at port 8080.
Failed connection from 256.300.1.1 (invalid IP).
Backup server at 172.16.0.100 is online.
Check logs at ab.10.10.10 and contact admin@example.com
Invalid: 999.999.999.999
Valid: 8.8.8.8
"""

my_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
my_ip_list =[]


def is_valid_ip(ip):
    check_ip = ip.count('.')


    parts = ip.split('.')

    if check_ip != 3:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False

        num = int(part)
        if not (num >=0 and num <=255):
            return False


    return True    

   

   
   


def find_ip_in_text(text):
    
    potential_ip = re.findall(my_regex, text)

    for ip in potential_ip:
        if is_valid_ip(ip):
            my_ip_list.append(ip)



    return my_ip_list   
        


result = find_ip_in_text(text)
print(result)

