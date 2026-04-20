class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst=[]
        s=0
        e=len(numbers)-1
        while s<e:
            summ=numbers[s]+numbers[e]
            if summ>target:
                e-=1
            elif summ<target:
                s+=1
            else:
                lst.append(s+1)
                lst.append(e+1)
                return lst

numbers = [1,2,3,4]
target = 3
obj=Solution()
soln=obj.twoSum(numbers,target)
print(soln)