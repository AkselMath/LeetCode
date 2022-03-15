class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        i = 0
        j = 0
        k = 0
        a = []
        while i < len(nums):
            if nums[i]:
                k += 1
            if i == len(nums) - 1 or not nums[i]:
                j += 1
                a.append(k)
                k = 0
            i += 1
        j -= 1
        if j == 0:
            return max(a) - 1
        elif j == len(a):
            return 0
        maxx = -1
        for i in range(len(a)-1):
            if a[i] + a[i+1] > maxx:
                maxx = a[i] + a[i+1]

        return maxx