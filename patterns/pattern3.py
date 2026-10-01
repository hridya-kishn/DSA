class Solution:
    def main(self, n:int) -> int:
        for i in range(n): #outer loop checks the row
            for j in range(i+1):
                print(i+1, end=" ")
            print()


obj = Solution()
obj.main(5)