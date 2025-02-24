import os
from datetime import datetime

COUNTER_FILE = "receipt_counter.txt"  # File to store the last counter value


def get_receipt_number():
    # Get current date in DD-MM-YY format
    today_date = datetime.now().strftime("%d-%m-%y")

    # Check if the counter file exists
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            saved_date, last_counter = f.read().strip().split(",")

        # Reset counter if the date has changed
        if saved_date == today_date:
            counter = int(last_counter) + 1
        else:
            counter = 1  # Reset counter for a new day
    else:
        counter = 1  # First receipt of the day

    # Save the new counter value
    with open(COUNTER_FILE, "w") as f:
        f.write(f"{today_date},{counter}")

    # Format receipt number (e.g., 25-03-24-0001)
    receipt_number = f"{today_date}-{counter:04d}"
    return receipt_number


# Example usage
print(get_receipt_number())  # First call → 25-03-24-0001
print(get_receipt_number())  # Second call → 25-03-24-0002
