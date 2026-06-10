'''Given a list of log lines in this format:
"YYYY-MM-DD LEVEL service-name message"

Write a function count_errors_by_service(logs)
that returns a dict with count of ERROR lines 
per service name.

Ignore INFO, WARN, DEBUG lines entirely.

Input:
logs = [
    "2024-01-01 ERROR auth connection failed",
    "2024-01-01 INFO  auth service started",
    "2024-01-01 ERROR payment timeout",
    "2024-01-01 ERROR auth disk full",
    "2024-01-01 WARN  payment slow response",
    "2024-01-01 ERROR payment connection refused",
    "2024-01-01 DEBUG auth retrying"
]

Given a list of log lines in this format:
"YYYY-MM-DD LEVEL service-name message"

Write a function count_errors_by_service(logs)
that returns a dict with count of ERROR lines 
per service name.

Ignore INFO, WARN, DEBUG lines entirely.

Input:'''

logs = [
    "2024-01-01 ERROR auth connection failed",
    "2024-01-01 INFO  auth service started",
    "2024-01-01 ERROR payment timeout",
    "2024-01-01 ERROR auth disk full",
    "2024-01-01 WARN  payment slow response",
    "2024-01-01 ERROR payment connection refused",
    "2024-01-01 DEBUG auth retrying"
]



def count_log_levels(logs):

    count_log_level = {"ERROR": 0, "INFO": 0, "WARN": 0, "DEBUG": 0}  

    service_error_count = {}
    for line in logs:
        level = line.split()[1]
        if level in count_log_level:
            if level == "ERROR":
                service_name = line.split()[2]
                service_error_count[service_name] = service_error_count.get(service_name, 0) + 1
    return service_error_count

result = count_log_levels(logs)
print(result)
