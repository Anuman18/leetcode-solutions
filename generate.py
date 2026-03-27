import os

def create_file(title, slug):
    folder = "Problems"
    os.makedirs(folder, exist_ok=True)

    file_path = f"{folder}/{slug}.py"

    template = f'''"""
Problem: {title}
Link: https://leetcode.com/problems/{slug}/

Approach:

Time Complexity:
Space Complexity:
"""

# Paste your solution here
'''

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(template)

        print("Created:", file_path)