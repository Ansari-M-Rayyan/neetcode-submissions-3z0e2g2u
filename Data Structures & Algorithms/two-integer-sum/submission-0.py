class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[nums[i]]=i
        return []

nums = [2, 11, 7, 15]
target = 9
obj=Solution()
soln=obj.twoSum(nums,target)
print(soln)

'''
Iteration 0

Current number: 2
Calculate difference: 9 − 2 = 7
Check hashmap: Is 7 present in {}? → No
Action: Store 2 with index 0 → {2: 0}

Iteration 1

Current number: 11
Calculate difference: 9 − 11 = -2
Check hashmap: Is -2 present in {2: 0}? → No
Action: Store 11 with index 1 → {2: 0, 11: 1}

Iteration 2

Current number: 7
Calculate difference: 9 − 7 = 2
Check hashmap: Is 2 present in {2: 0, 11: 1}? → Yes
Action: Pair found → return indices [2, 0]
'''