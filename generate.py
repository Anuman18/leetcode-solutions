import os

problems = {
    "Arrays": [
        "product_of_array_except_self",
        "majority_element",
        "missing_number",
        "third_maximum_number",
        "find_all_numbers_disappeared"
    ],
    "Strings": [
        "group_anagrams",
        "implement_strstr",
        "count_and_say",
        "longest_palindrome",
        "reverse_words_string"
    ],
    "TwoPointers": [
        "container_with_most_water",
        "three_sum",
        "remove_element",
        "backspace_string_compare"
    ],
    "SlidingWindow": [
        "minimum_size_subarray_sum",
        "longest_repeating_character_replacement",
        "permutation_in_string"
    ],
    "Hashing": [
        "top_k_frequent_elements",
        "subarray_sum_equals_k",
        "longest_consecutive_sequence"
    ],
    "LinkedList": [
        "merge_two_sorted_lists",
        "remove_nth_node",
        "palindrome_linked_list"
    ],
    "Stack": [
        "daily_temperatures",
        "next_greater_element",
        "evaluate_rpn"
    ],
    "Trees": [
        "max_depth_binary_tree",
        "same_tree",
        "invert_binary_tree",
        "level_order_traversal"
    ],
    "BinarySearch": [
        "binary_search",
        "search_insert_position",
        "find_min_rotated_array"
    ],
    "Matrix": [
        "set_matrix_zeroes",
        "spiral_matrix"
    ],
    "Backtracking": [
        "subsets",
        "permutations",
        "combination_sum"
    ],
    "DP": [
        "climbing_stairs",
        "house_robber",
        "coin_change",
        "longest_increasing_subsequence"
    ],
    "Misc": [
        "valid_sudoku",
        "gas_station",
        "jump_game",
        "rotate_array",
        "kth_largest_element",
        "find_peak_element",
        "merge_intervals",
        "insert_interval"
    ]
}

template = '''"""
Problem: {title}
Link: https://leetcode.com/problems/{slug}/
Difficulty: 

Approach:

Time Complexity:
Space Complexity:
"""

# Write your solution here
'''

for folder, files in problems.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        path = f"{folder}/{file}.py"
        with open(path, "w") as f:
            f.write(template.format(
                title=file.replace("_", " ").title(),
                slug=file.replace("_", "-")
            ))

print("✅ 50 Problems Generated Successfully!")