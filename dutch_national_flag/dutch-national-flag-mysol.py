"""[FILL IN] Algorithm

Time Complexity: [FILL IN]
"""

RED, WHITE, BLUE = range(3)

class Solution:
    def dutch_flag_partition(pivot_index, A):
        # TODO - you fill in here.
        return
    
def main():
    s = Solution()
    test_cases = [
        (1, [1, 1, 0, 2]),
        (3, [0, 1, 2, 0, 0, 1, 2]),
        (0, [2, 0, 1, 0, 1, 0, 2, 0]),
        (6, [2, 0, 1, 2, 2, 1, 1, 2, 1]),
        (8, [2, 0, 1, 2, 2, 0, 2, 2, 1, 2, 1, 1, 2, 1])
        ]
    for num in test_cases:
        print(f'PIVOT INDEX: {num[0]}')
        print(f'BEFORE: {num[1]}')
        flag = s.dutch_flag_partition(num[0], num[1])
        print(f'AFTER: {flag}\n')

if __name__ == '__main__':
    main()