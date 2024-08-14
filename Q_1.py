from queue import PriorityQueue
def solution(source, target):
    if len(target) == 0:
        return 0

    source_set = set(source)
    target_set = set(target)
    if source_set != target_set:
        return -1

    ans = 1
    source_index = 0
    for target_index in range(len(target)):
        while True:
            if source[source_index] == target[target_index]:
                source_index += 1
                if source_index == len(source) and target_index + 1 != len(target):
                    source_index = 0
                    ans += 1
                break
            source_index += 1
            if source_index == len(source):
                source_index = 0
                ans += 1
    return ans

print(solution("abc", "abcbc"))
print(solution("abc", "acdbc"))
print(solution("xyz", "xzyxz"))