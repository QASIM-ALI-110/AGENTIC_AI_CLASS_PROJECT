import time

def countdown_timer(seconds):
    print(f"Countdown starting from {seconds} seconds.")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Convert total seconds into minutes and seconds
        timeformat = f'{mins:02d}:{secs:02d}'  # Format time as mm:ss
        print(timeformat, end='\r')  # Print the time, overwrite the previous output
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("00:00\nTime's up!")

# User input for the countdown time in seconds
try:
    total_seconds = int(input("Enter the time in seconds for countdown: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number.")
