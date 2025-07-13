# ai-agent-in-python

Hi, this is my side project, you can feel free to fork and use it.

This is an AI agent that can edit, read, write, and run Python files, powered by Gemini API.

## Installation

To use this AI agent, follow these steps:

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```
2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
3.  **Install dependencies using uv:**
    ```bash
    pip install uv
    uv pip install -r requirements.txt
    ```

## UV Installation

[UV](https://github.com/astral-sh/uv) is a very fast Python package installer and resolver, written in Rust. You can install it using pip:

```bash
pip install uv
```

## Configuration

1.  **Create a `.env` file** in the root directory.
2.  **Add your Gemini API key** to the `.env` file. You can get your API key by going to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey):

    ```
    GEMINI_API_KEY='YOUR_API_KEY'
    ```

## Usage

1.  **Activate the virtual environment** (if you haven't already):

    ```bash
    source .venv/bin/activate
    ```
2.  **Run the `main.py` file** with your prompt:

    ```bash
    python3 main.py "your_prompt"
    ```

## Arguments

*   `--verbose`:  This argument prints the full command that the AI agent uses, providing more transparency and debugging information. Example:

    ```bash
    python3 main.py "your_prompt" --verbose
    ```