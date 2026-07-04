# pydantic-validation-exercises

## Setup

Create a virtual environment and install dependencies into it (not globally):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

`requirements.txt` holds the runtime dependency (`pydantic`); `requirements-dev.txt` adds `pytest` on top for testing.

If using VS Code, select the `.venv` interpreter via **Ctrl+Shift+P → "Python: Select Interpreter"** so Pylance resolves imports correctly.

## Running tests

```powershell
pytest
```
