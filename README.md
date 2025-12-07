# Port Nuke 🔥

A simple CLI tool to kill processes that are hogging your ports.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Add the tool to your system PATH (so you can run `nuke` from anywhere):

   **Option A: Add to PATH via System Settings**
   - Copy the full path of this directory (e.g., `C:\Users\YourName\port-nuke`)
   - Press `Win + X` and select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables", select "Path" and click "Edit"
   - Click "New" and paste the directory path
   - Click "OK" on all dialogs
   - Restart your terminal

   **Option B: Quick PowerShell Command**
   ```powershell
   $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
   [Environment]::SetEnvironmentVariable("Path", "$currentPath;$PWD", "User")
   ```
   Run this in PowerShell from the port-nuke directory, then restart your terminal.

## Usage

Port Nuke has two commands:

### 1. Scan - View all listening processes

```bash
nuke scan
```

Displays a beautiful table showing all processes listening on ports with their Port, PID, and Name.

### 2. Kill - Kill a process on a specific port

```bash
nuke kill <port>
```

### Examples

```bash
# Scan all listening processes
nuke scan

# Kill process on port 3000
nuke kill 3000

# Kill process on port 8080
nuke kill 8080
```

## Output

- **scan**: Beautiful table with Port, PID, and Name columns
- **kill (port in use)**: Shows the process name and PID in RED, then kills it
- **kill (port free)**: Shows "Port {port} is free" in GREEN

## Permissions

On Windows, you may need to run the script with administrator privileges to kill certain processes.

## Requirements

- Python 3.7+
- psutil
- typer
- rich
