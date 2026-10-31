import re
from html.parser import HTMLParser


class HTMLStructureParser(HTMLParser):
    """Collect HTML tags and their attributes."""

    def __init__(self):
        super().__init__()
        self.tags = []
        self.attributes = {}

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag.lower())
        self.attributes.setdefault(tag.lower(), []).append(
            dict(attrs)
        )

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


def _result(passed, message, expected):
    return {
        "passed": passed,
        "input": "Web Development answer validation",
        "expected": expected,
        "actual": message,
        "error": "",
    }


def _check_html(code, validator):
    parser = HTMLStructureParser()

    try:
        parser.feed(code)
        parser.close()
    except Exception as exc:
        return _result(
            False,
            f"HTML parsing failed: {exc}",
            "Valid HTML structure",
        )

    tags = parser.tags
    attrs = parser.attributes

    if validator == "html_profile":
        checks = {
            "A heading element": any(
                tag in tags for tag in ("h1", "h2", "h3")
            ),
            "A paragraph element": "p" in tags,
            "A link with href": any(
                bool(item.get("href"))
                for item in attrs.get("a", [])
            ),
        }

    elif validator == "html_registration":
        checks = {
            "A form element": "form" in tags,
            "A name input": any(
                item.get("type", "").lower() == "text"
                for item in attrs.get("input", [])
            ),
            "An email input": any(
                item.get("type", "").lower() == "email"
                for item in attrs.get("input", [])
            ),
            "A password input": any(
                item.get("type", "").lower() == "password"
                for item in attrs.get("input", [])
            ),
            "A submit button": (
                any(
                    item.get("type", "").lower() == "submit"
                    for item in attrs.get("button", [])
                )
                or "button" in tags
            ),
        }

        input_ids = {
            item.get("id")
            for item in attrs.get("input", [])
            if item.get("id")
        }

        label_targets = {
            item.get("for")
            for item in attrs.get("label", [])
            if item.get("for")
        }

        checks["Labels connected to inputs"] = bool(
            input_ids.intersection(label_targets)
        )

    else:
        return _result(
            False,
            "Unknown HTML validator.",
            "A supported HTML challenge",
        )

    missing = [
        name for name, passed in checks.items()
        if not passed
    ]

    if missing:
        return _result(
            False,
            "Missing requirements: " + ", ".join(missing),
            "All required HTML elements and attributes",
        )

    return _result(
        True,
        "All required HTML elements and attributes were found.",
        "All required HTML elements and attributes",
    )


def _check_css(code):
    css = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)

    normal_button = re.search(
        r"button\s*\{([^{}]*)\}",
        css,
        flags=re.IGNORECASE,
    )

    hover_button = re.search(
        r"button\s*:\s*hover\s*\{([^{}]*)\}",
        css,
        flags=re.IGNORECASE,
    )

    if not normal_button:
        return _result(
            False,
            "Add a button { ... } CSS rule.",
            "Button styles and a hover rule",
        )

    if not hover_button:
        return _result(
            False,
            "Add a button:hover { ... } rule.",
            "Button styles and a hover rule",
        )

    normal_styles = normal_button.group(1).lower()
    hover_styles = hover_button.group(1).lower()

    required_properties = [
        "background-color",
        "color",
        "padding",
        "border-radius",
    ]

    missing = [
        prop for prop in required_properties
        if not re.search(
            rf"(?:^|;)\s*{re.escape(prop)}\s*:",
            normal_styles,
        )
    ]

    if missing:
        return _result(
            False,
            "Missing button properties: " + ", ".join(missing),
            "Background color, text color, padding, rounded corners, "
            "and a hover background change",
        )

    if not re.search(
        r"background(?:-color)?\s*:",
        hover_styles,
    ):
        return _result(
            False,
            "Change the button background inside button:hover.",
            "A hover background color",
        )

    return _result(
        True,
        "Button styling and hover effect requirements were found.",
        "Background color, text color, padding, rounded corners, "
        "and a hover background change",
    )


def _check_js(code, validator):
    js = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)
    js = re.sub(r"//.*", "", js)

    if validator == "js_counter":
        has_count = bool(
            re.search(
                r"\b(?:let|var)\s+count\s*=\s*0\b",
                js,
            )
        )

        has_function = bool(
            re.search(
                r"\bfunction\s+incrementCounter\s*\(",
                js,
            )
        )

        has_increment = bool(
            re.search(
                r"\bcount\s*(?:\+\+|\+=\s*1|=\s*count\s*\+\s*1)",
                js,
            )
        )

        checks = {
            "count starts at zero": has_count,
            "incrementCounter function exists": has_function,
            "count increases by one": has_increment,
        }

    elif validator == "js_greeting":
        has_element = bool(
            re.search(
                r"document\s*\.\s*getElementById\s*\(\s*['\"]greeting['\"]\s*\)",
                js,
            )
        )

        has_text = bool(
            re.search(
                r"\.\s*textContent\s*=\s*['\"]Hello,\s*Developer!['\"]",
                js,
            )
        )

        checks = {
            "The greeting element is selected": has_element,
            "The greeting text is updated": has_text,
        }

    else:
        return _result(
            False,
            "Unknown JavaScript validator.",
            "A supported JavaScript challenge",
        )

    missing = [
        name for name, passed in checks.items()
        if not passed
    ]

    if missing:
        return _result(
            False,
            "Missing requirements: " + ", ".join(missing),
            "All required JavaScript statements",
        )

    return _result(
        True,
        "All required JavaScript patterns were found.",
        "All required JavaScript statements",
    )


def check_web_answer(code, validator):
    """Validate a Web Development quest without executing user code."""

    if not isinstance(code, str) or not code.strip():
        return _result(
            False,
            "Please enter your code before submitting.",
            "A completed Web Development solution",
        )

    if validator in ("html_profile", "html_registration"):
        return _check_html(code, validator)

    if validator == "css_button":
        return _check_css(code)

    if validator in ("js_counter", "js_greeting"):
        return _check_js(code, validator)

    return _result(
        False,
        "Unknown Web Development challenge.",
        "A supported Web Development challenge",
    )