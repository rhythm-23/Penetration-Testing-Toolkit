import socket
from rich.console import Console

console = Console()

def resolve_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[cyan]{domain}[/cyan] => [green]{ip}[/green]")
    except Exception as e:
        console.print(f"[red]DNS resolution failed: {e}[/red]")
