---
description: Every problem is solved if u get into the roots
---

# Find\_Root\_of\_number

**Problem Statement:** Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the ‘nth root is not an integer, return -1

```python
def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0
```

* The `func` function takes three arguments: `mid` (a candidate for the Nth root), `n` (the degree of the root), and `m` (the number for which we want to find the Nth root).
* It initializes `ans` to 1 and enters a loop that runs from 1 to `n`.
* Inside the loop, it multiplies `ans` by `mid` in each iteration, effectively raising `mid` to the power of `n`.
* If at any point `ans` becomes greater than `m`, it returns 2, indicating that the candidate `mid` is too high.
* If `ans` equals `m`, it returns 1, indicating that `mid` is the Nth root of `m`.
* If neither of these conditions is met, it returns 0.

```python
def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

* The `NthRoot` function takes two arguments: `n` (the degree of the root) and `m` (the number for which we want to find the Nth root).
* It initializes `low` to 1 and `high` to `m`, representing the search range for the Nth root.
* It enters a `while` loop that continues until `low` is less than or equal to `high`.
* In each iteration, it calculates the `mid` point as the average of `low` and `high`. It then calls the `func` function to check the result of raising `mid` to the power of `n`.
* If `midN` is 1, it means that `mid` is the Nth root of `m`, so the function returns `mid`.
* If `midN` is 0, it means that `mid` is too low, so it updates the `low` to `mid + 1` and continues the search in the upper half of the range.
* If `midN` is 2, it means that `mid` is too high, so it updates the `high` to `mid - 1` and continues the search in the lower half of the range.
* If the loop exits without finding the Nth root, the function returns -1 to indicate that there is no Nth root within the given range.

```python
n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)
```

* In this example, `n` is set to 3 (indicating a cube root), and `m` is set to 27.
* The `NthRoot` function is called with these arguments, and the result is stored in the variable `ans`.
* Finally, the result is printed, which in this case, would be "The answer is: 3" since the cube root of 27 is 3.
