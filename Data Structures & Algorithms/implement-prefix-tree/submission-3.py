class PrefixTree:
    tree: List[defaultdict(set)]

    def __init__(self):
        self.tree = [defaultdict(set) for i in range(100)]

    def insert(self, word: str) -> None:
        for i, c in enumerate(word):
            if i < len(word) - 1:
                next_char = word[i+1]
                self.tree[i][c].add(next_char)
            else:
                self.tree[i][c].add(' ')

    def search(self, word: str) -> bool:
        for i, c in enumerate(word):
            if i < len(word) - 1:
                if c not in self.tree[i]:
                    return False
                next_char = word[i+1]
                if next_char not in self.tree[i][c]:
                    return False
            else:
                if c not in self.tree[i]:
                    return False
                next_char = ' '
                if next_char not in self.tree[i][c]:
                    return False
        return True

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 1:
            if prefix not in self.tree[0]:
                return False 

        for i, c in enumerate(prefix):
            print(i, c)
            if i < len(prefix) - 1:
                if c not in self.tree[i]:
                    return False
                next_char = prefix[i+1]
                if next_char not in self.tree[i][c]:
                    return False

        return True
        