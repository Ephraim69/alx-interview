#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line
must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

line list = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]
"""

import sys
import re
import signal

def print_stats(file_size, status_codes):
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(file_size, status_codes)
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

line_format = re.compile(r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')
file_size = 0
status_codes = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

try:
    for i, line in enumerate(sys.stdin, 1):
        match = line_format.match(line)
        if match:
            code, size = match.groups()
            file_size += int(size)
            if int(code) in status_codes:
                status_codes[int(code)] += 1
        if i % 10 == 0:
            print_stats(file_size, status_codes)
except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise
