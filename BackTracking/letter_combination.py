"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

"""
Time Complexity Analysis:

The time complexity of the letterCombinations function is determined by two factors:
1. The total number of possible combinations.
2. The work required to construct each combination.

1. Total Number of Combinations:
   - Each digit maps to a set of letters:
     * Digits '2', '3', '4', '5', '6', '8' map to 3 letters each.
     * Digits '7' and '9' map to 4 letters each.
   - For an input string of length `n`, the total number of combinations is:
     O(3^n) in the average case (assuming digits map to 3 letters).
     O(4^n) in the worst case (if all digits are '7' or '9').

2. Work Per Combination:
   - Each combination is a string of length `n`.
   - Constructing such a string takes O(n) time.

Total Time Complexity:
- Combining the number of combinations and the work per combination, the overall complexity is:
  O(k^n * n),
  where `k` is the average number of letters per digit:
  * k = 3 for digits mapping to 3 letters (best/average case).
  * k = 4 for digits mapping to 4 letters (worst case).

Example:
- For input "23":
  * n = 2, and each digit maps to 3 letters.
  * Total combinations: 3^2 = 9.
  * Work per combination: O(2) (string length is 2).
  * Total complexity: O(3^2 * 2) = O(18).
"""


def solve(index, digits, phone, result, temp):
    # If we have reached the end of the digits string, add the current combination to the result
    if index == len(digits):
        result.append(temp)
        return
    # Get the letters corresponding to the current digit
    letters = phone[digits[index]]
    # Iterate over all the letters and add them to the current combination
    for letter in letters:
        solve(index + 1, digits, phone, result, temp + letter)


def find_letter_combinations(digits):
    if not digits:
        return []
    # Mapping of digits to letters
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []
    temp = ""
    # Backtracking function to generate combinations
    solve(0, digits, phone, result, temp)
    return result


if __name__ == "__main__":
    digits = input(f"Enter the digits: ")
    combinations = find_letter_combinations(digits)
    print(combinations)
