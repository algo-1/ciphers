#Caesar cipher 

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings 
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text 
        self.valid_words = load_words("words.txt") 
        #pass #delete this line and replace with your code here

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
        #pass #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        faux_valid_words = self.valid_words.copy()
        return faux_valid_words
        # pass #delete this line and replace with your code here

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_letters = string.ascii_lowercase
        upper_letters = string.ascii_uppercase
        shift_dict = {}
        
        for j in lower_letters:
            if lower_letters.index(j) + shift < 26:
                shift_dict[j] = lower_letters[lower_letters.index(j) + shift] 
            elif lower_letters.index(j) + shift >= 26:
                shift_dict[j] = lower_letters[lower_letters.index(j) + shift - 26] 
        for k in upper_letters:
            if upper_letters.index(k) + shift < 26:
                shift_dict[k] = upper_letters[upper_letters.index(k) + shift]
            elif upper_letters.index(k) + shift >= 26:
                shift_dict[k] = upper_letters[upper_letters.index(k) + shift - 26]
        
        return shift_dict
            
       # pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted_dict = self.build_shift_dict(shift)
        pre_cipher = self.message_text
        post_cipher = []
        for i in pre_cipher:
            if i in shifted_dict:
               post_cipher.append(shifted_dict[i])
            else:
               post_cipher.append(i)
        
        return "".join(post_cipher)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift 
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        #pass #delete this line and replace with your code here

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift 
        #pass #delete this line and replace with your code here

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        faux_encryption_dict = self.encryption_dict.copy()

        return faux_encryption_dict
        #pass #delete this line and replace with your code here

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
        #pass #delete this line and replace with your code here

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift 
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

        #pass #delete this line and replace with your code here


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #create an empty list for storing number of valid words 
        counts = []
        #checking all possible shift values
        for shift in range(26):
            count = 0
            count1 = 0
            text = self.apply_shift(shift)
            #split the text into words and count valid words
            for word in text.split():
                if is_word(self.valid_words, word):
                   count += 1

            #set current_shift to the first shift             
            if shift == 0:
                current_shift = shift

            #only change the current_shift if a shift has more valid words than all prev shifts (count > ALL in counts)    
            if shift > 0:
                for i in counts:
                    if count > i:
                        count1 += 1
                        #print("kl")
                if count1 == len(counts):
                    current_shift = shift
                    
            #add count to counts       
            counts.append(count)     
        #assign the present value of current_shift and use        
        value = current_shift    
        return (value, self.apply_shift(value))
        #pass #delete this line and replace with your code here

if __name__ == '__main__':

    '''#Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    #PlaintextMessage
    plaintext2 = PlaintextMessage('yeah', 2)
    print('Expected Output: agcj')
    print('Actual Output:', plaintext2.get_message_text_encrypted())
    
    plaintext3 = PlaintextMessage('grow', 4)
    print('Expected Output: kvsa')
    print('Actual Output:', plaintext3.get_message_text_encrypted())

    #CiphertextMessage
    ciphertext2 = CiphertextMessage('agcj')
    print('Expected Output:', (24, 'yeah'))
    print('Actual Output:', ciphertext2.decrypt_message())

    ciphertext3 = CiphertextMessage('ettpi')
    print('Expected Output:', (22, 'apple'))
    print('Actual Output:', ciphertext3.decrypt_message())'''

    #TODO: best shift value and unencrypted story 
    ciphertext_story = CiphertextMessage(get_story_string())
    print('Actual Output:', ciphertext_story.decrypt_message())
    
    # Best Shift Value = 12
    # Unencrypted Story
    #'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.'
   