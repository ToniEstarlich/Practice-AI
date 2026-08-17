from agents.coder_agent import decide

from tools.filesystem import (
    list_files,
    read_file,
    write_file,
)

from tools.shell import run_python


MAX_STEPS = 15


def execute_action(action):

    action_type = action.get("action")

    if action_type == "list_files":

        return {
            "success": True,
            "files": list_files(),
        }

    if action_type == "read_file":

        content = read_file(
            action["path"]
        )

        return {
            "success": True,
            "path": action["path"],
            "content": content,
        }

    if action_type == "write_file":

        result = write_file(
            action["path"],
            action["content"],
        )

        return {
            "success": True,
            "result": result,
        }

    if action_type == "run_python":

        result = run_python(
            action["path"]
        )

        return {
            "success": result["return_code"] == 0,
            **result,
        }

    if action_type == "finish":

        return {
            "finished": True,
            "message": action.get(
                "message",
                "Finished."
            ),
        }

    return {
        "success": False,
        "error": f"Unknown action: {action_type}",
    }


def run_techne(task):

    history = []

    print("\n")
    print("=" * 60)
    print("🤖 TECHNE")
    print("=" * 60)
    print(f"Task: {task}")
    print("=" * 60)

    for step in range(1, MAX_STEPS + 1):

        print(f"\n--- STEP {step} ---")

        action = decide(
            task,
            history,
        )

        print("THOUGHT ACTION:")
        print(action)

        result = execute_action(action)

        print("TOOL RESULT:")
        print(result)

        history.append({
            "step": step,
            "action": action,
            "result": result,
        })

        if result.get("finished"):

            print("\n" + "=" * 60)
            print("✅ TECHNE FINISHED")
            print(result["message"])
            print("=" * 60)

            return result

    print("\n❌ TECHNE reached maximum steps.")

    return {
        "finished": False,
        "error": "Maximum steps reached.",
    }


if __name__ == "__main__":

    task = input(
        "\nWhat should TECHNE build?\n> "
    )

    run_techne(task)