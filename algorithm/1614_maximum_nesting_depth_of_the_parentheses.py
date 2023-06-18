def maxDepth(s: str) -> int:

    max_depth = 0

    for i in range(len(s)):

        leftParentheses = s[:i+1].count("(")
        rightParentheses = s[:i+1].count(")")
        max_depth = max(max_depth, (leftParentheses - rightParentheses))

    return max_depth


print(maxDepth('(1+(2*3)+((8)/4))+1'))
print(maxDepth('(1)+((2))+(((3)))'))
