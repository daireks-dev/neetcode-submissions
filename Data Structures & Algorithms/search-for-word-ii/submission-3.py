class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = []

        visited = set()

        trie = Trie()
        for word in words:
            trie.add(word)

        def dfs(r, c, curr):
            if (min(r, c) < 0 or
            r >= ROWS or c >= COLS or 
            (r, c) in visited or
            not board[r][c] in curr.children):
                return

            curr = curr.children[board[r][c]]
            if curr.isWord:
                res.append(curr.word)
                curr.isWord = False

            visited.add((r, c))

            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)
        
        return res


        