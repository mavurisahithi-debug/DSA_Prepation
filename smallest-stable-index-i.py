class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        highs = accumulate(nums, max)  # max(nums[:i+1])
        lows = reversed(list(accumulate(reversed(nums), min)))  # min(nums[i:])
        return next((i for i, (hi, lo) in enumerate(zip(highs, lows)) if hi - lo <= k), -1)
