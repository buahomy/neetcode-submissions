class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # increasing order of tupels(position, speed)
        tuples = []
        for i in range(len(speed)):
            tuples.append((position[i], speed[i]))
        tuples.sort()

        # monotonic stack & violated rule
        
        stack = []
        for pos, sp in tuples[::-1]:
            time = (target - pos) / sp
            stack.append(time)
            # if because, a car, cannot pass by and would compare to only one ahead of it at a time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)        