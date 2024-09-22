def findKthNumber(n, k):
        curr = 1
        index = 1
        def countSteps(curr):
            res = 0
            nex = curr+1
            print("curr :",curr)
            while curr <=n:
                res+= min(nex,n+1) - curr
                curr*= 10
                nex*=10
            return res
        
        while index<k:
            steps = countSteps(curr)
            print("steps :",steps)
            if index+steps<=k:
                curr = curr+1
                index+=steps
            else:
                curr*=10
                index+=1
        return curr

print(findKthNumber(30,2))