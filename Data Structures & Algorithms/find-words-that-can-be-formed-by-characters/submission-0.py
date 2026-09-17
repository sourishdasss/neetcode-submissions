class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        output = 0
        
        # create chars dict
        chars_dict = defaultdict(int)
        for c in chars:
            chars_dict[c] += 1

        # create dict for each word
        for w in words:
            tmp_dict = defaultdict(int)
            valid = True

            for c in w:
                tmp_dict[c] += 1
                # skip if not formable
                if tmp_dict[c] > chars_dict[c]:
                    valid = False 

            if valid:
                output += len(w)
        
        return output

            


        