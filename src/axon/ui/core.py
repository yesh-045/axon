"""Core UI functions including banner and spinner management."""

from rich.console import Console
from rich.padding import Padding

from axon.ui.colors import colors
from axon.ui.spinner import SpinnerManager

console = Console()
_spinner_manager = SpinnerManager(console)

                        
BANNER = """
 █████╗ ██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗██╔╝██╔═══██╗████╗  ██║
███████║ ╚███╔╝ ██║   ██║██╔██╗ ██║
██╔══██║ ██╔██╗ ██║   ██║██║╚██╗██║
██║  ██║██╔╝ ██╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                
"""


class SpinnerStyle:
    DEFAULT = f"[bold {colors.primary}]{{}}[/bold {colors.primary}]"
    MUTED = f"[{colors.muted}]{{}}[/{colors.muted}]"
    WARNING = f"[{colors.warning}]{{}}[/{colors.warning}]"
    ERROR = f"[{colors.error}]{{}}[/{colors.error}]"


def banner():
    """Display the application banner."""
    console.clear()
    banner_padding = Padding(BANNER, (0, 0, 0, 2))
    console.print(banner_padding, style=colors.primary)


def start_spinner(message: str = "", style: str = SpinnerStyle.DEFAULT):
    """Start the spinner with a message."""
    _spinner_manager.start(message, style)


def stop_spinner():
    """Stop the spinner."""
    _spinner_manager.stop()
