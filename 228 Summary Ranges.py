class Solution():
    def summaryRanges(self, nums):
        if nums == []:
            return []
        result = []
        i = 0
        start_range = nums[0]
        range = ''

        while i != len(nums):
            if i == len(nums) - 1:
                if nums[i - 1] == nums[i] - 1:
                    range = str(start_range) + '->' + str(nums[i])
                    result.append(range)
                else:
                    result.append(str(nums[i]))
                return result
            if nums[i + 1] != nums[i] + 1:
                if nums[i + 1] == nums[i]:
                    i += 1
                    continue
                else:
                    if start_range == nums[i]:
                        result.append(str(start_range))
                        start_range = nums[i + 1]
                    else:
                        range = str(start_range) + "->" + str(nums[i])
                        result.append(range)
                        start_range = nums[i + 1]
            i += 1
        return result