def twoSum(self, nums: List[int], target: int) -> List[int]:
       lookhere = {}
       for i, v in enumerate(nums):
           diff = target - v
           if diff in lookhere:
            return [lookhere[diff], i]
           lookhere[v] = i
