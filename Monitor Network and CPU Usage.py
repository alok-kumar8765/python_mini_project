# This script utilizes the 'psutil' library to monitor system resources:
# specifically network input/output (upload/download speed) and CPU utilization.

import psutil
import time

# -----------------
# Monitor Network I/O (Upload/Download)
# -----------------

# Get the network I/O statistics *before* the measurement interval.
before = psutil.net_io_counters()

# Wait for 1 second to create a time interval for speed calculation.
time.sleep(1)

# Get the network I/O statistics *after* the measurement interval.
after = psutil.net_io_counters()

# Calculate the downloaded bytes (bytes received) by subtracting the 'before' count from the 'after' count.
download = after.bytes_recv - before.bytes_recv

# Calculate the uploaded bytes (bytes sent) by subtracting the 'before' count from the 'after' count.
upload = after.bytes_sent - before.bytes_sent

# Print the download speed in Bytes/sec.
print("Download Speed:", download, "Bytes/sec")

# Print the upload speed in Bytes/sec.
print("Upload Speed:", upload, "Bytes/sec")

# The image output shows example speeds:
# Download Speed: 86 Bytes/sec
# Upload Speed: 86 Bytes/sec

# -----------------
# Check CPU Usage
# -----------------

# Calculate the CPU usage percentage over a 1-second interval.
# The 'interval=1' parameter tells psutil to sample the CPU usage for 1 second.
cpu_percent = psutil.cpu_percent(interval=1)

# Print the calculated CPU usage percentage.
print("CPU Usage:", cpu_percent, "%")

# The image output shows an example usage:
# CPU Usage: 5.2 %