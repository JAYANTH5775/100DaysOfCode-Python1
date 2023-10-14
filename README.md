# One Problem a Day

**Problem:** Given a string, return the longest substring without repeating characters.

**Example:**

Input: "abcabcbb"

&#x20;Output: 3



Input  : "xxxxyxpppqqq"

Output : 3

**Solution:**

To solve this problem, we can use a sliding window approach. We will maintain a set of characters that have been seen so far. We will start at the beginning of the string and move a window to the right. At each step, we will check if the current character is in the set. If it is, we will remove the leftmost character from the window and continue. If it is not, we will add the current character to the set and update the longest substring.

Here is a Python implementation of the solution:

```python
def longest_substring_without_repeating_characters(str1: str) -> int:
  """
  Returns the length of the longest substring without repeating characters in the given string.

  Args:
    str1: The string to check.

  Returns:
    The length of the longest substring without repeating characters.
  """

  # Create a set to store the characters seen so far.
  seen_chars = set()

  # Initialize the longest substring length.
  longest_substring = 0

  # Start at the beginning of the string and move a window to the right.
  left = 0
  right = 0
  while right < len(str1):
    # Check if the current character is in the set.
    if str1[right] in seen_chars:
      # If it is, remove the leftmost character from the window and continue.
      seen_chars.remove(str1[left])
      left += 1
    else:
      # Otherwise, add the current character to the set and update the longest substring.
      seen_chars.add(str1[right])
      right += 1
      longest_substring = max(longest_substring, right - left)

  return longest_substring
```
