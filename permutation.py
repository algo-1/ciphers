# permutation function 
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # case for 1 letter 
    if len(sequence) == 1:
        return list(sequence)
 
    else: 
        first_letter = sequence[0]
        #recursive permutation of sequence 
        list_of_permutations = []    #of sequence minus first letter
        word_without_first_letter = sequence.replace(first_letter, "")
        #if sequence is a 2 letter word (base case) #permutation list trivial if its just a letter
        if len(word_without_first_letter) == 1:
            list_of_permutations.append(word_without_first_letter)
        else:
            #permutation of word minus first letter (recursive step) #using its insertion list for the permutation list
            for i in get_permutations(word_without_first_letter):
                list_of_permutations.append(i)
        #list_of_permutations.append(i)
    
        #insertion of first letter
        list_of_insertions = []
        for i in list_of_permutations:
            for j in range(len(sequence)):
                if j > 0:
                    list_of_insertions.append(i[:j] + first_letter + i[j:])
                else:
                    list_of_insertions.append(first_letter + i[j:])
    return list_of_insertions
    #pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    test1 = "abcd"
    print("Input:", test1)
    print("Expected Output:", ["too large"], "n = 24")
    print("Actual Output:", get_permutations(test1), "n =", len(get_permutations(test1)))

    test2 = "abcde"
    print("Input:", test2)
    print("Expected Output:", ["too large"], "n = 120")
    print("Actual Output:", get_permutations(test2), "n =", len(get_permutations(test2)))

    test3 = "b"
    print("Input:", test3)
    print("Expected Output:", ["b"], "n = 1")
    print("Actual Output:", get_permutations(test3), "n =", len(get_permutations(test3)))
    
    test4 = "bcd"
    print("Input:", test4)
    print("Expected Output:", ["bcd", "cbd", "cdb", "bdc", "dbc", "dcb"], "n = 6")
    print("Actual Output:", get_permutations(test4), "n =", len(get_permutations(test4)))

    test5 = "acd"
    print("Input:", test5)
    print("Expected Output:", ["acd", "cad", "cda", "adc", "dac", "dca"], "n = 6")
    print("Actual Output:", get_permutations(test5), "n =", len(get_permutations(test5)))



