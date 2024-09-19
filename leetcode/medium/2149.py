def longestSubarray(self, nums):
        result = 0
        lenSubArray = 0

        maxElement = max(nums)
        for num in nums:
            if num == maxElement:
                lenSubArray+=1
            else:
                lenSubArray=0
            result = max(result,lenSubArray)
        return result