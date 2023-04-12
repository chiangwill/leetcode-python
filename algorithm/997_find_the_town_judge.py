def findJudge(n: int, trust: list[list[int]]) -> int:

    trustMap = {i: [] for i in range(1, n+1)}
    trusteeMap = {i: [] for i in range(1, n+1)}

    for t in trust:
        trustMap[t[1]].append(t[0])
        trusteeMap[t[0]].append(t[1])

    for i, jList in trustMap.items():
        if len(jList) == (n - 1) and len(trusteeMap[i]) == 0:
            return i

    return -1


print(findJudge(3, [[1, 3], [2, 3], [3, 2]]))
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))
print(findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(findJudge(2, []))
