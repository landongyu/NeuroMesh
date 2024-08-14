def solution(s):
    n = len(s)
    result = [' ' for i in range(n)]
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'
    while stack:
        result[stack[-1]] = 'x'
        stack.pop()
    print(s)
    print("".join(result))

solution('bge)))))))))')
solution('((IIII))))))')
solution('()()()()(uuu')
solution('))))UUUU((()')