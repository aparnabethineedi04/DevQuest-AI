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
from sql_quests import QUEST_BANK_SQL
from additional_quests import ADDITIONAL_QUESTS
from web_dsa_quests import WEB_DSA_QUESTS
from web_dev_quests import WEB_DEV_QUESTS
from web_dev_checker import check_web_answer


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
        "category": "Python",
        "level": 1,
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
        "category": "SQL",
        "level": 1,
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
        "category": "Debugging",
        "level": 1,
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
    {
        "id": "python_level2_palindrome",
        "title": "Palindrome Checker",
        "icon": "🔁",
        "language": "Python",
        "category": "Python",
        "level": 2,
        "difficulty": "Intermediate",
        "xp": 100,
        "description": "Build a program that checks whether a word is a palindrome.",
        "question": (
            "Read a word from input. Print 'Palindrome' if the word "
            "reads the same forward and backward. Otherwise print 'Not Palindrome'."
        ),
        "hint": "Compare the word with its reversed version using slicing.",
        "starter_code": (
            "word = input().strip()\n\n"
            "# Write your code below\n"
        ),
        "solution": (
            "word = input().strip()\n\n"
            "if word == word[::-1]:\n"
            "    print('Palindrome')\n"
            "else:\n"
            "    print('Not Palindrome')"
        ),
        "explanation": (
            "The slice [::-1] reverses a string. Comparing the original "
            "word with its reverse tells us whether it is a palindrome."
        ),
        "tests": [
            {"input": "madam\n", "expected": "Palindrome\n"},
            {"input": "level\n", "expected": "Palindrome\n"},
            {"input": "python\n", "expected": "Not Palindrome\n"},
        ],
    },
    {
        "id": "debugging_level2_loop",
        "title": "Loop Bug Hunter",
        "icon": "🐞",
        "language": "Python",
        "category": "Debugging",
        "level": 2,
        "difficulty": "Intermediate",
        "xp": 100,
        "description": "Fix a loop that should calculate the sum from 1 to n.",
        "question": (
            "The program should read an integer n and print the sum "
            "of all integers from 1 through n. Fix the bug."
        ),
        "hint": (
            "Check the range endpoint. Python's range excludes its "
            "stop value."
        ),
        "starter_code": (
            "n = int(input())\n"
            "total = 0\n\n"
            "for number in range(1, n):\n"
            "    total += number\n\n"
            "print(total)"
        ),
        "solution": (
            "n = int(input())\n"
            "total = 0\n\n"
            "for number in range(1, n + 1):\n"
            "    total += number\n\n"
            "print(total)"
        ),
        "explanation": (
            "The stop value in range() is excluded. Using n + 1 "
            "ensures that n is included in the calculation."
        ),
        "tests": [
            {"input": "5\n", "expected": "15\n"},
            {"input": "3\n", "expected": "6\n"},
            {"input": "1\n", "expected": "1\n"},
        ],
    },
]


# ============================================================
# ADDITIONAL QUEST BANKS
# ============================================================

QUESTS.extend(QUEST_BANK_SQL)
QUESTS.extend(ADDITIONAL_QUESTS)
QUESTS.extend(WEB_DSA_QUESTS)
QUESTS.extend(WEB_DEV_QUESTS)

for quest in QUESTS:
    quest.setdefault(
        "category",
        quest.get("language", "Python"),
    )
    quest.setdefault("level", 1)


# ============================================================
# LOAD SAVED PROGRESS
# ============================================================

progress = load_progress()

if not isinstance(progress, dict):
    progress = {}

xp = int(progress.get("xp", 0))

completed_quests = list(
    progress.get("completed_quests", [])
)

accepted_quests = list(
    progress.get("accepted_quests", [])
)


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
# STYLING
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
    """Save progress and update the local leaderboard."""

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


def run_quest_tests(quest, code):
    """Run the appropriate checker for the selected quest."""

    # WEB DEVELOPMENT VALIDATION
    if quest.get("category") == "Web Development":

        check = check_web_answer(
            code,
            quest.get("validator", ""),
        )

        passed = bool(check.get("passed", False))

        return {
            "passed": 1 if passed else 0,
            "total": 1,
            "results": [
                {
                    "passed": passed,
                    "input": check.get(
                        "input",
                        "Web Development validation",
                    ),
                    "expected": check.get(
                        "expected",
                        "All requirements",
                    ),
                    "actual": check.get(
                        "actual",
                        "No validation message.",
                    ),
                    "error": check.get("error", ""),
                }
            ],
            "error": check.get("error", ""),
        }

    # SQL VALIDATION
    if quest["language"].upper() == "SQL":

        from sql_checker import check_sql_answer

        check = check_sql_answer(
            code,
            quest.get("validator", "select_employees"),
        )

        passed = bool(check.get("passed", False))

        return {
            "passed": 1 if passed else 0,
            "total": 1,
            "results": [
                {
                    "passed": passed,
                    "input": "SQL answer validation",
                    "expected": quest.get(
                        "solution",
                        "Correct SQL result",
                    ),
                    "actual": check.get(
                        "message",
                        "No validation message.",
                    ),
                }
            ],
            "error": None,
        }

    # PYTHON VALIDATION
    return run_python_tests(
        code,
        quest["tests"],
        timeout=3,
    )


def show_test_results(result):
    """Display individual test results."""

    if result.get("error"):
        st.error(
            f"Execution error: {result['error']}"
        )

    for index, item in enumerate(
        result.get("results", []),
        start=1,
    ):

        if item.get("passed", False):
            st.success(f"Test {index}: Passed")
        else:
            st.error(f"Test {index}: Failed")

        with st.expander(
            f"Test {index} details"
        ):

            st.write("**Input**")
            st.code(
                str(item.get("input", "")),
                language="text",
            )

            st.write("**Expected output**")
            st.code(
                str(item.get("expected", "")),
                language="text",
            )

            st.write("**Your output**")
            st.code(
                str(item.get("actual", "")),
                language="text",
            )


def render_practice_card(quest):
    """Render practice challenges without awarding XP."""

    quest_id = quest["id"]

    editor_key = f"practice_editor_{quest_id}"

    st.markdown(
        f"### {quest['icon']} {quest['title']}"
    )

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
        st.session_state.practice_hints_revealed[
            quest_id
        ] = True

    if solution_clicked:
        st.session_state.practice_solutions_revealed[
            quest_id
        ] = True

    if st.session_state.practice_hints_revealed.get(
        quest_id
    ):
        st.info(f"**Hint:** {quest['hint']}")

    if check_clicked:

        try:
            with st.spinner("Checking your code..."):

                result = run_quest_tests(
                    quest,
                    code,
                )

            st.session_state.practice_results[
                quest_id
            ] = result

            if (
                result.get("total", 0) > 0
                and result.get("passed", 0)
                == result.get("total", 0)
                and not result.get("error")
            ):

                st.success(
                    "Excellent work! All tests passed. "
                    "Practice Mode does not award XP."
                )

            else:

                st.warning(
                    "Not quite there yet! Review the test "
                    "results and try again."
                )

        except Exception as exc:

            st.session_state.practice_results[
                quest_id
            ] = None

            st.error(
                f"Could not check this answer: {exc}"
            )

    result = st.session_state.practice_results.get(
        quest_id
    )

    if result:

        show_test_results(result)

        passed_all = (
            result.get("total", 0) > 0
            and result.get("passed", 0)
            == result.get("total", 0)
            and not result.get("error")
        )

        if passed_all:
            st.success("Practice challenge passed!")

    if st.session_state.practice_solutions_revealed.get(
        quest_id
    ):

        st.markdown("#### Reference solution")

        language_map = {
            "HTML": "html",
            "CSS": "css",
            "JavaScript": "javascript",
            "Python": "python",
            "SQL": "sql",
        }

        st.code(
            quest["solution"],
            language=language_map.get(
                quest["language"],
                "text",
            ),
        )

        st.info(
            f"**Explanation:** {quest['explanation']}"
        )

        if st.button(
            "Reset editor to starter code",
            key=f"practice_reset_{quest_id}",
        ):

            st.session_state[editor_key] = quest[
                "starter_code"
            ]

            st.session_state.practice_results.pop(
                quest_id,
                None,
            )

            st.session_state.practice_solutions_revealed[
                quest_id
            ] = False

            st.session_state.practice_hints_revealed[
                quest_id
            ] = False

            st.rerun()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.title("🎮 DevQuest AI")

    st.caption(
        "Your coding adventure starts here!"
    )

    st.session_state.username = st.text_input(
        "Player name",
        value=st.session_state.username,
        max_chars=30,
    )

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

    st.metric("⭐ Total XP", xp)

    st.metric(
        "✅ Completed Quests",
        len(completed_quests),
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="hero">
            <h1>Welcome to DevQuest AI! 🚀</h1>
            <p>
                Learn coding, solve challenges, improve your skills,
                and level up one quest at a time.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⭐ Total XP", xp)

    with col2:
        st.metric(
            "✅ Completed Quests",
            len(completed_quests),
        )

    with col3:
        st.metric(
            "📚 Available Quests",
            len(QUESTS),
        )

    st.divider()

    st.subheader("🚀 Your Quest Progress")

    if not completed_quests:

        st.info(
            "You haven't completed a quest yet. "
            "Open Coding Quests and start your adventure!"
        )

    else:

        progress_percent = min(
            len(completed_quests) / max(len(QUESTS), 1),
            1.0,
        )

        st.progress(progress_percent)

        st.write(
            f"You have completed {len(completed_quests)} "
            f"out of {len(QUESTS)} available quests."
        )

    st.divider()

    st.subheader("🗺️ Learning Categories")

    category_columns = st.columns(5)

    category_details = [
        ("🗄️", "SQL", "Learn database queries"),
        ("🐍", "Python", "Build programming logic"),
        ("🕵️", "Debugging", "Find and fix errors"),
        ("🌐", "Web Development", "Build web applications"),
        ("🧠", "DSA", "Master problem solving"),
    ]

    for column, details in zip(
        category_columns,
        category_details,
    ):

        icon, title, description = details

        with column:

            st.markdown(
                f"### {icon} {title}"
            )

            st.caption(description)

    st.divider()

    st.subheader("🎯 Your Level Progress")

    for category in [
        "SQL",
        "Python",
        "Debugging",
        "Web Development",
        "DSA",
    ]:

        category_quests = [
            q for q in QUESTS
            if q.get("category") == category
        ]

        level_one = [
            q for q in category_quests
            if int(q.get("level", 1)) == 1
        ]

        level_two = [
            q for q in category_quests
            if int(q.get("level", 1)) == 2
        ]

        level_one_done = bool(level_one) and all(
            q["id"] in completed_quests
            for q in level_one
        )

        if level_one_done and level_two:

            status = "Level 2 unlocked 🎉"

        elif level_one:

            status = "Level 1 in progress"

        else:

            status = "Coming soon"

        st.write(
            f"**{category}:** {status}"
        )

    st.info(
        "Complete every Level 1 quest in a category "
        "to unlock its Level 2 challenges."
    )


# ============================================================
# CODING QUESTS
# ============================================================

elif page == "🎯 Coding Quests":

    st.header("🚀 Coding Quest Board")

    st.write(
        "Choose a category and level. Complete the challenges "
        "to unlock more difficult quests."
    )

    categories = [
        "SQL",
        "Python",
        "Debugging",
        "Web Development",
        "DSA",
    ]

    selected_category = st.radio(
        "📚 Choose a category",
        categories,
        horizontal=True,
        key="coding_quest_category",
    )

    category_quests = [
        quest for quest in QUESTS
        if quest.get("category") == selected_category
    ]

    st.divider()

    st.subheader(
        f"{selected_category} Quests"
    )

    level_one_quests = [
        quest for quest in category_quests
        if int(quest.get("level", 1)) == 1
    ]

    level_two_quests = [
        quest for quest in category_quests
        if int(quest.get("level", 1)) == 2
    ]

    level_one_complete = (
        bool(level_one_quests)
        and all(
            quest["id"] in completed_quests
            for quest in level_one_quests
        )
    )

    available_levels = [1]

    if level_one_complete and level_two_quests:
        available_levels.append(2)

    selected_level = st.selectbox(
        "🏆 Select your level",
        available_levels,
        format_func=lambda value: f"Level {value}",
        key=f"quest_level_{selected_category}",
    )

    if selected_level == 1:

        st.info(
            "Complete all Level 1 quests to unlock Level 2."
        )

    elif selected_level == 2:

        st.success(
            "🎉 Congratulations! You unlocked Level 2!"
        )

    visible_quests = [
        quest for quest in category_quests
        if int(quest.get("level", 1)) == selected_level
    ]

    if not category_quests:

        st.info(
            f"No {selected_category} quests have been added yet."
        )

    elif not visible_quests:

        st.info(
            f"No Level {selected_level} challenges are available "
            f"for {selected_category} yet."
        )

    else:

        quest_labels = [
            (
                f"{quest['icon']} {quest['title']} · "
                f"{quest['difficulty']} · {quest['xp']} XP"
            )
            for quest in visible_quests
        ]

        selected_label = st.selectbox(
            "Select a quest",
            quest_labels,
            key=f"quest_picker_{selected_category}_{selected_level}",
        )

        selected_index = quest_labels.index(
            selected_label
        )

        quest = visible_quests[selected_index]

        quest_id = quest["id"]

        completed = quest_id in completed_quests

        with st.container(border=True):

            st.subheader(
                f"{quest['icon']} {quest['title']}"
            )

            st.write(quest["description"])

            st.caption(
                f"Level {selected_level} · "
                f"{quest['language']} · "
                f"{quest['difficulty']} · "
                f"⭐ {quest['xp']} XP"
            )

            st.markdown("**Your challenge**")

            st.write(quest["question"])

            st.info(
                f"💡 Hint: {quest['hint']}"
            )

            if completed:

                st.success(
                    "🎉 You have already completed this quest!"
                )

                st.caption(
                    "Your XP is already saved. You can still "
                    "practise and submit your solution again."
                )

            editor_key = f"quest_editor_{quest_id}"

            if editor_key not in st.session_state:

                st.session_state[editor_key] = quest[
                    "starter_code"
                ]

            code = st.text_area(
                "Write your solution",
                key=editor_key,
                height=230,
            )

            button_label = (
                "🔁 Run Again"
                if completed
                else "🚀 Submit Quest"
            )

            if st.button(
                button_label,
                key=f"submit_{quest_id}",
                use_container_width=True,
            ):

                try:

                    with st.spinner(
                        "Checking your solution..."
                    ):

                        result = run_quest_tests(
                            quest,
                            code,
                        )

                    show_test_results(result)

                    passed_all = (
                        result.get("total", 0) > 0
                        and result.get("passed", 0)
                        == result.get("total", 0)
                        and not result.get("error")
                    )

                    if passed_all:

                        if quest_id not in completed_quests:

                            completed_quests.append(
                                quest_id
                            )

                            xp += int(
                                quest.get("xp", 0)
                            )

                            save_current_progress()

                            st.success(
                                f"🎉 Quest completed! "
                                f"You earned {quest['xp']} XP."
                            )

                            st.balloons()

                        else:

                            st.success(
                                "All tests passed again! "
                                "You have already earned XP for this quest. "
                                "No duplicate XP was added."
                            )

                        st.rerun()

                    else:

                        st.error(
                            "Some tests failed. Correct your answer "
                            "and submit again. XP is awarded only "
                            "after all tests pass."
                        )

                except Exception as exc:

                    st.error(
                        f"Could not run this quest: {exc}"
                    )


# ============================================================
# PRACTICE MODE
# ============================================================

elif page == "🧪 Practice Mode":

    st.header("🧪 Practice Arena")

    st.write(
        "Practise as many times as you like! "
        "Mistakes are part of learning."
    )

    st.info(
        "Practice Mode does not change your saved XP, "
        "completed quests, or leaderboard score."
    )

    for quest in QUESTS:

        with st.expander(
            f"{quest['icon']} {quest['title']} · "
            f"{quest['language']} · Level {quest.get('level', 1)}",
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
            "🔥 XP Champion",
            "Earn at least 500 XP.",
            xp >= 500,
        ),
        (
            "🐍 Python Explorer",
            "Complete a Python quest.",
            any(
                quest["id"] in completed_quests
                and quest.get("category") == "Python"
                for quest in QUESTS
            ),
        ),
        (
            "🕵️ Debugging Expert",
            "Complete a debugging quest.",
            any(
                quest["id"] in completed_quests
                and quest.get("category") == "Debugging"
                for quest in QUESTS
            ),
        ),
        (
            "🌐 Web Developer",
            "Complete a Web Development quest.",
            any(
                quest["id"] in completed_quests
                and quest.get("category") == "Web Development"
                for quest in QUESTS
            ),
        ),
        (
            "🧠 DSA Explorer",
            "Complete a DSA quest.",
            any(
                quest["id"] in completed_quests
                and quest.get("category") == "DSA"
                for quest in QUESTS
            ),
        ),
        (
            "🚀 Level 2 Explorer",
            "Complete a Level 2 quest.",
            any(
                quest["id"] in completed_quests
                and int(quest.get("level", 1)) == 2
                for quest in QUESTS
            ),
        ),
        (
            "👑 Quest Master",
            "Complete all available coding quests.",
            len(QUESTS) > 0
            and all(
                quest["id"] in completed_quests
                for quest in QUESTS
            ),
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
        "Review your code for potential issues and "
        "improvement opportunities."
    )

    language = st.selectbox(
        "Choose language",
        ["Python", "SQL"],
    )

    code = st.text_area(
        "Paste your code",
        height=300,
        key="reviewer_code",
        placeholder="Write or paste your code here...",
    )

    if st.button(
        "🔍 Review Code",
        use_container_width=True,
    ):

        if not code.strip():

            st.warning(
                "Please enter some code first."
            )

        else:

            try:

                result = review_code(
                    code,
                    language,
                )

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

    st.write(
        "See how players rank by earned XP."
    )

    try:

        leaderboard = get_leaderboard(10)

        if not leaderboard:

            st.info(
                "No leaderboard entries yet. "
                "Complete a quest to add your score!"
            )

        else:

            st.caption(
                "Scores are stored in the local SQLite database."
            )

            for rank, player in enumerate(
                leaderboard,
                start=1,
            ):

                if isinstance(player, dict):

                    username = player.get(
                        "username",
                        "Player",
                    )

                    player_xp = player.get(
                        "xp",
                        0,
                    )

                    count = player.get(
                        "completed_count",
                        0,
                    )

                else:

                    username = player[0]

                    player_xp = player[1]

                    count = (
                        player[2]
                        if len(player) > 2
                        else 0
                    )

                with st.container(border=True):

                    col1, col2, col3 = st.columns(
                        [2, 1, 1]
                    )

                    col1.write(
                        f"**#{rank} {username}**"
                    )

                    col2.write(
                        f"⭐ {player_xp} XP"
                    )

                    col3.write(
                        f"✅ {count} quests"
                    )

    except Exception as exc:

        st.error(
            f"Could not load leaderboard: {exc}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "DevQuest AI v2.4 · Built with Python, Streamlit, and SQLite · "
    "Keep learning. Keep building. Keep leveling up. 🚀"
)