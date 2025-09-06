APP_NAME = "axon"

MODELS = {
    "anthropic:claude-opus-4-0": {
        "pricing": {
            "input": 3.00,
            "cached_input": 1.50,
            "output": 15.00,
        },
        "context_window": 200_000,
    },
    "anthropic:claude-sonnet-4-0": {
        "pricing": {
            "input": 3.00,
            "cached_input": 1.50,
            "output": 15.00,
        },
        "context_window": 200_000,
    },
    "anthropic:claude-3-7-sonnet-latest": {
        "pricing": {
            "input": 3.00,
            "cached_input": 1.50,
            "output": 15.00,
        },
        "context_window": 200_000,
    },
    "google-gla:gemini-2.5-pro": {
        # Gemini pro has pricing tiers <= 200k / >200k
        # For now, using the lower pricing as unlikely to exceed 200k tokens
        # During a session
        #
        # TODO: Should make usage tracking dynamic to handle this
        "pricing": {
            "input": 1.25,
            "cached_input": 1.25,
            "output": 10.00,
        },
        "context_window": 2_000_000,
    },
    "google-gla:gemini-2.5-flash": {
        "pricing": {
            "input": 0.30,
            "cached_input": 0.035,
            "output": 2.50,
        },
        "context_window": 2_000_000,
    },
    "openai:o4-mini": {
        "pricing": {
            "input": 1.10,
            "cached_input": 0.275,
            "output": 4.40,
        },
        "context_window": 200_000,
    },
    "openai:o3-pro": {
        "pricing": {
            "input": 20.00,
            "cached_input": 20.00,
            "output": 80.00,
        },
        "context_window": 200_000,
    },
    "openai:o3": {
        "pricing": {
            "input": 10.00,
            "cached_input": 2.50,
            "output": 40.00,
        },
        "context_window": 200_000,
    },
    "openai:o3-mini": {
        "pricing": {
            "input": 1.10,
            "cached_input": 0.55,
            "output": 4.40,
        },
        "context_window": 200_000,
    },
    "openai:gpt-4.1": {
        "pricing": {
            "input": 2.00,
            "cached_input": 0.50,
            "output": 8.00,
        },
        "context_window": 1_047_576,
    },
    "openai:gpt-4.1-mini": {
        "pricing": {
            "input": 0.40,
            "cached_input": 0.10,
            "output": 1.60,
        },
        "context_window": 1_047_576,
    },
    "openai:gpt-4.1-nano": {
        "pricing": {
            "input": 0.10,
            "cached_input": 0.025,
            "output": 0.40,
        },
        "context_window": 1_047_576,
    },
}

# Non-destructive tools that should always be allowed without confirmation
ALLOWED_TOOLS = [
    "read_file",
    "find",
    "list_directory",
]

DEFAULT_USER_CONFIG = {
    "default_model": "",
    "env": {
        "ANTHROPIC_API_KEY": "your-anthropic-api-key",
        "OPENAI_API_KEY": "your-openai-api-key",
        "GEMINI_API_KEY": "your-gemini-api-key",
    },
    "mcpServers": {},
    "settings": {
        "allowed_tools": [],
        "allowed_commands": [
            "ls",
            "cat",
            "rg",
            "find",
            "pwd",
            "echo",
            "which",
            "head",
            "tail",
            "wc",
            "sort",
            "uniq",
            "diff",
            "tree",
            "file",
            "stat",
            "du",
            "df",
            "ps",
            "top",
            "env",
            "date",
            "whoami",
            "hostname",
            "uname",
            "id",
            "groups",
            "history",
        ],
    },
}
