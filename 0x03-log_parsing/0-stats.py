#!/usr/bin/python3
import sys
import signal

# Dictionary to keep track of status codes
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
lines_counter = 0

def print_stats(signal=None, frame=None):
    """ Print statistics """
    print("File size:", total_size)
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))
    if signal is not None:
        sys.exit()

# Handle CTRL + C
signal.signal(signal.SIGINT, print_stats)

try:
    for line in sys.stdin:
        parts = line.split()
        try:
            size = int(parts[-1])
            status = parts[-2]
            if status in status_codes:
                status_codes[status] += 1
            total_size += size
        except:
            pass

        lines_counter += 1
        if lines_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
