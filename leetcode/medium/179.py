import functools 

def largestNumber(nums):
        nums = list(map(str, nums))
        cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x))
        nums = sorted(nums, key=functools.cmp_to_key(cmp))
        return str(int(''.join(nums[::-1])))
    
print(largestNumber([3,30,34,5,9]))