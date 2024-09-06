def construct2DArray(original, m, n):
        listLen = len(original)
        if m*n != listLen:
            return []
        result = []
        k = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[k])
                k+=1
            result.append(temp)
        return result 

print(construct2DArray([1,2,3,4],2,2))
