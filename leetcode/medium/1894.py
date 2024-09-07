def chalkReplacer(chalk, k):
        n = len(chalk)
        index = 0
        chalkSum = sum(chalk)
        k = k%chalkSum
        while(True):
            if index==n:
                index = index%n
            if k >= chalk[index]:
                k -= chalk[index]
            else:
                return index
            index = index+1

print(chalkReplacer([5,1,5],22))