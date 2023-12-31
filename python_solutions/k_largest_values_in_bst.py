from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    def helper(tree):
        if tree and len(result) < k:
            helper(tree.right)
            if len(result) < k:
                result.append(tree.data)
                helper(tree.left)

    result = []
    helper(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
