class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Find all factors and then increment the count accordingly

        # count = 0
        # for i in range(1, num + 1):
        #     if(num % i == 0):
        #         count += 1
        
        # if (count % 2 != 0):
        #     return True
        # return False

        # Using Binary Search

        # left = 1
        # right = num
        # while left <= right:
        #     middle = left + (right - left) // 2
        #     square = middle * middle

        #     if(square == num): 
        #         return True
        #     elif square > num:
        #         right = middle - 1
        #     else:
        #         left = middle + 1

        # return False

        # Using a simpler approach

        a = int(num ** 0.5)
        if a * a == num:
            return True
        return False
