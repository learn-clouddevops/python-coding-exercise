'''[
  ['192.168.1.0/24', '192.168.2.0/24'],  ← Inner list 1
  ['10.0.0.0/16', '10.1.0.0/16'],        ← Inner list 2
  ['172.16.0.0/12']                      ← Inner list 3
]'''

'''['192.168.1.0/24', '192.168.2.0/24', '10.0.0.0/16', '10.1.0.0/16', '172.16.0.0/12']'''

subnets = [
    ['192.168.1.0/24', '192.168.2.0/24'],
    ['10.0.0.0/16', '10.1.0.0/16'],
    ['172.16.0.0/12']
]

def flatten_subnets(subnets):
    flat_list =[]

    for ip in subnets:
        for ip_name in ip:
            flat_list.append(ip_name)


    return flat_list    







result =  flatten_subnets(subnets)   
print(result)
