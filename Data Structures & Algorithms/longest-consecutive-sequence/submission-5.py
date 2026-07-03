class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        maxlen = 1
        for num in numset:
            if (num-1) not in numset:
                cur = 1
                while (num+cur) in numset:
                    cur += 1
                maxlen = max(maxlen,cur)
        return maxlen