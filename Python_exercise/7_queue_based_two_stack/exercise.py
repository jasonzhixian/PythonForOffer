class Solution(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, val):
        return self.stack1.append(val)

    def pop_1(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        elif len(self.stack2) == 0 :
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

solution = Solution()
solution.push(1)
solution.push(2)
solution.push(3)
solution.push(4)
print(solution.stack1)

print(solution.pop_1())
print(solution.pop_1())
print(solution.pop_1())
print(solution.pop_1())