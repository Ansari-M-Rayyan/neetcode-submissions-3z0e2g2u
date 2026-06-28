class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i , 0) + 1 # {1: 3, 2: 2, 100: 1}
        sorted_dict = dict(sorted(hashmap.items() , key = lambda x:x[1] , reverse = True))
        return list(sorted_dict.keys())[:k]

nums = [1,1,1,2,2,100]
k=2
obj=Solution()
soln=obj.topKFrequent(nums,k)
print(soln)

'''

hashmap.items(): Dictionary ko pairs mein tod deta hai -> [(1, 3), (2, 2), (100, 1)]. 
Yahan har tuple hai (number, uski_frequency).
lambda x: x[1]: Yeh sorting ka rule hai. Yeh kehta hai ki tuple x ke index 1 (yani frequency) ke hisaab se sort karo. 
Agar x[0] likhte toh woh keys (number) ke hisaab se sort karta.
reverse = True: Bade numbers (highest frequency) pehle aayenge (Descending order).
dict(...): Wapas us list ko dictionary bana deta hai.
Resulting sorted_dict: {1: 3, 2: 2, 100: 1} (Highest count pehle).

'''