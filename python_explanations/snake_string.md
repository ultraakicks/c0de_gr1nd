# Write a String Sinusoidally
Given an input string _s_, return the snake/sinuisoidal/zig-zag string.

The string "Hello_World!" written sinusoidally:
```
  e       _       l
H   l   o   W   r   d
      l       o       !
```
_ = blank

## Examples
```
 Input: 'Python_is_fun!'
Output: 'yn_!Pto_sfnhiu'

 Input: 'White_Board'
Output: 'h_rWieBadto'
```

## Pythonic Solution
```python
def snake_string(s):
    return s[1::4] + s[::2] + s[3::4]
```

## Explanation
* The pythonic solution uses slice notation which follows the syntax: `s[start:stop:step]`

Let's assume the input string _s_ is 'Hello_World!' and make sense of these slices:

|     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**0**|     |  e  |     |     |     |  _  |     |     |     |  l  |     |  !  |
|**1**|  H  |     |  l  |     |  o  |     |  W  |     |  r  |     |  d  |     |
|**2**|     |     |     |  l  |     |     |     |  o  |     |     |     |     |

Using the figure, it is much easier to analyze each row:

* Let _start_ = first index with a character in a row
* Let _step_ = number of indexes each subsequent character occurs

1. Row 1:
    * _start_ = 1
    * _step_  = 4
2. Row 2:
    * _start_ = 0
    * _step_  = 2
3. Row 3:
    * _start_ = 3
    * _step_  = 4

## Pythonic Code Dissection
1. Return the snake string using the slices of the string in sinusoidal fashion
    ```python
    return s[1::4] + s[::2] + s[3::4]
    ```
    * Note how each slice corresponds to the analysis of each row in the explanation