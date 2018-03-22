##############################################################################
#   Algorithm                                                                #
#       Asks for a file to read                                              #   
#       Reads the file and categorizes each word into a dictionary using     #
#       tuples                                                               #
#       of the index of each letter in the word                              #
#       Asks the user for a prefix                                           #
#       Gives the user a list of words that can complete that prefix using   #
#       the                                                                  #
#       dictionary                                                           #   
#       Repeatedly asks the user for a prefix until they quit using '#'      #
##############################################################################


import string

def open_file(): 
    """ Opens the file given to it, if the file exists. If not reprompts for\
    a new file."""
    file = input('Please insert a file name: ' )
    x=0
    while x==0:
        try:
            file_pointer = open(file, 'r')            
            x=1
        except FileNotFoundError:
            print('Please try again')
            file = input ('Enter a file name: ')
            x=0
    return (file_pointer)
    
def fill_completions(fd):
    ''' Goes through the words in the file pointer given and puts them into a
    dictionary multiple times using the indexes of each letter in the word as
    keys. Passes the dictionary.'''
    prefix_dictionary = {}
    for line in fd:
        word_list = line.split()
        for word in word_list:  
            word = word.strip(string.punctuation)
            if "'" in word:
                continue
            for i in range(len(word)):
                if (i, word[i]) in prefix_dictionary:
                    prefix_dictionary[(i, word[i])].add(word)
                else:
                    prefix_dictionary[(i, word[i])] = {word}
    return prefix_dictionary

def find_completions(prefix, c_dict):
    '''Given the dictionary from the fill_completions function and a prefix
    it goes through the index of each letter of the prefix and matches them 
    with the index of each word in the dictionary and adding all matchiing all
    words with the same indexed letters to a set. Passes the set.'''
    return_set = set()
    for i in range(len(prefix)):
        try:
            if i==0:
                return_set =c_dict[i, prefix[i].lower()]
            else: 
                return_set = return_set&c_dict[i,prefix[i].lower()]
        except KeyError:
            return_set = set()
            return(return_set)
    return return_set

words_str = ''
fp = open_file()
dictionary = fill_completions(fp)
prefix = ''
while prefix != '#': #repeatedly asks user for a prefix until they input '#'
    prefix = input('Please input a prefix or "#" to quit: ')
    if prefix == '#':
        break
    words = find_completions(prefix, dictionary)
    word_count = 0
    if words != set(): #goes through each word in the set returned by the 
                       #find_completions function and prints them
        for word in words:
            if word_count == len(words):
                words_str += word
            else:
                words_str += word + ' '
                word_count+=1
        print('Completions of {}:'.format(prefix),  words_str)
        words_str = ''
    #if no completions for the function are found, prints there were none found
    else: 
        print('Prefix has no completion')
            
    