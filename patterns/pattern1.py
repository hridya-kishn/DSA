# pattern 1

class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

obj = Solution()
answer = obj.main(4)