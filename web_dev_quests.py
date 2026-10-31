WEB_DEV_QUESTS = [
    {
        "id": "web_html_profile_card",
        "title": "HTML Profile Card",
        "icon": "🪪",
        "language": "HTML",
        "category": "Web Development",
        "level": 1,
        "difficulty": "Beginner",
        "xp": 50,
        "description": "Build a simple personal profile card using HTML.",
        "question": (
            "Create a profile card containing a heading with your name, "
            "a paragraph describing yourself, and a link to your portfolio."
        ),
        "hint": (
            "Use a heading element, a paragraph element, and an anchor "
            "element with an href attribute."
        ),
        "starter_code": (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "    <title>My Profile</title>\n"
            "</head>\n"
            "<body>\n"
            "    <!-- Add your profile card below -->\n"
            "\n"
            "</body>\n"
            "</html>"
        ),
        "solution": (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "    <title>My Profile</title>\n"
            "</head>\n"
            "<body>\n"
            "    <div class=\"profile-card\">\n"
            "        <h1>My Name</h1>\n"
            "        <p>I am a computer science student.</p>\n"
            "        <a href=\"https://example.com\">My Portfolio</a>\n"
            "    </div>\n"
            "</body>\n"
            "</html>"
        ),
        "explanation": (
            "HTML describes the structure of a webpage. A heading displays "
            "the profile name, a paragraph provides a short introduction, "
            "and an anchor creates a clickable link."
        ),
        "validator": "html_profile",
        "tests": [],
    },
    {
        "id": "web_css_button",
        "title": "CSS Button Styling",
        "icon": "🎨",
        "language": "CSS",
        "category": "Web Development",
        "level": 1,
        "difficulty": "Beginner",
        "xp": 50,
        "description": "Style a button and add a hover effect using CSS.",
        "question": (
            "Write CSS for a button with a background color, white text, "
            "padding, rounded corners, and a hover effect that changes "
            "its background color."
        ),
        "hint": (
            "Use a button selector, background-color, color, padding, "
            "border-radius, and the :hover pseudo-class."
        ),
        "starter_code": (
            "button {\n"
            "    /* Add your button styles */\n"
            "}\n\n"
            "button:hover {\n"
            "    /* Add your hover effect */\n"
            "}"
        ),
        "solution": (
            "button {\n"
            "    background-color: #6c4aff;\n"
            "    color: white;\n"
            "    padding: 12px 24px;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    cursor: pointer;\n"
            "}\n\n"
            "button:hover {\n"
            "    background-color: #4326b5;\n"
            "}"
        ),
        "explanation": (
            "CSS controls the appearance of HTML elements. The button "
            "selector applies the normal styles, while button:hover applies "
            "different styles when the pointer is over the button."
        ),
        "validator": "css_button",
        "tests": [],
    },
    {
        "id": "web_html_registration",
        "title": "HTML Registration Form",
        "icon": "📝",
        "language": "HTML",
        "category": "Web Development",
        "level": 1,
        "difficulty": "Beginner",
        "xp": 60,
        "description": "Create a registration form with basic input fields.",
        "question": (
            "Create a form containing a name input, an email input, "
            "a password input, and a submit button. Each input must "
            "have an associated label."
        ),
        "hint": (
            "Use form, label, input, and button elements. Give each input "
            "an id and connect its label using the for attribute."
        ),
        "starter_code": (
            "<form>\n"
            "    <!-- Add name, email and password fields -->\n"
            "\n"
            "    <!-- Add a submit button -->\n"
            "</form>"
        ),
        "solution": (
            "<form>\n"
            "    <label for=\"name\">Name</label>\n"
            "    <input type=\"text\" id=\"name\" name=\"name\">\n"
            "\n"
            "    <label for=\"email\">Email</label>\n"
            "    <input type=\"email\" id=\"email\" name=\"email\">\n"
            "\n"
            "    <label for=\"password\">Password</label>\n"
            "    <input type=\"password\" id=\"password\" name=\"password\">\n"
            "\n"
            "    <button type=\"submit\">Register</button>\n"
            "</form>"
        ),
        "explanation": (
            "A form collects information from users. Labels make fields "
            "easier to understand and improve accessibility. Input types "
            "help browsers identify the kind of information expected."
        ),
        "validator": "html_registration",
        "tests": [],
    },
    {
        "id": "web_js_counter",
        "title": "JavaScript Counter",
        "icon": "🔢",
        "language": "JavaScript",
        "category": "Web Development",
        "level": 1,
        "difficulty": "Beginner",
        "xp": 70,
        "description": "Create a counter that increases when a function runs.",
        "question": (
            "Create a variable named count starting at zero. Write a "
            "function named incrementCounter that increases count by one."
        ),
        "hint": (
            "Declare count with let. Inside the function, use count += 1 "
            "or count++."
        ),
        "starter_code": (
            "let count = 0;\n\n"
            "function incrementCounter() {\n"
            "    // Increase count by one\n"
            "}\n"
        ),
        "solution": (
            "let count = 0;\n\n"
            "function incrementCounter() {\n"
            "    count += 1;\n"
            "}\n"
        ),
        "explanation": (
            "The let keyword declares a variable whose value can change. "
            "The incrementCounter function updates the count by adding one."
        ),
        "validator": "js_counter",
        "tests": [],
    },
    {
        "id": "web_js_greeting",
        "title": "DOM Greeting App",
        "icon": "👋",
        "language": "JavaScript",
        "category": "Web Development",
        "level": 1,
        "difficulty": "Beginner",
        "xp": 70,
        "description": "Use JavaScript to update text on a webpage.",
        "question": (
            "Write JavaScript that finds the HTML element with the id "
            "'greeting' and changes its text to 'Hello, Developer!'."
        ),
        "hint": (
            "Use document.getElementById('greeting') and update its "
            "textContent property."
        ),
        "starter_code": (
            "// Find the element with id 'greeting'\n"
            "\n"
            "// Change its text to 'Hello, Developer!'\n"
        ),
        "solution": (
            "const greeting = document.getElementById('greeting');\n"
            "greeting.textContent = 'Hello, Developer!';"
        ),
        "explanation": (
            "The DOM represents the structure of a webpage. "
            "getElementById selects an element using its id, and "
            "textContent changes the text displayed inside it."
        ),
        "validator": "js_greeting",
        "tests": [],
    },
]