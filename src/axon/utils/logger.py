"""Debug logging configuration for axon CLI."""

import logging

from axon import ui


class UILogHandler(logging.Handler):
    """A logging handler that outputs messages to the UI's muted function."""

    def emit(self, record):
        # Only manipulate spinner if one is active
        # The spinner manager will handle the state internally
        from axon.ui.core import _spinner_manager

        spinner_was_active = _spinner_manager.spinner is not None
        if spinner_was_active:
            ui.stop_spinner()

        ui.muted(self.format(record))

        if spinner_was_active:
            ui.start_spinner()


def _is_allowed_module(name: str) -> bool:
    """Check if a logger name is from an allowed module."""
    # allowed = ["axon", "openai", "google_genai", "anthropic", "pydantic_ai"]
    allowed = ["axon"]
    return any(name == module or name.startswith(module + ".") for module in allowed)


def setup_logging(debug_enabled: bool):
    """Configure logging for debug mode or disable completely."""
    if debug_enabled:
        logging.root.setLevel(logging.DEBUG)

        handler = UILogHandler()
        handler.setFormatter(logging.Formatter("⚙︎ %(levelname)s (%(name)s): %(message)s"))
        handler.addFilter(lambda record: _is_allowed_module(record.name))

        logging.root.addHandler(handler)
    else:
        logging.disable(logging.CRITICAL)
