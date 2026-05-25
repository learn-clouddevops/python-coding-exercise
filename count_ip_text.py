#Extract all IP addresses from a block of text (no regex first, then with regex).

text = """
Server 192.168.1.1 connected to 10.0.0.5 at port 8080.
Failed connection from 256.300.1.1 (invalid IP).
Backup server at 172.16.0.100 is online.
Check logs at 10.10.10.10 and contact admin@example.com
Invalid: 999.999.999.999
Valid: 8.8.8.8
"""

my_ip_list =[]


def is_valid_ip(word):
    if word.count('.') != 3:
        return False
    
    parts = word.split('.')

    for part in parts:
        if not part.isdigit():
            return False
        
        num = int(part)
        if num < 0 or num > 255:
            return False
        

    return True

def split_text_words(text):
    words = text.split()
    print(words)

    for word in words:
        if is_valid_ip(word):
            my_ip_list.append(word)

    return my_ip_list        




result = split_text_words(text)
print(result)

