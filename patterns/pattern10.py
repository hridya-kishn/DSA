class Solution:
    def main(self, n:int) -> int:
        for i in range(1,n+1):
            for j in range(i):
                print(j+1, end="")
            
            # for _ in range(n+1-i,1,-1):
            for _ in range(2*(n-i)):
                print(" ", end="")
            for m in range(i):
                print(i-m, end="")
            print()

obj = Solution()
obj.main(5)