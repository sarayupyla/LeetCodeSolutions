class Solution:
    def longestWord(self, words: List[str]) -> str:
       word_set=set(words)
       ans=""
       for word in words: 
          valid=True
          for i in range(1,len(word)): #for each character in word we check prefix
            if word[:i] not in word_set: #check if the prefix of the word is in word_set
                valid=False #if prefix doesnt exist then we break and move to next word
                break
          if valid:
            if len(word)>len(ans): #if word is longer than ans then update ans
               ans=word
            elif len(word)==len(ans): #if word is same length as ans then we take Lexicographically smaller one
               ans=min(ans,word)  #example("appple","apply") e comes before y so ans ="apple"
       return ans
            