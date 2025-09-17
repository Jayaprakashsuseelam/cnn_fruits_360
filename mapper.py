# mapper.py
import sys

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) == 5:
        user, trackid, genre, band, duration_sec = data
        print(f'{user}\t1')