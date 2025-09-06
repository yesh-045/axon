"""Command handlers for axon CLI."""

from axon import ui
from axon.commands.clear import handle_clear
from axon.commands.dump import handle_dump
from axon.commands.help import handle_help
from axon.commands.model import handle_model
from axon.commands.usage import handle_usage
from axon.commands.yolo import handle_yolo

__all__ = [
    "handle_clear",
    "handle_dump",
    "handle_help",
    "handle_model",
    "handle_usage",
    "handle_yolo",
    "handle_command",
]


async def handle_command(user_input: str, message_history=None) -> bool:
    """Handle slash commands. Returns True if command was handled."""
    if not user_input.startswith("/"):
        return False

    parts = user_input.split()
    command = parts[0]
    args = parts[1:] if len(parts) > 1 else []

    handlers = {
        "/dump": lambda: handle_dump(message_history),
        "/yolo": handle_yolo,
        "/model": lambda: handle_model(args),
        "/usage": handle_usage,
        "/clear": lambda: handle_clear(message_history),
        "/help": handle_help,
    }

    handler = handlers.get(command)
    if handler:
        await handler()
        return True

    ui.line()
    ui.error(f"Unknown command: {command}")
    ui.muted("Use /help to see available commands")

    return True
