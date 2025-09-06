from pydantic_ai import Tool

from axon.tools.find import find
from axon.tools.git import git_add, git_commit
from axon.tools.list import list_directory
from axon.tools.read_file import read_file
from axon.tools.run_command import run_command
from axon.tools.update_file import update_file
from axon.tools.write_file import write_file

TOOL_RETRY_LIMIT = 10


def create_tools():
    """Create Tool instances for all tools."""
    tools = [
        read_file,
        write_file,
        update_file,
        run_command,
        git_add,
        git_commit,
        find,
        list_directory,
    ]

    return [Tool(tool, max_retries=TOOL_RETRY_LIMIT) for tool in tools]
