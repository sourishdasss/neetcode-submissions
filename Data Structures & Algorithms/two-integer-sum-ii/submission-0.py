class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        answer = []

        while start < end:
            tmp = numbers[start] + numbers[end] 
            if tmp == target:
                answer = [start, end]
                break
            elif tmp < target:
                start += 1
            else:
                end -= 1

        answer[0] += 1
        answer[1] += 1
        
        return answer
