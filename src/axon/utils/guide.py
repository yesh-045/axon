from pathlib import Path


def load_guide():
    """Load the project guide from axon.md if it exists."""
    guide_path = Path.cwd() / "axon.md"
    if guide_path.exists():
        return guide_path.read_text(encoding="utf-8").strip()
    return None
