class Solution:
    def main(self, n:int) -> int:
        for i in range(n):
            for j in range(i+1):
                print(" ", end="")
            # print()
            for k in range(2*(n-i)-1,0,-1):
                print("*", end="")
            print()


obj = Solution()
obj.main(5)