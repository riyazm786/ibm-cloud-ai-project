import psutil
import time

print("AI-Based Cloud Resource Monitoring System")
print("-----------------------------------------")

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print("--------------------------------")

    time.sleep(2)
