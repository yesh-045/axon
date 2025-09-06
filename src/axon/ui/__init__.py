"""Clean, simplified UI module."""

from axon.ui.core import BANNER, SpinnerStyle
from axon.ui.formatting import (
    create_inline_diff,
    create_shell_syntax,
    create_syntax_highlighted,
    create_unified_diff,
    format_server_name,
    get_command_display_name,
    get_file_language,
)
from axon.ui.manager import MessageType, OutputType, PanelType, UIManager
from axon.ui.special import usage as _usage
from axon.ui.spinner import SpinnerManager

_ui = UIManager()
_spinner = SpinnerManager(_ui.console)

# Core API
panel = _ui.panel
message = _ui.message
line = _ui.line
reset_context = _ui.reset_context

# Convenience methods
agent = _ui.agent
tool = _ui.tool
info = _ui.info
error = _ui.error
warning = _ui.warning
success = _ui.success
bullet = _ui.bullet
muted = _ui.muted
thinking = _ui.thinking

# Special panels
thinking_panel = _ui.thinking_panel
confirmation_panel = _ui.confirmation_panel
info_panel = _ui.info_panel
error_panel = _ui.error_panel

# Special functions
dump = _ui.dump
help = _ui.help



def usage(usage_data: dict):
    """Display usage statistics."""
    _usage(_ui, usage_data)


def banner():
    """Display the application banner."""
    from rich.padding import Padding

    from axon.ui.colors import colors

    _ui.console.clear()
    banner_padding = Padding(BANNER, (1, 0, 0, 2))
    _ui.console.print(banner_padding, style=colors.primary)
    _ui._last_output = None


def start_spinner(message: str = "", style: str = SpinnerStyle.DEFAULT):
    """Start the spinner with a message."""
    # Add spacing before spinner if coming after user input
    if _ui._last_output == OutputType.USER_INPUT:
        _ui.console.print()

    _spinner.start(message, style)
    _ui.set_spinner_active(True)


def stop_spinner():
    """Stop the spinner."""
    _spinner.stop()
    _ui.set_spinner_active(False)


console = _ui.console

__all__ = [
    # Core API
    "panel",
    "message",
    "line",
    "reset_context",
    # Messages
    "info",
    "error",
    "warning",
    "success",
    "bullet",
    "muted",
    "thinking",
    # Panels
    "agent",
    "tool",
    "thinking_panel",
    "confirmation_panel",
    "info_panel",
    "error_panel",
    # Special functions
    "dump",
    "help",
    "version",
    "update_available",
    "usage",
    # Utilities
    "banner",
    "start_spinner",
    "stop_spinner",
    "console",
    # Formatting
    "create_inline_diff",
    "create_shell_syntax",
    "create_syntax_highlighted",
    "create_unified_diff",
    "format_server_name",
    "get_command_display_name",
    "get_file_language",
    # Types
    "PanelType",
    "MessageType",
    "SpinnerStyle",
]
