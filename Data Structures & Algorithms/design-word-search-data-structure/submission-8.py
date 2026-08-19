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


    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.word
            
            c = word[index]

            if c == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
                
            if c not in node.children:
                return False

            return dfs(node.children[word[index]], index + 1)

        return dfs(self.root, 0)
    
