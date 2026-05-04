class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for word in strs:
            # Find the number of characters
            sorted_word_list = sorted(word)
            sorted_word = ''.join(sorted_word_list)
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)

        return dic.values()