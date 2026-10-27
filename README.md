
# DevQuest AI 🚀

An interactive coding practice and developer learning dashboard built with Python and Streamlit.

## Features

- Interactive developer dashboard
- Python coding challenges
- SQL practice
- Debugging challenges
- XP and achievement tracking
- Leaderboard
- Python Code Reviewer with syntax error detection, hints, suggested corrections, and rule-based explanations
- SQLite-based progress storage

## Tech Stack

- Python
- Streamlit
- SQLite

## Project Structure

- `app.py` - Main Streamlit application
- `ai_reviewer.py` - Code review functionality
- `code_runner.py` - Coding challenge execution
- `storage.py` - Database and progress management
- `requirements.txt` - Python dependencies

## Installation

1. Clone this repository.
2. Open the project folder in your terminal.
3. Create a Python virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment on Windows:

   ```powershell
   .venv\Scripts\activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

7. Open `http://localhost:8501` in your browser.

## Current Limitations

- The Code Reviewer uses local syntax checks and rule-based explanations, not a generative AI model.
- Suggested corrections cover only certain common syntax errors.
- The reviewer does not execute submitted code or guarantee logical correctness.
- The coding challenge runner is intended for local development and is not a secure sandbox.
- Progress is stored locally in SQLite; cloud synchronization is not implemented.

## Future Improvements

- Generative AI-powered code suggestions
- More coding challenges
- Enhanced performance analytics
- Cloud deployment

## Author

Likhitha Sri Aparna Bethineedi

Computer Science Graduate | Python Developer | Web Development Enthusiast
