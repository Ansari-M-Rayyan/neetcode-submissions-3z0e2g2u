class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        reverse(0,n-1)  # reversing the whole list
        reverse(0,k-1)  # reversing the starting 'k' elems
        reverse(k,n-1)  # reversing the elems after 'k'
        
nums = [1,2,3,4,5,6,7]
k = 3
obj=Solution()
soln=obj.rotate(nums,k)
print(soln)

