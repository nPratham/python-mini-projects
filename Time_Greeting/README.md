# Time of Day Greeter ⏰

This Python script prints a message based on the current time of day — morning, afternoon, evening, or night.

## 🧠 How It Works

The script uses the built-in `time` module to get the local system time. Based on the current hour (`tm_hour`), it classifies the time into one of four categories:

- **Morning:** 5:00 AM to 11:59 AM
- **Afternoon:** 12:00 PM to 4:59 PM
- **Evening:** 5:00 PM to 8:59 PM
- **Night:** 9:00 PM to 4:59 AM

It then prints a simple message like:

-It's evening!