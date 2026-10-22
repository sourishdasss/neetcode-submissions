class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0

        for i, w in enumerate(words):
            for j in range(i+1, len(words)):
                print(w, words[j])

                # check if words[i] is a prefix of words[j]
                prefix = words[j].startswith(words[i])
                suffix = words[j].endswith(words[i])

                if prefix and suffix:
                    count += 1
        
        return count