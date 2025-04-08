import psutil
import time
import plyer
from plyer import notification

def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    time_left = battery.secsleft

    if plugged:
        status = "Charging"
    else:
        status = "Not Charging"

    # Convert seconds to readable time
    if time_left == psutil.POWER_TIME_UNLIMITED:
        time_str = "N/A"
    elif time_left == psutil.POWER_TIME_UNKNOWN:
        time_str = "Unknown"
    else:
        hours = time_left // 3600
        minutes = (time_left % 3600) // 60
        time_str = f"{hours}h {minutes}m"

    return percent, status, time_str

def notify_battery():
    percent, status, time_left = get_battery_status()
    
    message = f"Battery: {percent}%\nStatus: {status}\nTime left: {time_left}"
    print(message)  # Optional: Print to terminal

    # Show system notification
    notification.notify(
        title="🔋 Battery Status",
        message=message,
        timeout=10
    )

# 🕒 Check every 60 seconds (you can adjust)
while True:
    notify_battery()
    time.sleep(60)