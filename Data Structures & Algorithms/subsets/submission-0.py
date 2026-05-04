class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = [[]]

        for i in nums:
            print('HEREE')
            for subset in curr[:]:
                print('HERE')
                # Add i
                new_subset = subset.copy()
                new_subset.append(i)
                curr.append(new_subset)
        
        return curr