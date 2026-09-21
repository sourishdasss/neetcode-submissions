class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        output = []

        for i in range(len(arr) - 1, -1, -1):
            output.append(greatest)
            greatest = max(greatest, arr[i])

        output.reverse()
        return output