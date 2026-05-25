#Extract HTTP status code and request path from Nginx logs.

log_line = '192.168.1.1 - - [15/Jan/2024:10:23:45 +0000] "GET /api/users HTTP/1.1" 200 1234'



def parse_nginx_log(log_line):
    parts = log_line.split('"')
    # print(parts)

    requests = parts[1]
    get_uri = requests.split()
    print(get_uri)



    status_code = parts[2]
    code = status_code.split()
    print(code)


    data ={
        "status" : get_uri[1],
        "httpcode" : code[0]
    }

    return data 



result = parse_nginx_log(log_line)    
print(result)


