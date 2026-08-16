import asyncio
import json
import os
import subprocess
from pathlib import Path

from ollama import AsyncClient


# ============================================================
# CONFIGURATION
# ============================================================

MODEL = "qwen3.6:latest"
WORKSPACE = Path.cwd().resolve()


# ============================================================
# TERMINAL TOOL
# ============================================================

class TerminalTool:

    async def run(self, command: str) -> str:
        """
        Execute a PowerShell command inside the Techne workspace.
        """

        print(f"\n[TERMINAL] {command}\n")

        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=WORKSPACE,
                capture_output=True,
                text=True,
                timeout=120,
            )

            output = ""

            if result.stdout:
                output += result.stdout

            if result.stderr:
                output += "\n[stderr]\n"
                output += result.stderr

            output += f"\n[exit code: {result.returncode}]"

            return output

        except subprocess.TimeoutExpired:
            return "Command timed out."


# ============================================================
# FILESYSTEM TOOL
# ============================================================

class FileSystemTool:

    def _safe_path(self, path: str) -> Path:
        """
        Prevent the agent from escaping the workspace.
        """

        target = (WORKSPACE / path).resolve()

        if not str(target).startswith(str(WORKSPACE)):
            raise ValueError("Access outside workspace is not allowed.")

        return target

    async def list_files(self) -> str:

        files = []

        for path in WORKSPACE.rglob("*"):

            if ".git" in path.parts:
                continue

            if "__pycache__" in path.parts:
                continue

            if path.is_file():
                files.append(
                    str(path.relative_to(WORKSPACE))
                )

        return "\n".join(files)

    async def read(self, path: str) -> str:

        target = self._safe_path(path)

        if not target.exists():
            return f"File does not exist: {path}"

        return target.read_text(
            encoding="utf-8"
        )

    async def write(
        self,
        path: str,
        content: str
    ) -> str:

        target = self._safe_path(path)

        target.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        target.write_text(
            content,
            encoding="utf-8"
        )

        return f"Created/updated: {path}"


# ============================================================
# TECHNE AGENT
# ============================================================

class TechneAgent:

    def __init__(self):

        self.client = AsyncClient()

        self.terminal = TerminalTool()

        self.files = FileSystemTool()

        self.history = []

    # --------------------------------------------------------
    # SYSTEM PROMPT
    # --------------------------------------------------------

    def system_prompt(self):

        return f"""
You are Techne, an autonomous software engineering agent.

You are running on Windows.

Your workspace is:

{WORKSPACE}

Your job is to create and modify software projects.

You can work with:

- Python
- FastAPI
- Flask
- HTML
- CSS
- JavaScript
- React
- APIs
- databases
- tests
- configuration files

You have access to terminal and filesystem tools.

IMPORTANT:

1. Work only inside the workspace.
2. Inspect existing files before modifying a project.
3. Create files when necessary.
4. Run tests after making changes.
5. Run applications when useful.
6. If a command fails, analyze the error and fix it.
7. Do not pretend that a command succeeded.
8. Keep the project organized.
9. Prefer simple maintainable code.
10. Explain what you are doing.

You are the first prototype of the Techne software-engineering system.

Your objective is not merely to generate code.

Your objective is:

UNDERSTAND → PLAN → BUILD → RUN → TEST → FIX
"""

    # --------------------------------------------------------
    # MODEL
    # --------------------------------------------------------

    async def ask_model(self, message: str):

        response = await self.client.chat(

            model=MODEL,

            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt()
                },

                *self.history,

                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        answer = response["message"]["content"]

        self.history.append({
            "role": "user",
            "content": message
        })

        self.history.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    # --------------------------------------------------------
    # COMMAND LOOP
    # --------------------------------------------------------

    async def run(self):

        print()
        print("=" * 60)
        print("                 TECHNE")
        print("          Autonomous Coding Agent")
        print("=" * 60)
        print()

        print(f"Workspace:")
        print(WORKSPACE)

        print()
        print("Type a task.")
        print("Examples:")
        print()
        print("  Create a Python FastAPI web application")
        print("  Create a portfolio website")
        print("  Inspect this project and explain its architecture")
        print("  Build a todo application")
        print()
        print("Commands:")
        print("  /files  - show project files")
        print("  /exit   - quit")
        print()

        while True:

            try:
                user_input = input("You > ").strip()

            except KeyboardInterrupt:
                print("\nBye.")
                break

            if not user_input:
                continue

            if user_input == "/exit":
                break

            if user_input == "/files":

                files = await self.files.list_files()

                print("\nPROJECT FILES\n")
                print(files)
                print()

                continue

            print("\nTechne > thinking...\n")

            answer = await self.ask_model(
                user_input
            )

            print(answer)
            print()


# ============================================================
# START
# ============================================================

async def main():

    agent = TechneAgent()

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())