class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            for j in range(n-i):
                print(chr(ord('A') + j), end=" ")
            print()


obj = Solution()
obj.main(5)