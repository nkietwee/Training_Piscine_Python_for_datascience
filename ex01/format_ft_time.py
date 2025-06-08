"""
Write a script that formats the dates this way, of course your date will not be mine
as in the example but it must be formatted the same.

Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$

reference :
1 Jan 1970 (unix date) : https://www.unixtimestamp.com/
Current timestamp : https://www.geeksforgeeks.org/get-current-timestamp-using-python/
print format time (strftime) : https://www.geeksforgeeks.org/python-strftime-function/
F-string : https://builtin.com/data-science/python-f-string
"""

import time
import datetime

# January 1, 1970 is known as the Unix Epoch — the reference point for most computer systems to measure time.
# Get the current timestamp
timestamp = time.time()

# Format the timestamp with 4 decimal places
formatted_timestamp = f"{timestamp:,.4f}"

# Format the timestamp in scientific notation
scientific_timestamp = f"{timestamp:.2e}"

# Convert timestamp to human-readable date
date_str = datetime.datetime.fromtimestamp(timestamp).strftime("%b %d %Y")

# Print the result
print(f"Seconds since January 1, 1970: {formatted_timestamp} or {scientific_timestamp} in scientific notation$")
print(f"{date_str}$")