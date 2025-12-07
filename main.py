import psutil
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


def find_process_on_port(port: int):
    """Find the process listening on the given port."""
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port and conn.status == 'LISTEN':
            try:
                process = psutil.Process(conn.pid)
                return process
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return None


@app.command()
def scan():
    """Scan and display all processes listening on ports."""
    table = Table(title="Listening Processes", show_header=True, header_style="bold magenta")
    table.add_column("Port", style="cyan", justify="right")
    table.add_column("PID", style="yellow", justify="right")
    table.add_column("Name", style="green")
    
    listening_processes = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            try:
                process = psutil.Process(conn.pid)
                listening_processes.append({
                    'port': conn.laddr.port,
                    'pid': conn.pid,
                    'name': process.name()
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    # Sort by port number
    listening_processes.sort(key=lambda x: x['port'])
    
    for proc in listening_processes:
        table.add_row(str(proc['port']), str(proc['pid']), proc['name'])
    
    console.print(table)
    console.print(f"\nTotal: {len(listening_processes)} listening processes", style="bold")


@app.command()
def kill(port: int):
    """Kill the process using the specified port."""
    process = find_process_on_port(port)
    
    if process:
        pid = process.pid
        name = process.name()
        console.print(f"Killing process {name} (PID: {pid})...", style="bold red")
        try:
            process.kill()
            console.print(f"Process killed successfully!", style="bold green")
        except psutil.AccessDenied:
            console.print(f"Access denied. Try running with administrator privileges.", style="bold yellow")
        except Exception as e:
            console.print(f"Error killing process: {e}", style="bold red")
    else:
        console.print(f"Port {port} is free", style="bold green")


if __name__ == "__main__":
    app()
