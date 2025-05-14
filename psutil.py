import psutil
#pip install psutil
import time

def monitor(interval=5):
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        print(f"CPU Usage:{cpu}%\nMemory Usage:{ram}%")
        time.sleep(interval)

if __name__ == "__main__":
    monitor()
