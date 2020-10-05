from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_dict = {}
        for i, num in enumerate(nums):
            if target - num in ind_dict:
                return [ind_dict[target - num], i]
            else:
                ind_dict[num] = i
