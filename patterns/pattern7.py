class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            for _ in range(n-i-1):
                print(" ", end="")
            for _ in range(2*i+1):
                print("*", end="")
            print()

        for i in range(1,n):
            for _ in range(i):
                print(" ", end="")
            for _ in range(2*(n-i)-1):
                print("*", end="")
            print()


obj = Solution()
obj.main(5)