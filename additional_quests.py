
ADDITIONAL_QUESTS = [
    {
        "id": "py_sum_two",
        "title": "Sum of Two Numbers",
        "icon": "🐍",
        "language": "Python",
        "category": "Python",
        "difficulty": "Beginner",
        "xp": 20,
        "description": "Calculate the sum of two numbers.",
        "question": "Read two integers and print their sum.",
        "hint": "Use input(), int(), and the + operator.",
        "starter_code": "a = int(input())\nb = int(input())\n# Calculate and print the sum",
        "solution": "a = int(input())\nb = int(input())\nprint(a + b)",
        "explanation": "The + operator adds two integer values.",
        "tests": [
            {"input": "5\n3", "expected": "8"},
            {"input": "10\n20", "expected": "30"},
            {"input": "-4\n9", "expected": "5"}
        ]
    },
    {
        "id": "py_largest",
        "title": "Find the Largest Number",
        "icon": "🐍",
        "language": "Python",
        "category": "Python",
        "difficulty": "Beginner",
        "xp": 20,
        "description": "Find the largest among three numbers.",
        "question": "Read three integers and print the largest number.",
        "hint": "Use max() or conditional statements.",
        "starter_code": "a = int(input())\nb = int(input())\nc = int(input())\n# Find the largest number",
        "solution": "a = int(input())\nb = int(input())\nc = int(input())\nprint(max(a, b, c))",
        "explanation": "The max() function returns the largest value.",
        "tests": [
            {"input": "10\n20\n5", "expected": "20"},
            {"input": "7\n7\n3", "expected": "7"},
            {"input": "-5\n-2\n-9", "expected": "-2"}
        ]
    },
    {
        "id": "py_factorial",
        "title": "Factorial Calculator",
        "icon": "🐍",
        "language": "Python",
        "category": "Python",
        "difficulty": "Intermediate",
        "xp": 30,
        "description": "Calculate the factorial of a number.",
        "question": "Read a non-negative integer and print its factorial.",
        "hint": "Start with result = 1 and multiply numbers from 1 to n.",
        "starter_code": "n = int(input())\n# Calculate factorial\n",
        "solution": "n = int(input())\nresult = 1\nfor i in range(1, n + 1):\n    result *= i\nprint(result)",
        "explanation": "A factorial is the product of all positive integers up to n. Zero factorial is 1.",
        "tests": [
            {"input": "5", "expected": "120"},
            {"input": "0", "expected": "1"},
            {"input": "4", "expected": "24"}
        ]
    },
    {
        "id": "py_palindrome",
        "title": "Palindrome Checker",
        "icon": "🐍",
        "language": "Python",
        "category": "Python",
        "difficulty": "Intermediate",
        "xp": 30,
        "description": "Check whether a word reads the same backward.",
        "question": "Read a word and print Palindrome if it reads the same backward; otherwise print Not Palindrome.",
        "hint": "Compare the word with word[::-1].",
        "starter_code": "word = input()\n# Check whether the word is a palindrome",
        "solution": "word = input()\nif word == word[::-1]:\n    print('Palindrome')\nelse:\n    print('Not Palindrome')",
        "explanation": "String slicing with step -1 reverses a string.",
        "tests": [
            {"input": "madam", "expected": "Palindrome"},
            {"input": "python", "expected": "Not Palindrome"},
            {"input": "level", "expected": "Palindrome"}
        ]
    },
    {
        "id": "py_prime",
        "title": "Prime Number Checker",
        "icon": "🐍",
        "language": "Python",
        "category": "Python",
        "difficulty": "Intermediate",
        "xp": 30,
        "description": "Determine whether a number is prime.",
        "question": "Read an integer and print Prime or Not Prime.",
        "hint": "A prime number is greater than 1 and has no divisors other than 1 and itself.",
        "starter_code": "n = int(input())\n# Check whether n is prime",
        "solution": "n = int(input())\nis_prime = n > 1\nfor i in range(2, int(n ** 0.5) + 1):\n    if n % i == 0:\n        is_prime = False\n        break\nprint('Prime' if is_prime else 'Not Prime')",
        "explanation": "Checking divisors up to the square root is sufficient.",
        "tests": [
            {"input": "7", "expected": "Prime"},
            {"input": "9", "expected": "Not Prime"},
            {"input": "1", "expected": "Not Prime"}
        ]
    },
    {
        "id": "debug_assignment",
        "title": "Fix the Assignment Bug",
        "icon": "🕵️",
        "language": "Python",
        "category": "Debugging",
        "difficulty": "Beginner",
        "xp": 20,
        "description": "Find and fix an assignment syntax error.",
        "question": "Fix the code so it prints Correct when number equals 10, otherwise Incorrect.",
        "hint": "Use == to compare values.",
        "starter_code": "number = int(input())\nif number = 10:\n    print('Correct')\nelse:\n    print('Incorrect')",
        "solution": "number = int(input())\nif number == 10:\n    print('Correct')\nelse:\n    print('Incorrect')",
        "explanation": "A single = assigns a value. Double == compares values.",
        "tests": [
            {"input": "10", "expected": "Correct"},
            {"input": "5", "expected": "Incorrect"}
        ]
    },
    {
        "id": "debug_loop",
        "title": "Repair the Loop",
        "icon": "🕵️",
        "language": "Python",
        "category": "Debugging",
        "difficulty": "Beginner",
        "xp": 20,
        "description": "Fix a loop that skips the final number.",
        "question": "Fix the loop so it prints numbers from 1 through n, each on a separate line.",
        "hint": "Remember that the ending value of range() is excluded.",
        "starter_code": "n = int(input())\nfor i in range(1, n):\n    print(i)",
        "solution": "n = int(input())\nfor i in range(1, n + 1):\n    print(i)",
        "explanation": "Adding 1 to the stop value includes n in the loop.",
        "tests": [
            {"input": "3", "expected": "1\n2\n3"},
            {"input": "1", "expected": "1"}
        ]
    },
    {
        "id": "debug_type",
        "title": "Fix the Data Type Error",
        "icon": "🕵️",
        "language": "Python",
        "category": "Debugging",
        "difficulty": "Beginner",
        "xp": 20,
        "description": "Correct an input conversion error.",
        "question": "Fix the program so it reads two integers and prints their sum.",
        "hint": "input() returns a string. Convert both values to integers.",
        "starter_code": "a = input()\nb = input()\nprint(a + b)",
        "solution": "a = int(input())\nb = int(input())\nprint(a + b)",
        "explanation": "Converting strings to integers makes numeric addition possible.",
        "tests": [
            {"input": "4\n6", "expected": "10"},
            {"input": "10\n20", "expected": "30"}
        ]
    },
    {
        "id": "debug_off_by_one",
        "title": "Fix the Off-by-One Error",
        "icon": "🕵️",
        "language": "Python",
        "category": "Debugging",
        "difficulty": "Intermediate",
        "xp": 30,
        "description": "Correct an incorrect loop boundary.",
        "question": "Fix the program so it calculates the sum of integers from 1 to n, inclusive.",
        "hint": "Check the stop value in range().",
        "starter_code": "n = int(input())\ntotal = 0\nfor i in range(1, n):\n    total += i\nprint(total)",
        "solution": "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total += i\nprint(total)",
        "explanation": "The stop value in range() is excluded, so use n + 1.",
        "tests": [
            {"input": "5", "expected": "15"},
            {"input": "3", "expected": "6"},
            {"input": "1", "expected": "1"}
        ]
    },
    {
        "id": "debug_mutable",
        "title": "Fix the List Update",
        "icon": "🕵️",
        "language": "Python",
        "category": "Debugging",
        "difficulty": "Intermediate",
        "xp": 30,
        "description": "Fix a list update that uses the wrong operator.",
        "question": "Fix the program so it adds the new number to the existing list and prints the updated list.",
        "hint": "Use append() to add one item to a list.",
        "starter_code": "numbers = [1, 2, 3]\nnew_number = int(input())\nnumbers + new_number\nprint(numbers)",
        "solution": "numbers = [1, 2, 3]\nnew_number = int(input())\nnumbers.append(new_number)\nprint(numbers)",
        "explanation": "append() modifies the list by adding one element at the end.",
        "tests": [
            {"input": "4", "expected": "[1, 2, 3, 4]"},
            {"input": "10", "expected": "[1, 2, 3, 10]"}
        ]
    }
]
