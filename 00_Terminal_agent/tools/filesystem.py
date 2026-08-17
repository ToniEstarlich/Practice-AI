from pathlib import Path


WORKSPACE = Path(__file__).resolve().parent.parent / "workspace"


def safe_path(relative_path: str) -> Path:
    path = (WORKSPACE / relative_path).resolve()

    if WORKSPACE.resolve() not in path.parents and path != WORKSPACE.resolve():
        raise ValueError("Path outside TECHNE workspace is not allowed.")

    return path


def list_files():
    WORKSPACE.mkdir(exist_ok=True)

    files = []

    for path in WORKSPACE.rglob("*"):
        if path.is_file():
            files.append(
                str(path.relative_to(WORKSPACE))
            )

    return files


def read_file(path: str):
    file_path = safe_path(path)

    if not file_path.exists():
        raise FileNotFoundError(path)

    return file_path.read_text(
        encoding="utf-8"
    )


def write_file(path: str, content: str):
    file_path = safe_path(path)

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return f"File written: {path}"