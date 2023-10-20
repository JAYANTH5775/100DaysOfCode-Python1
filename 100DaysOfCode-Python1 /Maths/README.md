---
description: Have a good day :)   , Every problem is divisible
---

# Divisible\_by\_3



### Problem of the Day

#### Problem Statement

You will be given an array `arr` of integers of length N. You can construct an integer from two integers by treating the integers as strings and then concatenating them. For example, 19 and 4 can be used to construct 194 and 419.

The task is to find whether it's possible to construct an integer using all the digits of these numbers such that it would be divisible by 3. If it is possible, then print 1, and if not, print 0.

#### Solution

To solve this problem, we need to check if the sum of the digits in the array `arr` is divisible by 3, as this is a requirement for the constructed integer to be divisible by 3.

Here is a Python implementation of the solution:

```python
def is_possible_to_construct(arr):
    """
    Returns 1 if it is possible to construct an integer using all the digits of the numbers in arr
    such that it would be divisible by 3. Otherwise, returns 0.
    
    Args:
        arr: A list of integers.
    
    Returns:
        1 if possible, 0 if not.
    """
    
    # Calculate the sum of digits in arr.
    digit_sum = sum([sum(map(int, str(num))) for num in arr])
    
    # Check if the digit sum is divisible by 3.
    if digit_sum % 3 == 0:
        return 1
    else:
        return 0
```

This code defines a function `is_possible_to_construct` that takes a list of integers as input and returns 1 if it's possible to construct an integer using all the digits of the numbers in `arr` such that it would be divisible by 3. Otherwise, it returns 0.

The solution works by calculating the sum of digits of all the numbers in `arr` and checking if that sum is divisible by 3, which determines if it's possible to construct such an integer.
