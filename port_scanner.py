import socket
from rich.console import Console

console = Console()

def port_scan(target, ports):
    console.print(f"[bold yellow]Scanning {target}[/bold yellow]")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            console.print(f"[green]Port {port} is open[/green]")
            sock.close()
        except:
            console.print(f"[red]Port {port} is closed[/red]")
