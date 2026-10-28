
import streamlit as st

from storage import (
    initialize_database,
    load_progress,
    save_progress,
    save_player_score,
    get_leaderboard,
)
from ai_reviewer import review_code
from code_runner import run_python_tests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="DevQuest AI | Coding Adventure",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_database()


# ============================================================
# QUEST DATA
# ============================================================

QUESTS = [
    {
        "id": "python_starter",
        "title": "Python Starter",
        "icon": "🐍",
        "language": "Python",
        "difficulty": "Beginner",
        "xp": 50,
        "description": "Write a program that checks whether a number is even or odd.",
        "question": (
            "Read an integer from input and print 'Even' if it is "
            "divisible by 2. Otherwise, print 'Odd'."
        ),
        "hint": "Use int(input()), the modulo operator %, and if-else.",
        "starter_code": (
            "number = int(input())\n\n"
            "# Write your code below\n"
        ),
        "solution": (
            "number = int(input())\n\n"
            "if number % 2 == 0:\n"
            "    print('Even')\n"
            "else:\n"
            "    print('Odd')"
        ),
        "explanation": (
            "The modulo operator (%) returns the remainder. "
            "If number % 2 equals 0, the number is even."
        ),
        "tests": [
            {"input": "8\n", "expected": "Even\n"},
            {"input": "7\n", "expected": "Odd\n"},
            {"input": "0\n", "expected": "Even\n"},
            {"input": "-3\n", "expected": "Odd\n"},
        ],
    },
    {
        "id": "sql_explorer",
        "title": "SQL Explorer",
        "icon": "🗄️",
        "language": "SQL",
        "difficulty": "Beginner",
        "xp": 40,
        "description": "Retrieve all records from the employees table.",
        "question": (
            "Write an SQL query that retrieves every column and every "
            "row from a table named employees."
        ),
        "hint": "Use SELECT, *, and FROM.",
        "starter_code": "-- Write your SQL query here",
        "solution": "SELECT * FROM employees;",
        "explanation": (
            "SELECT * requests every column. FROM employees specifies "
            "the table from which records are retrieved."
        ),
        "tests": [],
    },
    {
        "id": "debug_detective",
        "title": "Debug Detective",
        "icon": "🕵️",
        "language": "Python",
        "difficulty": "Intermediate",
        "xp": 60,
        "description": "Find and fix a comparison bug in Python.",
        "question": (
            "The program should print 'Adult' when age is 18 or above, "
            "and 'Minor' otherwise. Find and fix the bug."
        ),
        "hint": (
            "The current condition excludes age 18. Check the comparison "
            "operator."
        ),
        "starter_code": (
            "age = int(input())\n\n"
            "if age > 18:\n"
            "    print('Adult')\n"
            "else:\n"
            "    print('Minor')"
        ),
        "solution": (
            "age = int(input())\n\n"
            "if age >= 18:\n"
            "    print('Adult')\n"
            "else:\n"
            "    print('Minor')"
        ),
        "explanation": (
            "The >= operator includes 18. The original > operator "
            "only matches numbers strictly greater than 18."
        ),
        "tests": [
            {"input": "18\n", "expected": "Adult\n"},
            {"input": "25\n", "expected": "Adult\n"},
            {"input": "17\n", "expected": "Minor\n"},
        ],
    },
]


# ============================================================
# LOAD SAVED PROGRESS
# ============================================================

progress = load_progress()

if not isinstance(progress, dict):
    progress = {}

xp = int(progress.get("xp", 0))
completed_quests = list(progress.get("completed_quests", []))
accepted_quests = list(progress.get("accepted_quests", []))


# ============================================================
# SESSION STATE
# ============================================================

if "username" not in st.session_state:
    st.session_state.username = "Player"

if "practice_results" not in st.session_state:
    st.session_state.practice_results = {}

if "practice_solutions_revealed" not in st.session_state:
    st.session_state.practice_solutions_revealed = {}

if "practice_hints_revealed" not in st.session_state:
    st.session_state.practice_hints_revealed = {}


# ============================================================
# STYLING — READABLE TEXT AND EDITORS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #100d22, #111827);
        color: #f8fafc;
    }

    [data-testid="stHeader"] {
        background: rgba(16, 13, 34, 0.98);
    }

    [data-testid="stToolbar"] {
        right: 1rem;
    }

    [data-testid="stSidebar"] {
        background: #111126;
        border-right: 1px solid #393052;
    }

    [data-testid="stSidebar"] * {
        color: #f1f5f9;
    }

    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp p,
    .stApp li,
    .stApp label,
    .stApp .stMarkdown {
        color: #f1f5f9;
    }

    .stApp textarea,
    .stApp input,
    .stApp [data-baseweb="input"] input,
    .stApp [data-baseweb="textarea"] textarea {
        background-color: #ffffff !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        caret-color: #111827 !important;
        border-color: #cbd5e1 !important;
    }

    .stApp textarea::placeholder,
    .stApp input::placeholder {
        color: #64748b !important;
        -webkit-text-fill-color: #64748b !important;
        opacity: 1 !important;
    }

    .stApp [data-baseweb="select"] > div {
        background-color: #ffffff;
        color: #111827;
    }

    .stButton > button {
        background-color: #6d4aff;
        color: #ffffff !important;
        border: 1px solid #8b75ff;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton > button p,
    .stButton > button span {
        color: #ffffff !important;
    }

    .stButton > button:hover {
        background-color: #5234d8;
        border-color: #b2a4ff;
    }

    .hero {
        padding: 25px;
        border-radius: 18px;
        background: linear-gradient(135deg, #39236b, #171d3b);
        border: 1px solid #51417b;
        margin-bottom: 20px;
    }

    .hero h1,
    .hero p {
        color: #ffffff !important;
    }

    .quest-card {
        padding: 20px;
        border-radius: 16px;
        background: #191d36;
        border: 1px solid #35304f;
        margin-bottom: 14px;
    }

    .small-muted {
        color: #cbd5e1 !important;
        font-size: 14px;
    }

    div[data-testid="stMetric"] {
        background: #1f213e;
        border: 1px solid #393454;
        padding: 15px;
        border-radius: 12px;
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    [data-testid="stExpander"] {
        border-color: #393454;
    }

    [data-testid="stCode"] {
        border: 1px solid #393454;
        border-radius: 8px;
    }

    [data-testid="stAlert"] p {
        color: inherit;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def save_current_progress():
    """Save existing progress and update the local leaderboard."""
    save_progress(
        xp,
        completed_quests,
        accepted_quests,
    )

    save_player_score(
        st.session_state.username,
        xp,
        len(completed_quests),
    )


def check_sql_answer(code):
    """Basic expected-query check; does not execute SQL."""
    normalized = " ".join(
        code.strip().rstrip(";").strip().lower().split()
    )

    return normalized in {
        "select * from employees",
        "select employees.* from employees",
    }


def run_quest_tests(quest, code):
    """Run Python tests or perform the basic SQL answer check."""
    if quest["language"] == "SQL":
        passed = check_sql_answer(code)

        return {
            "passed": 1 if passed else 0,
            "total": 1,
            "results": [
                {
                    "passed": passed,
                    "input": "SQL query check",
                    "expected": "SELECT * FROM employees;",
                    "actual": code.strip(),
                }
            ],
            "error": None,
        }

    return run_python_tests(
        code,
        quest["tests"],
        timeout=3,
    )


def show_test_results(result):
    """Display individual test results."""
    if result.get("error"):
        st.error(f"Execution error: {result['error']}")

    for index, item in enumerate(result.get("results", []), start=1):
        if item.get("passed", False):
            st.success(f"Test {index}: Passed")
        else:
            st.error(f"Test {index}: Failed")

        with st.expander(f"Test {index} details"):
            st.code(str(item.get("input", "")), language="text")
            st.write("**Expected output**")
            st.code(str(item.get("expected", "")), language="text")
            st.write("**Your output**")
            st.code(str(item.get("actual", "")), language="text")

    st.write(
        f"**Result: {result.get('passed', 0)}/"
        f"{result.get('total', 0)} tests passed.**"
    )

def render_practice_card(quest):
    """Render a practice challenge without changing saved XP."""
    quest_id = quest["id"]
    editor_key = f"practice_editor_{quest_id}"

    st.markdown(f"### {quest['icon']} {quest['title']}")
    st.write(quest["description"])
    st.caption(
        f"{quest['language']} · {quest['difficulty']} · "
        "Practice only — no XP awarded"
    )

    st.markdown("**Your challenge**")
    st.write(quest["question"])

    if editor_key not in st.session_state:
        st.session_state[editor_key] = quest["starter_code"]

    code = st.text_area(
        "Write or edit your solution",
        key=editor_key,
        height=220,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        check_clicked = st.button(
            "▶ Run & Check",
            key=f"practice_check_{quest_id}",
            use_container_width=True,
        )

    with col2:
        hint_clicked = st.button(
            "💡 Show Hint",
            key=f"practice_hint_{quest_id}",
            use_container_width=True,
        )

    with col3:
        solution_clicked = st.button(
            "📖 Show Solution",
            key=f"practice_solution_{quest_id}",
            use_container_width=True,
        )

    if hint_clicked:
        st.session_state.practice_hints_revealed[quest_id] = True

    if solution_clicked:
        st.session_state.practice_solutions_revealed[quest_id] = True

    if st.session_state.practice_hints_revealed.get(quest_id):
        st.info(f"**Hint:** {quest['hint']}")

    if check_clicked:
        try:
            with st.spinner("Checking your code..."):
                result = run_quest_tests(quest, code)

            st.session_state.practice_results[quest_id] = result

            if (
                result.get("total", 0) > 0
                and result.get("passed", 0) == result.get("total", 0)
                and not result.get("error")
            ):
                st.success(
                    "Excellent work! All tests passed. "
                    "Practice Mode does not award XP."
                )
            else:
                st.warning(
                    "Not quite there yet! Review the test results, "
                    "learn from the feedback, and try again."
                )

        except Exception as exc:
            st.session_state.practice_results[quest_id] = None
            st.error(f"Could not check this answer: {exc}")

    result = st.session_state.practice_results.get(quest_id)

    if result:
        show_test_results(result)

        passed_all = (
            result.get("total", 0) > 0
            and result.get("passed", 0) == result.get("total", 0)
            and not result.get("error")
        )

        if passed_all:
            st.success("Practice challenge passed!")
        else:
            st.markdown("#### Learn from your mistakes")
            st.write(
                "Review the expected output and your output. "
                "Check your conditions, spelling, indentation, and logic."
            )

            if st.button(
                "Reveal solution and explanation",
                key=f"practice_reveal_{quest_id}",
            ):
                st.session_state.practice_solutions_revealed[quest_id] = True

    if st.session_state.practice_solutions_revealed.get(quest_id):
        st.markdown("#### Reference solution")
        st.code(quest["solution"], language=quest["language"].lower())
        st.info(f"**Explanation:** {quest['explanation']}")

        if st.button(
            "Reset editor to starter code",
            key=f"practice_reset_{quest_id}",
        ):
            st.session_state[editor_key] = quest["starter_code"]
            st.session_state.practice_results.pop(quest_id, None)
            st.session_state.practice_solutions_revealed[quest_id] = False
            st.session_state.practice_hints_revealed[quest_id] = False
            st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("🎮 DevQuest AI")
    st.caption("Your coding adventure")

    st.text_input(
        "Player username",
        key="username",
    )

    st.divider()

    st.subheader(f"Developer · Level {xp // 100 + 1}")
    st.progress((xp % 100) / 100)
    st.write(f"⭐ {xp} total XP")

    st.divider()

    page = st.radio(
        "🧭 NAVIGATION",
        [
            "🏠 Dashboard",
            "🎯 Coding Quests",
            "🧪 Practice Mode",
            "🏅 Achievements",
            "🤖 AI Code Reviewer",
            "🏆 Leaderboard",
        ],
    )

    st.divider()

    st.markdown("### 💡 DAILY REMINDER")
    st.info("Small steps every day lead to big skills.")
    st.caption("DevQuest AI · Version 2.3")


# ============================================================
# PAGE HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🎮 DevQuest AI</h1>
        <p>
            Level up your coding skills, complete challenges,
            and become a better developer.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":
    st.header("🏠 Player Dashboard")

    st.write(
        f"Welcome back, **{st.session_state.username}**! "
        "Ready for your next coding adventure?"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("⭐ Total XP", xp)
    col2.metric("✅ Quests Completed", len(completed_quests))
    col3.metric("🎯 Available Quests", len(QUESTS))

    st.subheader("📈 Your Progress")

    completion_ratio = len(completed_quests) / len(QUESTS)
    st.progress(min(completion_ratio, 1.0))

    st.write(
        f"You have completed {len(completed_quests)} "
        f"of {len(QUESTS)} quests."
    )

    st.subheader("🚀 Your Missions")

    for quest in QUESTS:
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(f"### {quest['icon']} {quest['title']}")
                st.write(quest["description"])

            with col2:
                if quest["id"] in completed_quests:
                    st.success("Completed")
                else:
                    st.warning("Available")

    st.info(
        "Open 🧪 Practice Mode to try challenges again "
        "without changing your saved XP."
    )


# ============================================================
# CODING QUESTS
# ============================================================

elif page == "🎯 Coding Quests":
    st.header("🚀 Coding Quest Board")

    st.write(
        "Complete missions to earn XP. Your completed quests "
        "remain saved between app restarts."
    )

    for quest in QUESTS:
        quest_id = quest["id"]
        completed = quest_id in completed_quests

        with st.container(border=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(f"{quest['icon']} {quest['title']}")
                st.write(quest["description"])
                st.caption(
                    f"{quest['language']} · {quest['difficulty']} · "
                    f"⭐ {quest['xp']} XP"
                )

            with col2:
                if completed:
                    st.success("Completed")
                else:
                    st.warning("Available")

            if completed:
                st.success(
                    f"🎉 Mission complete! You earned {quest['xp']} XP."
                )
                continue

            with st.expander("Open mission"):
                st.write(quest["question"])
                st.info(f"Hint: {quest['hint']}")

                editor_key = f"quest_editor_{quest_id}"

                if editor_key not in st.session_state:
                    st.session_state[editor_key] = quest["starter_code"]

                code = st.text_area(
                    "Your code",
                    key=editor_key,
                    height=200,
                )

                if st.button(
                    "Submit Mission",
                    key=f"submit_{quest_id}",
                ):
                    try:
                        result = run_quest_tests(quest, code)
                        show_test_results(result)

                        passed_all = (
                            result.get("total", 0) > 0
                            and result.get("passed", 0)
                            == result.get("total", 0)
                            and not result.get("error")
                        )

                        if passed_all:
                            if quest_id not in completed_quests:
                                completed_quests.append(quest_id)
                                xp += quest["xp"]
                                save_current_progress()

                            st.success(
                                f"Mission complete! +{quest['xp']} XP"
                            )
                            st.balloons()
                            st.rerun()

                        else:
                            st.error(
                                "Some tests failed. Correct your code "
                                "and submit the mission again."
                            )

                            with st.expander("View reference solution"):
                                st.code(
                                    quest["solution"],
                                    language=quest["language"].lower(),
                                )
                                st.write(quest["explanation"])

                    except Exception as exc:
                        st.error(f"Could not run the mission: {exc}")

# ============================================================
# PRACTICE MODE
# ============================================================

elif page == "🧪 Practice Mode":
    st.header("🧪 Practice Arena")

    st.write(
        "Practise as many times as you like, bro! "
        "Mistakes are part of learning."
    )

    st.info(
        "Practice Mode does not change your saved XP, "
        "completed quests, or leaderboard score."
    )

    for quest in QUESTS:
        with st.expander(
            f"{quest['icon']} {quest['title']} · {quest['language']}",
            expanded=False,
        ):
            render_practice_card(quest)


# ============================================================
# ACHIEVEMENTS
# ============================================================

elif page == "🏅 Achievements":
    st.header("🏅 Achievements")

    achievements = [
        (
            "🌟 First Quest",
            "Complete your first coding quest.",
            len(completed_quests) >= 1,
        ),
        (
            "⭐ XP Hunter",
            "Earn at least 100 XP.",
            xp >= 100,
        ),
        (
            "👑 Quest Master",
            "Complete all three coding quests.",
            len(completed_quests) >= len(QUESTS),
        ),
    ]

    for title, description, unlocked in achievements:
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])

            with col1:
                st.subheader(title)
                st.write(description)

            with col2:
                if unlocked:
                    st.success("Unlocked")
                else:
                    st.caption("Locked")


# ============================================================
# AI CODE REVIEWER
# ============================================================

elif page == "🤖 AI Code Reviewer":
    st.header("🤖 AI Code Reviewer")

    st.write(
        "Review your code for potential issues and improvement "
        "opportunities."
    )

    language = st.selectbox("Choose language", ["Python", "SQL"])

    code = st.text_area(
        "Paste your code",
        height=300,
        key="reviewer_code",
        placeholder="Write or paste your code here...",
    )

    if st.button("🔍 Review Code", use_container_width=True):
        if not code.strip():
            st.warning("Please enter some code first.")
        else:
            try:
                result = review_code(code, language)
                st.subheader("Review Results")

                if isinstance(result, str):
                    st.markdown(result)

                elif isinstance(result, dict):
                    for key, value in result.items():
                        st.markdown(
                            f"**{key.replace('_', ' ').title()}**"
                        )
                        st.write(value)

                else:
                    st.write(result)

            except Exception as exc:
                st.error(
                    "The reviewer could not process this code. "
                    "Check the review_code function in ai_reviewer.py."
                )
                st.caption(str(exc))


# ============================================================
# LEADERBOARD
# ============================================================

elif page == "🏆 Leaderboard":
    st.header("🏆 Leaderboard")

    st.write("See how players rank by earned XP.")

    try:
        leaderboard = get_leaderboard(10)

        if not leaderboard:
            st.info(
                "No leaderboard entries yet. Complete a quest "
                "to add your score!"
            )
        else:
            st.caption("Scores are stored in the local SQLite database.")

            for rank, player in enumerate(leaderboard, start=1):
                if isinstance(player, dict):
                    username = player.get("username", "Player")
                    player_xp = player.get("xp", 0)
                    count = player.get("completed_count", 0)
                else:
                    username = player[0]
                    player_xp = player[1]
                    count = player[2] if len(player) > 2 else 0

                with st.container(border=True):
                    col1, col2, col3 = st.columns([2, 1, 1])

                    col1.write(f"**#{rank} {username}**")
                    col2.write(f"⭐ {player_xp} XP")
                    col3.write(f"✅ {count} quests")

    except Exception as exc:
        st.error(f"Could not load the leaderboard: {exc}")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "DevQuest AI v2.3 · Built with Python, Streamlit, and SQLite · "
    "Keep learning. Keep building. Keep leveling up. 🚀"
)
