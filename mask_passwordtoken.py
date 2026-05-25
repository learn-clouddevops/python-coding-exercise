'''Mask Email Addresses
Mask password'''

import re

log_lines = [
    "2024-01-15 08:23:12 INFO Login from 192.168.1.100 user=admin@company.com session=sk_live_abc123",
    "2024-01-15 08:24:45 WARN Failed login from 203.0.113.5 user=hacker@evil.com attempts=3",
    "2024-01-15 08:25:10 ERROR API call from 10.0.0.50 key=prod_xyz789abc012",
]


def check_senstive_value(log_lines):
    for line in log_lines:
        line = re.sub( r'(token|key|password|session)=\S+', r'\1=****' , line)
        line = re.sub(r'(user)=\S+@\S+' , r'\1=****', line)
        print(line)




check_senstive_value(log_lines)
