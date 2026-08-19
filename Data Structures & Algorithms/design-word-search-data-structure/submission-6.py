class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def dfs(self, word, curr):
        for i, c in enumerate(word):
            if c == ".":
                for child in curr.children.values():
                    if self.dfs(word[i+1:len(word)], child):
                        return True
                return False
            elif not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)
    
