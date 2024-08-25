import psutil
import threading
import time

class PerformanceMonitor:
    def __init__(self, label):
        self.label = label
        self.running = True
        self.thread = threading.Thread(target=self.update_metrics, daemon=True)
        self.thread.start()

    def update_metrics(self):
        while self.running:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_usage = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/').percent
            self.label.config(text=f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}%")
            time.sleep(1)

    def stop(self):
        self.running = False
        self.thread.join()
