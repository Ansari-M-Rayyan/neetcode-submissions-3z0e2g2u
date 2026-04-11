class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def heapify(n,i):
            largest=i
            l=2*i+1
            r=2*i+2

            if l<n and nums[l]>=nums[largest]:
                largest=l

            if r<n and nums[r]>=nums[largest]:
                largest=r

            if largest!=i:
                nums[largest],nums[i]=nums[i],nums[largest]
                heapify(n,largest)

        n=len(nums)
        for i in range(n//2-1,-1,-1):
            heapify(n,i)

        for i in range(n-1,0,-1):
            nums[i],nums[0]=nums[0],nums[i]
            heapify(i,0)

nums = [1,0,1,2]
obj=Solution()
soln=obj.sortColors(nums)
print(soln)