'''Server List Comparison (Set Operations)'''

list_a = ['server1', 'server2', 'server3', 'server4']
list_b = ['server3', 'server4', 'server5', 'server6']



def common_server(list_a,list_b):
    list_a= set(list_a)
    list_b= set(list_b)
    common_count = list_a & list_b
    only_a = list_a - list_b
    only_b= list_b - list_a


    data = {
        "common" : common_count,
        "server_a": only_a,
        "server_b" : only_b

    }

    return data


result = common_server(list_a,list_b) 

print(result)


