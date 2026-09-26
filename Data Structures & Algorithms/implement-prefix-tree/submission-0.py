class TrieNode:
    def __init__(self):
        # represent each node & its children
        
        self.children = {} #create a variable(*dict aka hash map) -> all possible next letters
        self.endOfWord = False #mark end of valid word 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode() #null root of Trie

    def insert(self, word: str) -> None:
        curr = self.root # -> (children={}, endOfWord=False)
        for char in word:
            if char not in curr.children:
                # key-value, value of TrieNode() is like a pointer to new node
                curr.children[char] = TrieNode()
            # update pointer, move down the tree(whether it existed or was just created)     
            curr = curr.children[char] 
        curr.endOfWord = True #mark that insert(word) as a valid word  

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            #update pointer again    
            curr = curr.children[char]
        # if let say cat(c, a, t) was inserted earlier, now mark True on t   
        return curr.endOfWord  #automatically return Bool      

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True # even it ends at 'a' on 'ca', it'd make it the way to return True      
        
        