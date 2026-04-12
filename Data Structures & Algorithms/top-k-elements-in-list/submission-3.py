class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size=len(nums)
        
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)     # {1: 3, 2: 2, 100: 1}
        
        bucket=[[] for _ in range(size+1)]
        for val,freq in count.items():
            bucket[freq].append(val)    
            # buckets[3] = [1] ,buckets[2] = [2] ,buckets[1] = [100]
        
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
# Index 3 se 1 uthaya. res = [1] 
# Index 2 se 2 uthaya. res = [1, 2]
# len(res) == k, so Return [1, 2].

nums = [1,1,1,2,2,100]
k=2
obj=Solution()
soln=obj.topKFrequent(nums,k)
print(soln)

'''
Bucket Sort : O(n)

SHORT OVERVIEW OF THE CODE

Make a dictionary with frequency of each element.

Make a FreqList having list as element which have their index as the frequency.

Append each element from the end of FreqList till the result list reaches a length of k.
'''