# axon (Beta)

[![PyPI version](https://badge.fury.io/py/axon-cli.svg)](https://badge.fury.io/py/axon-cli)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

![axon Demo](screenshot.gif)

Your agentic CLI developer.

## Overview

axon is an agentic CLI-based AI tool inspired by Claude Code, Copilot, Windsurf and Cursor. It's meant
to be an open source alternative to these tools, providing a similar experience but with the flexibility of
using different LLM providers (Anthropic, OpenAI, Google Gemini) while keeping the agentic workflow.

*axon is currently in beta and under active development. Please [report issues](https://github.com/geekforbrains/axon-cli/issues) or share feedback!*

## Features

- No vendor lock-in. Use whichever LLM provider you prefer.
- MCP support
- Easily switch between models in the same session.
- JIT-style system prompt injection ensures axon doesn't lose the plot.
- Per-project guide. Adjust axon's behavior to suit your needs.
- CLI-first design. Ditch the clunky IDE.
- Cost and token tracking.
- Per command or per session confirmation skipping.

## Roadmap

- Tests 😅
- More LLM providers, including Ollama

## Quick Start

Install axon.

```
pip install axon-cli
```

On first run, you'll be asked to configure your LLM providers.

```
axon
```

## Configuration

After initial setup, axon saves a config file to `~/.config/axon.json`. You can open and 
edit this file as needed. Future updates will make editing easier directly from within axon.

### MCP Support

axon supports Model Context Protocol (MCP) servers. You can configure MCP servers in your `~/.config/axon.json` file:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

MCP servers extend the capabilities of your AI assistant, allowing it to interact with additional tools and data sources. Learn more about MCP at [modelcontextprotocol.io](https://modelcontextprotocol.io/).

### Available Commands

- `/help` - Show available commands
- `/yolo` - Toggle "yolo" mode (skip tool confirmations)
- `/clear` - Clear message history
- `/model` - List available models
- `/model <num>` - Switch to a specific model (by index)
- `/usage` - Show session usage statistics
- `exit` - Exit the application

## Customization

axon supports the use of a "guide". This is a `axon.md` file in the project root that contains
instructions for axon. Helpful for specifying tech stack, project structure, development
preferences etc.

## Telemetry

axon uses [Sentry](https://sentry.io/) for error tracking and usage analytics. You can disable this by
starting with the `--no-telemetry` flag.

```
axon --no-telemetry
```

## Requirements

- Python 3.10 or higher
- Git (for undo functionality)

## Installation

### Using pip

```bash
pip install axon-cli
```

### From Source

1. Clone the repository
2. Install dependencies: `pip install .` (or `pip install -e .` for development)

## Development

```bash
# Install development dependencies
make install

# Run linting
make lint

# Run tests
make test
```

## Release Process

When preparing a new release:

1. Update version numbers in:
   - `pyproject.toml`
   - `src/axon/constants.py` (APP_VERSION)

2. Commit the version changes:
   ```bash
   git add pyproject.toml src/axon/constants.py
   git commit -m "chore: bump version to X.Y.Z"
   ```

3. Create and push a tag:
   ```bash
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

4. Create a GitHub release:
   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes "Release notes here"
   ```

5. Merge to main branch and push to trigger PyPI release (automated)

### Commit Convention

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Test additions or modifications
- `chore:` - Maintenance tasks (version bumps, etc.)
- `build:` - Build system changes
- `ci:` - CI configuration changes

## Links

- [PyPI Package](https://pypi.org/project/axon-cli/)
- [GitHub Issues](https://github.com/geekforbrains/axon-cli/issues)
- [GitHub Repository](https://github.com/geekforbrains/axon-cli)

## License

MIT
