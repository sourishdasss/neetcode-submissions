class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        output = []

        while left <= right and top <= bottom:
            # left to right
            for i in range(left, right + 1):
                print("lr")
                output.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom + 1):
                print("tb")
                output.append(matrix[i][right])
            right -= 1

            print(left, right, top, bottom)
            if left > right or top > bottom:
                break

            # right to left
            for i in range(right, left - 1, -1):
                print("rl")
                output.append(matrix[bottom][i])
            bottom -= 1

            # bottom to top
            for i in range(bottom, top - 1, -1):
                print("bt")
                output.append(matrix[i][left])
            left += 1
        
            print(left, right, top, bottom)







        # d = 1
        # count = 0
        # while count < (n * m):
        #     if d == 1:
        #         print("1")
        #         if left > right: break
        #         for i in range(left, right + 1):
        #             output.append(matrix[top][i])
        #             count += 1
        #             print(output)
        #         d = 2
        #         top += 1
            
        #     elif d == 2:
        #         print("2")
        #         if top > bottom: break
        #         for i in range(top, bottom + 1):
        #             output.append(matrix[i][right])
        #             count += 1
        #             print(output)
        #         d = 3
        #         right -= 1 

        #     elif d == 3:
        #         print("3")
        #         if left > right: break
        #         for i in range(right, left - 1, -1):
        #             output.append(matrix[bottom][i])
        #             count += 1
        #             print(output)
        #         d = 4
        #         bottom -= 1

        #     elif d == 4:
        #         print("4")
        #         if top > bottom: break
        #         for i in range(bottom, top - 1, -1):
        #             output.append(matrix[i][left])
        #             count += 1
        #             print(output)
        #         d = 1
        #         left += 1
  
        
        # print(output)

        return output


