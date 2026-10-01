# class Solution:
#     def main(self, n:int) -> int:
#         start = ord('A')
#         for i in range(0, n):
#             letter = chr(start + i)
#             for j in range(i+1):
#                 print(letter, end="")
#             print()


# obj = Solution()
# obj.main(5)

numbers = [12, 5, 18, 7, 20, 3, 14, 9]

square = [x ** 2 for x in numbers if x % 2 == 0 and x > 10]

print(square)