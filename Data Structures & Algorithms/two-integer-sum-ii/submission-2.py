class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=0
        e=len(numbers)-1
        while s<e:
            summ=numbers[s]+numbers[e]
            if summ>target:
            # Agar sum target se bada hai: Toh sum ko chota karne ke liye right pointer 
            # ko piche lao (R -= 1), kyunki piche chote numbers h
                e-=1
            elif summ<target:
            # Agar sum target se chota hai: Toh sum badhane ke liye left pointer 
            # ko aage badhao (L += 1)
                s+=1
            else:
                return [s+1,e+1]

numbers = [1,2,3,4]
target = 3
obj=Solution()
soln=obj.twoSum(numbers,target)
print(soln)