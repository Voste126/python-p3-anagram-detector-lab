class Anagram:
    def __init__(self,word):
        self._word = word
    
    def match(self, word_list):
        array_word =[]
        #sorts the word casing to lower case 
        sorted_word = sorted(self._word.lower())

        for word in word_list:
            #first test to make sure to similar words pass the second matching letter cases in both words pass
            if word.lower() != self._word.lower()  and sorted(word.lower()) == sorted_word:
                array_word.append(word)
            
        return array_word
        

        
