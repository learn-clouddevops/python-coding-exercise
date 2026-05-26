
#Deduplicate IPs While Preserving Order
ips = ['192.168.1.1', '10.0.0.5', '192.168.1.1', '172.16.0.1', '10.0.0.5', '8.8.8.8']

# Remove duplicates but keep the original order
# Expected: ['192.168.1.1', '10.0.0.5', '172.16.0.1', '8.8.8.8']


def count_unique_ip(ips):

    seen = set()
    my_ip = []
    for ip in ips:
        if ip not in seen:
            seen.add(ip)
            my_ip.append(ip)



    return my_ip



result = count_unique_ip(ips)
print(result)
