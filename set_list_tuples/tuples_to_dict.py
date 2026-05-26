#"Problem 4: Group Ports by Service"

services = [
    ('web', 80),
    ('web', 443),
    ('db', 5432),
    ('db', 3306),
    ('cache', 6379),
    ('web', 8080)
]

'''{
    'web': [80, 443, 8080],
    'db': [5432, 3306],
    'cache': [6379]
}'''
from collections import defaultdict

my_server_list=defaultdict(list)



for server, port in services:
    my_server_list[server].append(port)


print(my_server_list)  


'''alternate solution'''


my_new_server_list={}

for server, port in services:
    if server not in my_new_server_list:
        my_new_server_list[server] =[]

    my_new_server_list[server].append(port)


print(my_new_server_list)  
