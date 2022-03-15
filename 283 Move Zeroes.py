class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                k += 1
                i += 1
                continue
            if k != 0:
                nums[i], nums[i-k] = nums[i-k], nums[i]

            i += 1

        return nums