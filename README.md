# Monitor-System
The Monitor tool is a comprehensive application for managing and monitoring processes on a Windows system. It provides functionalities similar to Process Hacker, allowing users to view and manipulate processes, monitor system performance, and customize the tool’s appearance.


Features
Process Management:

View Processes: Displays a list of running processes with details like PID (Process ID), name, CPU usage, and memory usage.
Right-Click Options: Users can perform various actions on processes via a context menu:
Terminate Process: Ends the selected process.
Create Dump File: Generates a dump file for the selected process.
Inject DLL: Allows users to inject a DLL into the selected process.
Suspend/Resume Process: Suspends or resumes the selected process.
Set Priority: Changes the priority of the selected process.
Set Affinity: Sets the CPU affinity for the selected process.
Open File Location: Opens the directory containing the executable of the selected process.
View Handles/Modules/Network Connections/Threads: Provides detailed information about the process's handles, loaded modules, network connections, and threads.
Search for Malware: Checks the process for known malware indicators.
Dump Memory: Dumps the memory of the selected process.
Export Process Info: Exports detailed information about the selected process to a text file.
Monitor Process Performance: Starts monitoring the performance of the selected process.
Performance Monitoring:

Real-Time Metrics: Displays real-time CPU usage, memory usage, and disk usage on the Performance tab.
Continuous Update: Performance metrics are updated every second.
Settings and Customization:

Light/Dark Mode: Allows users to switch between light and dark modes for the UI.
Export Path: Users can set the path for exporting process lists to CSV files.
Internet Tab (Placeholder):

Graphical Representation: Intended to display network usage or other internet-related metrics. This feature is currently a placeholder and can be enhanced to show detailed network activity.
Error Handling:

Informative Messages: Provides feedback on actions and errors using message boxes, including success or failure notifications for various operations.
Code Structure
settings.json:

Stores user preferences, such as the mode (light or dark) and export file path.
process_utils.py:

Contains functions for managing processes, including:
Updating the process list
Terminating, suspending, or resuming processes
Creating dump files and injecting DLLs
Viewing handles, modules, network connections, and threads
Exporting process information
performance_monitor.py:

Contains the PerformanceMonitor class, which handles real-time updates for CPU, memory, and disk usage metrics.
main.py:

The core file that integrates the GUI with functionality:
UI Setup: Creates the main window and tabs using customtkinter.
Process List Management: Updates the list of processes and handles right-click context menu actions.
Settings Management: Implements light/dark mode and handles user settings.
Export Functionality: Exports process information to a CSV file.
Usage
Run the Application:

Launch main.py to start the Monitor tool.
View and Manage Processes:

Use the Process tab to view and interact with running processes.
Right-click on processes to access management options.
Monitor System Performance:

Check the Performance tab for real-time system metrics.
Customize Settings:

Access the Settings tab to change the UI mode and set export paths.
Use the Internet Tab:

View network-related information (currently a placeholder).
This tool is designed to be a powerful utility for users who need to monitor and manage system processes and performance. It combines modern UI elements with advanced process management capabilities, offering a user-friendly and feature-rich experience.

Some Of the options wont work since i havent had the time to update or fix them. 
![image](https://github.com/user-attachments/assets/3f5d19fa-4351-44f8-9f33-4d9eac69a6ea)
![image](https://github.com/user-attachments/assets/9cb2477d-9788-4c2d-8f10-6bd45bab81ce)
