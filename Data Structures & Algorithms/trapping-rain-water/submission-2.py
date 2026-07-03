class Solution:
    def trap(self, height: List[int]) -> int:
        # Agar graph empty hai toh 0 return karo
        if not height:
            return 0
        
        # 1. Two pointers setup karo
        l, r = 0, len(height) - 1
        
        # 2. Shuruati max pillars maintain karo
        left_max = height[l]
        right_max = height[r]
        
        total_water = 0
        
        # 3. Jab tak dono pointers takra nahi jate
        while l < r:
            # Agar left pillar chota hai, toh left se calculate karna safe hai
            if left_max < right_max:
                l += 1
                # Naya pillar left_max se lamba hai toh left_max update karo
                left_max = max(left_max, height[l])
                # Water = max capacity - khudki height
                # (Agar naya pillar sabse lamba hua, toh left_max - height[l] 0 aayega, jo logical hai)
                total_water += left_max - height[l]
            
            # Agar right pillar chota ya barabar hai, toh right se calculate karo
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
                
        return total_water
        

height = [0,2,0,3,1,0,1,3,2,1]
obj = Solution()
soln = obj.trap(height)
print(soln)