def solution(a):
    n = len(a)
    result = 0
    a.sort()
    query_array = []
    for i in range(n):
        query_array.append([a[i], a[i], 1, i-1, i+1])
        if i + 1 < n:
            query_array.append([(a[i]+a[i+1])/2, a[i]+a[i+1], 2, i-1, i+2])
    for query in query_array:
        median = query[0]
        right = n - 1
        left = query[3]
        total_sum = query[1]
        length = query[2]
        result = max(result, total_sum / length - median)
        while left >= 0 and right >= query[4]:
            total_sum += a[right]
            total_sum += a[left]
            length += 2
            left -= 1
            right -= 1
            result = max(result, total_sum / length - median)
    return result

print(solution([1,3,5,9]))