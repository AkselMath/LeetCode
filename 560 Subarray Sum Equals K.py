class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        i = 0
        m = nums[0]
        p = 0
        lp = []
        while i < len(nums):
            if nums[i] <= k:
                while m + nums[i] > k:
                    m -= lp[0]
                    lp.pop(0)
                m += nums[i]
                lp.append(nums[i])
            else:
                m = 0
                lp = []
            if m == k:
                p += 1
            i += 1
        return p

pp = Solution()
print(pp.subarraySum([1,2,3], 3))