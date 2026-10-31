# DevQuest AI 🚀

DevQuest AI is an interactive coding-practice and developer-learning dashboard built with Python, Streamlit, and SQLite. It brings coding challenges, progress tracking, and local code-review helpers into one application.

## Features

- Interactive dashboard with XP and completion progress
- Coding quests across Python, SQL, Debugging, Data Structures & Algorithms (DSA), and Web Development
- Quest levels, hints, starter code, solutions, and explanations
- Python challenge execution against predefined test cases
- SQL answer validation
- HTML, CSS, and JavaScript pattern-based challenge validation
- Local Python and SQL code-review feedback
- XP, achievements, accepted/completed quest tracking, and leaderboard
- SQLite-backed local progress storage

## Tech stack

- Python
- Streamlit
- SQLite
- Python standard library (`ast`, `sqlite3`, `html.parser`, `subprocess`, etc.)

## Run locally

1. Clone the repository:
   ```bash
   git clone https://github.com/aparnabethineedi04/DevQuest-AI.git
   cd DevQuest-AI
   ```

2. Create and activate a virtual environment (Windows PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:
   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Project structure

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit interface and application flow |
| `storage.py` | SQLite progress and leaderboard storage |
| `code_runner.py` | Runs Python quest solutions against test cases |
| `ai_reviewer.py` | Local Python/SQL syntax and rule-based review |
| `sql_checker.py` | SQL quest validation |
| `sql_quests.py` | SQL quest bank |
| `additional_quests.py` | Additional Python and debugging quests |
| `web_dsa_quests.py` | DSA quest bank |
| `web_dev_quests.py` | HTML, CSS, and JavaScript quest bank |
| `web_dev_checker.py` | Web Development answer validation |

## Notes and limitations

- The Python and SQL reviewer uses local syntax checks and rule-based feedback; it is not a generative AI model.
- Web Development validation checks for required HTML/CSS/JavaScript patterns. It does not run JavaScript in a browser.
- The Python challenge runner executes submitted code in a local subprocess. It is intended for local learning and is **not a secure sandbox**. Do not expose it to untrusted users on a public server without implementing proper isolation and resource limits.
- Progress is stored in a local SQLite database (`devquest.db`). The database is created automatically when the app starts and is excluded from Git.
- Cloud synchronization and persistent hosted storage are not included in the current version.

## Author

**Likhitha Sri Aparna Bethineedi**  
Computer Science Graduate | Python Developer | Web Development Enthusiast
