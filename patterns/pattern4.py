class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            for j in range(n - i):
                print(j+1, end="")
            print()


obj = Solution()
obj.main(5)