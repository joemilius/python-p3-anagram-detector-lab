# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
        pass

    def match(self, list):
        found_list = []
        for word in list:
            if sorted([letter for letter in word]) == sorted([letter for letter in self.word]):
                found_list.append(word)
        
        return found_list
        pass
    
    
    
    
    
    pass