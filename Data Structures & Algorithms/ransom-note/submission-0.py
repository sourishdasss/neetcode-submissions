class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create magazine dict
        magazine_dict = defaultdict(int)

        # create ransom dict
        ransom_dict = defaultdict(int)

        for c in magazine:
            magazine_dict[c] += 1
        
        for c in ransomNote:
            ransom_dict[c] += 1

            if ransom_dict[c] > magazine_dict[c]:
                return False

        return True