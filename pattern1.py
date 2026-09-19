# pattern 1

class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            print("*" * n)
            print()

obj = Solution()
answer = obj.main(4)