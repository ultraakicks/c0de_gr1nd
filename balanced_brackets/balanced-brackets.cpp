//=====================
//= Balanced Brackets =
//=====================

// Problem: Given an expression string, determine whether or not
//          each sequence of '[](){}' is balanced.
// Runtime: O(n)

#include <iostream>
#include <stack>
#include <string>

class Solution {
    public: 
        bool is_balanced(std::string expression) {
            std::string str = expression;
            stack<char> stack;

            for (int i = 0; i < str.length(); i++) {
                if (str[i] == '[' || str[i] == '(' || str[i] == '{') {
                    stack.push(str[i]);
                }
                else if (stack.empty() && )
            }
        }
};

int main(void) {
    //Solution s;
    std::string test1 = "()[]{}";    // true
    std::string test2 = "{([])}";    // true
    std::string test3 = "()[";       // false

    return 0;
}