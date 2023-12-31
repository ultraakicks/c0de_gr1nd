# Compute _x <sup>y</sup>_
Given a double _x_ and an integer _y_, compute _x <sup>y</sup>_.

## Examples
```
 Input: x = 9.871778445549765, y = 3
Output: 962.0246486149941

 Input: x = 1.0005205926241314, y = 2
Output: 1.001041456264943

 Input: x = 3.398860582608009, y = 4
Output: 133.45455538332973
```

## Solution
```python
def power(x, y):
    result = 1
    if y < 0:
        y = -y
        x = 1 / x
    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1
    return result
```

## Explanation
* When _y_ is a power of 2, the multiplications can be iterated by squaring like _x_, _x <sup>2</sup>_, (_x <sup>2</sup>_ ) _<sup>2</sup>_
* When _y_ is nonnegative, if the least significant bit of _y_ is 0, the result is (_x <sup>y &#8725; 2</sup>_ ) _<sup>2</sup>_
* When _y_ is nonnegative, if the least significant bit of _y_ is 1, the result is _x_ &times; (_x <sup>y &#8725; 2</sup>_ ) _<sup>2</sup>_
* When _y_ is negative, if the least significant bit of _y_ is 0, the result is (_1 &#8725; x <sup>-y &#8725; 2</sup>_ ) _<sup>2</sup>_
* When _y_ is negative, if the least significant bit of _y_ is 1, the result is _1 &#8725; x_ &times; (_1 &#8725; x <sup>-y &#8725; 2</sup>_ ) _<sup>2</sup>_

## Code Dissection
1. Initialize the result to 1
    ```python
    result = 1
    ```
2. If _y_ is negative, replace _y_ with _-y_ and _x_ with _1 &#8725; x_
    ```python
    if y < 0:
        y = -y
        x = 1 / x
    ```
3. Loop until _y_ == 0
    ```python
    while y:
    ```
4. If the least significant bit of _y_ is 1, compute the result = result &times; _x_
    ```python
    if y & 1:
        result *= x
    ```
5. Compute _x_ = _x_ &times; _x_ and _y_ = _y_ &#8725; 2
    ```python
    x *= x
    y >>= 1
    ```
6. Return the result of _x <sup>y</sup>_
    ```python
    return result
    ```

## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)