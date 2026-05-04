class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = set()

        def dfs(pos_sel, curr, total):
            if total == target:
                curr = sorted(curr)
                combs.add(tuple(curr))
                return
            elif total > target:
                return
            
            for i in range(len(pos_sel)):
                if pos_sel[i] == True:
                    new_sel = pos_sel.copy()
                    new_sel[i] = False
                    dfs(new_sel, curr + [candidates[i]], total + candidates[i])
        
        candidates = sorted(candidates)
        pos_sel = [True] * len(candidates)
        dfs(pos_sel, [], 0)
        
        return [list(s) for s in combs]
