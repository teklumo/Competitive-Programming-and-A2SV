class Solution:
    def removeStars(self, s: str) -> str:
        num1 = []
        n1 = list(s)
        for n in range(len(n1)):
            if n1[n] != "*":
                num1.append(n1[n])
            else:
                if len(num1) != 0:
                    num1.pop()
        return "".join(num1)
