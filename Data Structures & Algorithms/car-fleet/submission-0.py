class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p ,s] for p ,s in zip(position ,speed)]
        stack = []

        for p ,s in sorted(pair)[::-1]: 
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

obj = Solution()
target = 10
position = [1,4] 
speed = [3,2]
soln = obj.carFleet(target ,position ,speed)
print(soln)

# Concept:
# A car's time to reach the target is calculated as (target - position) / speed.
# We process cars from the closest to the target to the farthest.
#
# If a car behind takes LESS THAN or EQUAL TO the time taken by the car ahead,
# it will eventually catch up with that car, so both cars become one fleet.
# Therefore, we remove the current car from the stack.
#
# If the car behind takes MORE time than the fleet ahead, it cannot catch up,
# so it forms a new fleet.
#
# The stack therefore stores the arrival time of each independent car fleet.
# The number of elements left in the stack is the total number of car fleets.