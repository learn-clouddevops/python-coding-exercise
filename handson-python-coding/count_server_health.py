'''Given a list of server dicts, return a summary dict with:
- total: total number of servers
- healthy_count: count where status == "running"
- unhealthy: list of names where status != "running"
- avg_cpu: average cpu across ALL servers, 
           rounded to 2 decimal places
- critical: list of names where cpu > 90
            sorted alphabetically

Input:
servers = [
    {"name": "web-01", "status": "running",  "cpu": 45},
    {"name": "web-02", "status": "stopped",  "cpu": 92},
    {"name": "db-01",  "status": "running",  "cpu": 95},
    {"name": "db-02",  "status": "degraded", "cpu": 60},
    {"name": "cache",  "status": "running",  "cpu": 30}
]

Expected output:
{
    "total": 5,
    "healthy_count": 3,
    "unhealthy": ["web-02", "db-02"],
    "avg_cpu": 64.4,
    "critical": ["db-01", "web-02"]
}

Edge cases to handle:
- empty list → return {}
- all servers healthy → unhealthy = []
- no server above 90 cpu → critical = []'''


servers = [
    {"name": "web-01", "status": "running",  "cpu": 45},
    {"name": "web-02", "status": "stopped",  "cpu": 92},
    {"name": "db-01",  "status": "running",  "cpu": 95},
    {"name": "db-02",  "status": "degraded", "cpu": 60},
    {"name": "cache",  "status": "running",  "cpu": 30},
   
]


def server_components(servers):

    total_cpu = 0

    unique_server = set()
    healthy =[]
    unhealthy=[]
    critical=[]

    count_servers ={}

    if not servers:
        return {}

    for server in servers:
        
        

        if server["status"] == "running":
            healthy.append(server["name"])
        

        if server["status"] != "running":
            unhealthy.append(server["name"])

        total_cpu = total_cpu + server["cpu"]    

        if server["cpu"] > 90:
            critical.append(server["name"])

    # print(total_servers) 
    # print(unique_server)       

            

    # return {
    #     "total": len(servers),
    #     "healthy_count": sum(1 for server in servers if server["status"] == "running"),
    #     "unhealthy": [server["name"] for server in servers if server["status"] != "running"],
    #     "avg_cpu": round(sum(server["cpu"] for server in servers) / len(servers), 2) if servers else 0,
    #     "critical": sorted([server["name"] for server in servers if server["cpu"] > 90])
    # }
    print(total_cpu)
    return{
        "total" : len(servers),

        "healthy_count": len(healthy),

        "unhealthy" : unhealthy,
        "avg_cpu" : round(total_cpu / len(servers),2),
        "critical": sorted(critical)
    }
    




result = server_components(servers)
print(result)    
