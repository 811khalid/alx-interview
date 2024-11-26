#!/usr/bin/python3
"""
Log Parsing
Reads log entries from standard input and computes metrics.
"""

import sys
import re


def output(log):
    """
    Helper function to display statistics.
    Prints the total file size and the count of each status code in ascending order.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regular expression for log entry validation
    regex = re.compile(
        r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*?\] "
        r"\"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$"
    )

    # Initialize counters and log data
    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)

            if match:
                # Extract status code and file size
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code frequency
                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1

                # Increment line count
                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    output(log)

    except KeyboardInterrupt:
        # Handle CTRL + C gracefully
        pass
    finally:
        # Output stats at the end
        output(log)
