class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
    
    # "." in the word ->at this position, the character can be any letter
    # With that, the *trick part* is to try all possible child nodes and see if any path leads to a full word match
    # -> dfs going deeper in each recursively    
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root 

            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    # *wanna visit every child node corresponding to that letter
                    # .values() is the pointer to the next possible branches
                    for child in curr.children.values(): 
                        # in the end child is just TrieNode() which is free to go over whichever
                        if dfs(i + 1, child): 
                            return True
                        # even if like do. as the current pointer would be at 'o', it'd go through all the branches and return True at first    
                    return False
                else:
                    # standard code
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]   
            return curr.word # Bool

        return dfs(0, self.root)#called                
