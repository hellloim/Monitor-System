import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import customtkinter as ctk
import json
import os
from process_utils import *
from performance_monitor import PerformanceMonitor

# Load settings
with open('settings.json', 'r') as f:
    settings = json.load(f)

# Create main window
root = ctk.CTk()
root.title("Monitor")
root.geometry("1200x800")

# Create tabs
tab_control = ctk.CTkTabview(root)
performance_tab = tab_control.add("Performance")
settings_tab = tab_control.add("Settings")
internet_tab = tab_control.add("Internet")
tab_control.pack(expand=1, fill="both")

# Performance tab
performance_label = ctk.CTkLabel(performance_tab, text="CPU Usage: | Memory Usage: | Disk Usage: ")
performance_label.pack(pady=10)
performance_monitor = PerformanceMonitor(performance_label)

# Settings tab
light_mode_var = tk.BooleanVar(value=settings.get('light_mode', True))
light_mode_checkbox = ctk.CTkCheckBox(settings_tab, text="Light Mode", variable=light_mode_var, command=lambda: toggle_mode(light_mode_var))
light_mode_checkbox.pack(pady=10)
settings_label = ctk.CTkLabel(settings_tab, text="Mode: Light" if light_mode_var.get() else "Mode: Dark")
settings_label.pack(pady=10)

export_button = ctk.CTkButton(settings_tab, text="Export Process List to CSV", command=lambda: export_to_csv())
export_button.pack(pady=10)

# Internet tab
internet_label = ctk.CTkLabel(internet_tab, text="Internet usage graph will be here.")
internet_label.pack(pady=10)

# Process listbox
process_listbox = tk.Listbox(root, width=160, height=20)
process_listbox.pack(pady=20)
update_process_list(process_listbox)

# Right-click menu
def on_right_click(event):
    try:
        selected_text = process_listbox.get(process_listbox.curselection()[0])
        process_id = int(selected_text.split(' ')[1].strip())
        menu = tk.Menu(root, tearoff=0)
        menu.add_command(label="Terminate Process", command=lambda: handle_process_action(process_id, taskkill_process))
        menu.add_command(label="Create Dump File", command=lambda: handle_process_action(process_id, lambda pid: create_dump_file(pid)))
        menu.add_command(label="Inject DLL", command=lambda: handle_process_action(process_id, lambda pid: inject_dll(pid, filedialog.askopenfilename(title="Select DLL to Inject", filetypes=[("DLL files", "*.dll")]))))
        menu.add_command(label="Suspend Process", command=lambda: handle_process_action(process_id, suspend_process))
        menu.add_command(label="Resume Process", command=lambda: handle_process_action(process_id, resume_process))
        menu.add_command(label="Set Priority", command=lambda: handle_process_action(process_id, lambda pid: set_process_priority(pid, simpledialog.askstring("Set Process Priority", "Enter new priority (idle, below_normal, normal, above_normal, high, realtime):"))))
        menu.add_command(label="Set Affinity", command=lambda: handle_process_action(process_id, lambda pid: set_process_affinity(pid, simpledialog.askstring("Set Affinity", "Enter CPU affinity (comma-separated list of CPU indices):").split(','))))
        menu.add_command(label="Open File Location", command=lambda: handle_process_action(process_id, open_file_location))
        menu.add_command(label="View Handles", command=lambda: handle_process_action(process_id, view_handles))
        menu.add_command(label="View Modules", command=lambda: handle_process_action(process_id, view_modules))
        menu.add_command(label="View Network Connections", command=lambda: handle_process_action(process_id, view_network_connections))
        menu.add_command(label="View Threads", command=lambda: handle_process_action(process_id, view_threads))
        menu.add_command(label="Search for Malware", command=lambda: handle_process_action(process_id, search_for_malware))
        menu.add_command(label="Dump Memory", command=lambda: handle_process_action(process_id, lambda pid: dump_memory(pid)))
        menu.add_command(label="Export Process Info", command=lambda: handle_process_action(process_id, lambda pid: export_process_info(pid)))
        menu.add_command(label="Monitor Process Performance", command=lambda: handle_process_action(process_id, lambda pid: monitor_process_performance(pid)))
        menu.post(event.x_root, event.y_root)
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

process_listbox.bind("<Button-3>", on_right_click)

def toggle_mode(var):
    if var.get():
        root.tk_setPalette(background="#FFFFFF", foreground="#000000")
        settings_label.config(text="Mode: Light")
    else:
        root.tk_setPalette(background="#000000", foreground="#FFFFFF")
        settings_label.config(text="Mode: Dark")

def handle_process_action(pid, action):
    success, *msg = action(pid)
    if not success:
        messagebox.showerror("Error", msg[0])
    else:
        messagebox.showinfo("Success", f"Action completed successfully.")

def export_to_csv():
    try:
        with open(settings.get('export_file_path', 'process_list.csv'), 'w', newline='') as csvfile:
            fieldnames = ['PID', 'Name', 'CPU Usage (%)', 'Memory Usage (MB)']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
                writer.writerow({
                    'PID': proc.info['pid'],
                    'Name': proc.info['name'],
                    'CPU Usage (%)': proc.info['cpu_percent'],
                    'Memory Usage (MB)': proc.info['memory_info'].rss / (1024 * 1024)
                })
        messagebox.showinfo("Success", "Process list exported to CSV.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root.mainloop()
