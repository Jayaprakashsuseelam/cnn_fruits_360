# reducer.py
import sys

unique_users = set()

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        continue
    user, count = data
    unique_users.add(user)

print(f'Number of unique listeners: {len(unique_users)}')
