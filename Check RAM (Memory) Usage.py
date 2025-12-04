# This script uses the 'psutil' library to check and display system RAM usage
# (total, available, used) in a human-readable format (Gigabytes).

import psutil

# Get the system's virtual memory statistics.
memory = psutil.virtual_memory()

# -----------------
# Helper Function
# -----------------
def convert_bytes(size):
    # Purpose: Convert bytes to Gigabytes (GB).
    # Input: size (integer, in bytes)
    # Output: gb (float, in Gigabytes)

    # Convert bytes to GB by dividing by (1024 * 1024 * 1024) or 1024 cubed.
    gb = size / (1024 ** 3)
    return gb

# -----------------
# Calculate and Display Usage
# -----------------
# Calculate Total RAM in GB.
total_gb = convert_bytes(memory.total)

# Calculate Available RAM in GB.
available_gb = convert_bytes(memory.available)

# Calculate Used RAM in GB.
used_gb = convert_bytes(memory.used)

# Print the Total RAM, formatted to 3 decimal places.
print(f"Total RAM: {total_gb:.3f} GB ")

# Print the Available RAM, formatted to 3 decimal places.
print(f"Available RAM: {available_gb:.3f} GB ")

# Print the Used RAM, formatted to 3 decimal places.
print(f"Used RAM: {used_gb:.3f} GB ")

# Print the RAM Usage percentage, provided directly by psutil.
print(f"RAM Usage: {memory.percent}%")
