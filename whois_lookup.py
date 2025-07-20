import whois
from rich.console import Console

console = Console()

def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        console.print(f"[bold blue]Whois info for {domain}[/bold blue]")
        console.print(info)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
