import requests
from rich.console import Console

console = Console()

def basic_vuln_scan(url):
    payloads = ["'", '"', "<script>alert(1)</script>", "../"]
    for payload in payloads:
        try:
            r = requests.get(url + payload, timeout=2)
            if "error" in r.text.lower() or "alert" in r.text:
                console.print(f"[yellow]Possible vulnerability with payload: {payload}[/yellow]")
        except:
            pass
    console.print("[bold green]Basic scan finished.[/bold green]")
