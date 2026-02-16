class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i=="C":
                stack.pop()
            elif i=="D":
                val = stack[-1]
                stack.append(val*2)
            elif i=="+":
                num1=stack[-1]
                num2 = stack[-2]
                stack.append(num1+num2)
            else:
                stack.append(int(i))
        s=0
        for i in stack:
            s = s + i
        return s