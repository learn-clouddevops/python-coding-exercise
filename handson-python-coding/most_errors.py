'''Given a list of log lines in format:
"YYYY-MM-DD LEVEL service-name message"

Return a dict with:
- total_lines: total number of log lines
- error_services: list of unique service names 
                  that had at least one ERROR
                  sorted alphabetically
- most_errors: name of service with most errors
               if tie return alphabetically first
- clean_services: list of services that appear 
                  in logs but have ZERO errors
                  sorted alphabetically

Input:
logs = [
    "2024-01-01 ERROR auth timeout",
    "2024-01-01 INFO  auth started",
    "2024-01-01 ERROR payment failed",
    "2024-01-01 ERROR auth disk full",
    "2024-01-01 WARN  payment slow",
    "2024-01-01 ERROR payment timeout",
    "2024-01-01 INFO  orders started",
    "2024-01-01 DEBUG orders retrying"
]

Expected:
{
    "total_lines": 8,
    "error_services": ["auth", "payment"],
    "most_errors": "auth",
    "clean_services": ["orders"]
}

Edge cases:
- empty list → return {}
- no ERROR lines → error_services = [],
                   most_errors = None,
                   clean_services = all unique services
                   '''

############################
logs = [
    "2024-01-01 ERROR auth timeout",
    "2024-01-01 INFO  auth started",
    "2024-01-01 ERROR payment failed",
    "2024-01-01 ERROR auth disk full",
    "2024-01-01 WARN  payment slow",
    "2024-01-01 ERROR payment timeout",
    "2024-01-01 INFO  orders started",
    "2024-01-01 DEBUG orders retrying"
]

def most_errors(logs):

    error_apps = {}

    all_services = set()
    clean_service =[]

    

    if not logs:
        return {}

    for log in logs:
        parts = log.split()
        apps = parts[1]
        services = parts[2]


        all_services.add(services)

        if "ERROR" in log:
            error_apps[services] = error_apps.get(services,0) + 1


    for s in all_services:
        if s not in error_apps:
            clean_service.append(s)

    return {
    "total_lines": len(logs),
    "error_services": sorted(error_apps.keys()),
    "most_errors": max(error_apps, key=lambda x: error_apps[x]),
    "clean_services": sorted(clean_service)
}


result = most_errors(logs)
print(result)
