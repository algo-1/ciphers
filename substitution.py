# Vowel substitution cipher 
import string
from permutation import get_permutations

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

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text 
        self.valid_words = load_words("words.txt")
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        faux_valid_words = self.valid_words.copy()
        return faux_valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        shift_dict = {}
        vowels_lower = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        vowels_upper = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
        letters = string.ascii_letters

        for i in letters:
            if i in vowels_lower.keys():
                shift_dict[i] = vowels_permutation[vowels_lower[i]]
            elif i in vowels_upper.keys():
                x = vowels_permutation[vowels_upper[i]]
                shift_dict[i] = x.upper()
            else:
                shift_dict[i] = i
        return  shift_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        pre_cipher = self.message_text
        post_cypher =[]
        for i in pre_cipher:
            if i in transpose_dict:
                post_cypher.append(transpose_dict[i])
            else:
                post_cypher.append(i)
        
        return "".join(post_cypher)

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowels = "aeiou"
        counts = []
        list_of_permutations = get_permutations(vowels)
        for i in list_of_permutations:        #test all permutations of vowels
            count = 0 
            count1 = 0 
            transpose_dict = self.build_transpose_dict(i)
            decrypted_message = self.apply_transpose(transpose_dict)
            for word in decrypted_message.split():
                if is_word(self.valid_words, word):
                    count += 1 
                    #print(word)            # count the number of valid words for each i 
            if list_of_permutations[0] == i:
                current_permutation = i
            else:
                for j in counts:   # only change current_permutation if it has more valid words than all in counts
                    if count > j:
                        count1 += 1
                        #print('yeah')
                if count1 == len(counts):
                    current_permutation = i
            counts.append(count)   #add i into counts 
        #print(current_permutation)    
        transpose_dict1 = self.build_transpose_dict(current_permutation)  
        decrypted_message1 = self.apply_transpose(transpose_dict1)         
        return (current_permutation, decrypted_message1)
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
   
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()
    #TODO: WRITE YOUR TEST CASES HERE
    
    #SubMessage1
    message1 = SubMessage("I will get multiple offers from FANG and have my own companies. I will be successful!")
    permutation1 = "oieau"
    enc_dict1 = message.build_transpose_dict(permutation1)
    print("Original message:", message1.get_message_text(), "Permutation:", permutation1)
    print("Expected encryption:", "E well git multepli affirs fram FONG and hovi my awn camponeis. E well bi succissful!")
    print("Actual encryption:", message1.apply_transpose(enc_dict1))

    #EncryptedSubMessage1
    enc_message1 = EncryptedSubMessage(message1.apply_transpose(enc_dict1))
    print("Decrypted message:", enc_message1.decrypt_message())
    print()

    #SubMessage2
    message2 = SubMessage("Barcelona's definitely winning the treble. Messi remains the GOAT")
    permutation2 = "ieauo"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "Birceluni's defanately wannang the treble. Messa remians, the GUIT")
    print("Actual encryption:", message2.apply_transpose(enc_dict2)) 

    #EncryptedSubMessage2
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())