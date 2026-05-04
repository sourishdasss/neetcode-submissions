class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negs = []
        pos = []

        for n in nums:
            if n < 0:
                negs.append(abs(n))
            else:
                pos.append(n)

        negs = negs[::-1]

        n = len(negs)
        p = len(pos)
        cn = 0
        cp = 0
        ans = []
        while cn < n or cp < p:
            if cn < n and cp < p:
                if negs[cn] < pos[cp]:
                    ans.append(negs[cn]**2)
                    cn += 1
                else:
                    ans.append(pos[cp]**2)
                    cp += 1
            elif cn < n:
                ans.append(negs[cn]**2)
                cn += 1
            else:
                ans.append(pos[cp]**2)
                cp += 1

        print(ans)
                

        return ans