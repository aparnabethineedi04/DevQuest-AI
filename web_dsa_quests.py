
WEB_DSA_QUESTS = [
    {
        "id": "dsa_linear_search",
        "title": "Linear Search",
        "icon": "🧠",
        "language": "Python",
        "category": "DSA",
        "difficulty": "Beginner",
        "xp": 25,
        "description": "Find an element in a list.",
        "question": "Read a list of integers and a target. Print the index of the first occurrence, or -1 if it is absent.",
        "hint": "Loop through the list using enumerate().",
        "starter_code": "numbers = list(map(int, input().split()))\ntarget = int(input())\n# Find and print the target index",
        "solution": "numbers = list(map(int, input().split()))\ntarget = int(input())\nanswer = -1\nfor i, value in enumerate(numbers):\n    if value == target:\n        answer = i\n        break\nprint(answer)",
        "explanation": "Linear search checks each element until the target is found.",
        "tests": [
            {"input": "4 8 2 9\n2", "expected": "2"},
            {"input": "1 3 5\n7", "expected": "-1"}
        ]
    },
    {
        "id": "dsa_binary_search",
        "title": "Binary Search",
        "icon": "🧠",
        "language": "Python",
        "category": "DSA",
        "difficulty": "Intermediate",
        "xp": 35,
        "description": "Search efficiently in a sorted list.",
        "question": "Read a sorted list and a target. Print its index, or -1 if not found.",
        "hint": "Use left, right and middle pointers.",
        "starter_code": "numbers = list(map(int, input().split()))\ntarget = int(input())\n# Implement binary search",
        "solution": "numbers = list(map(int, input().split()))\ntarget = int(input())\nleft, right = 0, len(numbers) - 1\nanswer = -1\nwhile left <= right:\n    mid = (left + right) // 2\n    if numbers[mid] == target:\n        answer = mid\n        break\n    elif numbers[mid] < target:\n        left = mid + 1\n    else:\n        right = mid - 1\nprint(answer)",
        "explanation": "Binary search halves the search interval at each step.",
        "tests": [
            {"input": "1 3 5 7 9\n7", "expected": "3"},
            {"input": "2 4 6 8\n5", "expected": "-1"}
        ]
    },
    {
        "id": "dsa_reverse",
        "title": "Reverse an Array",
        "icon": "🧠",
        "language": "Python",
        "category": "DSA",
        "difficulty": "Beginner",
        "xp": 25,
        "description": "Reverse the order of list elements.",
        "question": "Read integers and print them in reverse order, separated by spaces.",
        "hint": "Try slicing with [::-1].",
        "starter_code": "numbers = list(map(int, input().split()))\n# Reverse and print",
        "solution": "numbers = list(map(int, input().split()))\nprint(*numbers[::-1])",
        "explanation": "Negative slicing reverses the list.",
        "tests": [
            {"input": "1 2 3 4", "expected": "4 3 2 1"},
            {"input": "9 5", "expected": "5 9"}
        ]
    },
    {
        "id": "dsa_duplicates",
        "title": "Remove Duplicates",
        "icon": "🧠",
        "language": "Python",
        "category": "DSA",
        "difficulty": "Intermediate",
        "xp": 35,
        "description": "Remove repeated values while preserving order.",
        "question": "Read integers and print the unique values in their original order.",
        "hint": "Use a set to remember values already seen.",
        "starter_code": "numbers = list(map(int, input().split()))\n# Remove duplicates while preserving order",
        "solution": "numbers = list(map(int, input().split()))\nseen = set()\nresult = []\nfor number in numbers:\n    if number not in seen:\n        seen.add(number)\n        result.append(number)\nprint(*result)",
        "explanation": "A set provides efficient membership checks while the result list preserves order.",
        "tests": [
            {"input": "1 2 2 3 1 4", "expected": "1 2 3 4"},
            {"input": "5 5 5", "expected": "5"}
        ]
    },
    {
        "id": "dsa_second_largest",
        "title": "Second Largest Element",
        "icon": "🧠",
        "language": "Python",
        "category": "DSA",
        "difficulty": "Intermediate",
        "xp": 35,
        "description": "Find the second largest distinct number.",
        "question": "Read a list of integers and print the second largest distinct value. Assume at least two distinct values exist.",
        "hint": "Use sorted() with set().",
        "starter_code": "numbers = list(map(int, input().split()))\n# Find the second largest distinct value",
        "solution": "numbers = list(map(int, input().split()))\nunique = sorted(set(numbers))\nprint(unique[-2])",
        "explanation": "Removing duplicates and sorting makes the second largest value easy to access.",
        "tests": [
            {"input": "10 20 30 40", "expected": "30"},
            {"input": "5 5 9 2", "expected": "5"}
        ]
    }
]
