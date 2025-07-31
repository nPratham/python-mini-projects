'''This script checks the current time and prints a message based on the time of day.'''
import time
current_time = time.localtime()
if current_time.tm_hour >= 5 and current_time.tm_hour < 12:
    print("It's morning!")
elif current_time.tm_hour >= 12 and  current_time.tm_hour< 17:
    print("It's afternoon!")
elif current_time.tm_hour>= 17 and current_time.tm_hour < 21:
    print("It's evening!")
elif current_time.tm_hour >= 21 or current_time.tm_hour < 5:
    print("It's night!")
