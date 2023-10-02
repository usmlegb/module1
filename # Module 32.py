# Module 3_2 
current_time = int(input("Enter the current time (in hours, 0-23): "))

# Get the number of hours to wait for the alarm
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24

# Display the alarm time on a 24-hour clock
print(f"The alarm will go off at {alarm_time:02d}:00")
