class Solution:
    def compress(self, chars: List[str]) -> int:
        s = 0

        last_index = len(chars) - 1

        i = 0
        write = 0
        while i <= last_index:
            count = 1
            curr = chars[i]

            # check if the character gets repeated in a sequence
            while i < last_index and curr == chars[i+1]:
                count += 1
                i += 1

            # write char
            chars[write] = curr
            write += 1

            # write digits
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
            
            # move to the next character
            i += 1
    
        return write