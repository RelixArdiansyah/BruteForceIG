import os, rich
from rich.panel import Panel
from rich import print as KenXinDev

def Banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = """[bold red]●[bold yellow] ●[bold green] ●[/]
    [bold red]______ __           ____  ______       ________             
    ___  //_/_____________  |/ /__(_)_________  __ \\_______   __
    __  ,<  _  _ \\_  __ \\_    /__  /__  __ \\_  / / /  _ \\_ | / /
    _  /| | /  __/  / / /    | _  / _  / / /  /_/ //  __/_ |/ / 
    [bold white]/_/ |_| \\___//_/ /_//_/|_| /_/  /_/ /_//_____/ \\___/_____/

        [underline red] BruteForce Instagram - Coded by KenXinDev[/]
"""
    KenXinDev(Panel(logo, width=80, style="bold bright_black"))

if __name__ == "__main__":
    Banner()
    KenXinDev(Panel("[bold white]Script ini masih dalam pengembangan mohon bersabar, script ini akan rilis pada tanggal 30 maret 2025[/]", width=80, style="bold bright_black"))
