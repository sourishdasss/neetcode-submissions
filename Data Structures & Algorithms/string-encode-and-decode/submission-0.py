class Solution:
    def __init__(self):
        self.word_len = []
        self.encoded_str = ""

    def encode(self, strs: List[str]) -> str:
        for s in strs:
            self.encoded_str += s
            self.word_len.append(len(s))
        
        return self.encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr_index = 0
        curr_bound = 0

        for i, l in enumerate(self.word_len):
            curr_str = ""
            curr_bound += l
            while curr_index < curr_bound:
                curr_str += self.encoded_str[curr_index]
                curr_index += 1
            decoded.append(curr_str)
        
        return decoded
            
