class Solution:
    def main(self, n:int) -> int:
        for i in range(1,n+1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()


obj = Solution()
obj.main(5)
            
