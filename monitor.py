import psutil

def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return {
        "CPU Usage": cpu,
        "Memory Usage": memory
    }
