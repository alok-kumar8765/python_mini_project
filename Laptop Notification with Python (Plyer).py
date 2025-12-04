# This script demonstrates how to send desktop notifications (alerts) using
# the 'plyer' library.

# Installation requirement (if running outside an environment where it's installed):
# pip install plyer

import time
from plyer import notification

# Check if the script is being run directly (not imported).
if __name__ == "__main__":
    # The purpose is to loop indefinitely, sending a notification every 10 seconds.
    while True:
        # Send the notification using the 'notify' function from plyer.
        notification.notify(
            title = "ALERT!!!",                          # The title of the notification pop-up.
            message = "Take a break! It has been an hour!", # The main content/message of the notification.
            timeout = 10                                 # How long the notification should stay visible (in seconds).
        )
        # Pause the loop for 10 seconds before sending the next notification.
        time.sleep(10)
