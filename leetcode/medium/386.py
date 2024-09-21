def lexicalOrder(n):
    result = []
    def dfs(curr):
        if curr>n:
            return
        result.append(curr)
        curr = curr*10
        for i in range(10):
            dfs(curr+i)
    for i in range(1,10):
        dfs(i)
    return result

print(lexicalOrder(100))