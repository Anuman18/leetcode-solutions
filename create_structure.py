import os

structure = {
    "Arrays": [
        "move_zeroes",
        "find_pivot_index",
        "sort_array_by_parity",
        "maximum_subarray",
    ],
    "Strings": [
        "roman_to_integer",
        "valid_palindrome",
    ],
    "Matrix": [
        "matrix_similarity_after_cyclic_shifts",
    ]
}

template = '''"""
Problem: {name}
Link: https://leetcode.com/problems/{slug}/
Difficulty: 

Approach:

Time Complexity:
Space Complexity:
"""
'''

for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        filename = f"{folder}/{file}.py"
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(template.format(
                    name=file.replace("_", " ").title(),
                    slug=file.replace("_", "-")
                ))

print("Structure Created ✅")