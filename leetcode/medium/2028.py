def missingRolls(rolls, mean, n):
        rhs = 0
        m = len(rolls)
        for i in rolls:
            rhs+=i
        rhs = (mean*(m+n))-rhs
            
        ans = [1]*n

        if rhs > n*6 or rhs < n :
            return []
        rhs -=n
        for i in range(n):
            ans[i]+= min(5,rhs)
            rhs -=5
            if rhs<=0:
                break
        return ans

print(missingRolls([1,5,6],3,4))
