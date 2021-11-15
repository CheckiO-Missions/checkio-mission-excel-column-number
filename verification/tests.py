"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["A"],
            "answer": 1,
        },
        {
            "input": ["Z"],
            "answer": 26,
        },
        {
            "input": ["AB"],
            "answer": 28,
        },
        {
            "input": ["ZY"],
            "answer": 708,
        }
    ],
    "Extra": [
        {
            "input": ["FXSHRXW"],
            "answer": 2147483647,
        }
    ]
}
