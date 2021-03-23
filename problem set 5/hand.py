import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()
        self.hand_list=[]
        self.vector=[]
        self.hand_copy={}

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE // 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand_copy.keys())
        for letter in hand_keys:
            for j in range(self.hand_copy[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        # Your code here
        list_word=list(word)
        hand_l=list(self.hand)
        hand_values=list(self.hand.values())
        for i in range(len(hand_l)):
            n=hand_values[i]
            for j in range(n):
                self.hand_list.append(hand_l[i])
        for letra in list_word:
            if letra in self.hand_list:
                self.vector.append(0)
                self.hand_list.remove(letra)
            else:
                self.vector.append(1)
        if max(self.vector)==1:
            salida=False
        else:
            salida =True
        self.hand_copy=self.hand.copy()
        if salida:
            for i in word:
                if i in self.hand_copy:
                    self.hand_copy[i]=self.hand_copy[i]-1
            hand_values_copy=list(self.hand_copy.values())
            hand_key_copy=list(self.hand_copy)
            for i in range(len(hand_values_copy)):
                if hand_values_copy[i] <= 0:
                    del self.hand_copy[hand_key_copy[i]]
        return salida

    
myHand = Hand(7)
print(myHand)
print(myHand.calculateLen())

myHand.setDummyHand('aazzmsp')
print(myHand)
print(myHand.calculateLen())

myHand.update('za')
print(myHand)
