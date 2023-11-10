class Trie:
    def __init__(self):
        self.dict_string = {}

    def insert(self, word: str) -> None:
        dict_ref = self.dict_string        

        for char in word:
            if char not in dict_ref:
                dict_ref[char] = {}
            dict_ref = dict_ref[char]

        dict_ref['*']=''

    def search(self, word: str) -> bool:
        dict_ref = self.dict_string        

        for char in word:
            if char not in dict_ref:
                return False
            dict_ref = dict_ref[char]

        return '*' in dict_ref

    def startsWith(self, prefix: str) -> bool:
        dict_ref = self.dict_string        

        for char in prefix:
            if char not in dict_ref:
                return False
            dict_ref = dict_ref[char]

        return True
