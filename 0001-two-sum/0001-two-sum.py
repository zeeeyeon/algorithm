class Solution(object):
    def twoSum(self, nums, target):
        dict = {}

        for i, num in enumerate(nums):
            number = target - num

            if number in dict:
                return [dict[number], i]

            dict[num] = i
        return []
        