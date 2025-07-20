from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    console.print(Panel.fit("[bold magenta]PENETRATION TESTING TOOLKIT[/bold magenta]\n[green]By YourName[/green]"), justify="center")
