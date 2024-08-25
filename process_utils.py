import psutil
import os
import ctypes
import tkinter as tk
from tkinter import messagebox, filedialog

def update_process_list(listbox):
    listbox.delete(0, tk.END)
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        listbox.insert(tk.END, f"PID: {proc.info['pid']} | Name: {proc.info['name']} | CPU: {proc.info['cpu_percent']}% | Memory: {proc.info['memory_info'].rss / (1024 * 1024):.2f} MB")

def taskkill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait()
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        return False, str(e)

def create_dump_file(pid):
    try:
        proc = psutil.Process(pid)
        dump_file_path = f"process_{pid}_dump.dmp"
        with open(dump_file_path, "wb") as f:
            f.write(proc.memory_full_info().rss)  # Placeholder for actual dump
        return dump_file_path
    except Exception as e:
        return None, str(e)

def inject_dll(pid, dll_path):
    if not dll_path:
        return False, "No DLL path provided"
    try:
        # Placeholder for DLL injection
        return True
    except Exception as e:
        return False, str(e)

def suspend_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.suspend()
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        return False, str(e)

def resume_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.resume()
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        return False, str(e)

def set_process_priority(pid, priority):
    try:
        proc = psutil.Process(pid)
        priority_map = {
            "idle": psutil.IDLE_PRIORITY_CLASS,
            "below_normal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
            "normal": psutil.NORMAL_PRIORITY_CLASS,
            "above_normal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            "high": psutil.HIGH_PRIORITY_CLASS,
            "realtime": psutil.REALTIME_PRIORITY_CLASS
        }
        proc.nice(priority_map.get(priority, psutil.NORMAL_PRIORITY_CLASS))
        return True
    except Exception as e:
        return False, str(e)

def set_process_affinity(pid, affinity_list):
    try:
        proc = psutil.Process(pid)
        proc.cpu_affinity(affinity_list)
        return True
    except Exception as e:
        return False, str(e)

def open_file_location(pid):
    try:
        proc = psutil.Process(pid)
        file_location = proc.exe()
        os.startfile(os.path.dirname(file_location))
        return True
    except Exception as e:
        return False, str(e)

def view_handles(pid):
    return "Handles viewing not implemented"

def view_modules(pid):
    return "Modules viewing not implemented"

def view_network_connections(pid):
    try:
        proc = psutil.Process(pid)
        connections = proc.connections()
        connection_info = "\n".join([f"Local: {conn.laddr} | Remote: {conn.raddr} | Status: {conn.status}" for conn in connections])
        return connection_info
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        return str(e)

def view_threads(pid):
    try:
        proc = psutil.Process(pid)
        threads = proc.threads()
        thread_info = "\n".join([f"Thread ID: {t.id} | CPU Time: {t.user_time + t.system_time}" for t in threads])
        return thread_info
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        return str(e)

def export_process_info(pid):
    try:
        proc = psutil.Process(pid)
        with open(f"process_{pid}_info.txt", "w") as file:
            file.write(f"PID: {pid}\n")
            file.write(f"Name: {proc.name()}\n")
            file.write(f"Executable Path: {proc.exe()}\n")
            file.write(f"Status: {proc.status()}\n")
            file.write(f"CPU Usage: {proc.cpu_percent()}%\n")
            file.write(f"Memory Usage: {proc.memory_info().rss / (1024 * 1024):.2f} MB\n")
            file.write(f"Threads: {len(proc.threads())}\n")
        return f"process_{pid}_info.txt"
    except Exception as e:
        return None, str(e)
