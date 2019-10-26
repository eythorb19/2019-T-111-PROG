import string
import operator

def open_file(filename):
    try:
        file_stream = open(filename, 'r')
        return file_stream
    except FileNotFoundError:
        return None

def get_word_list(file_stream):
    ''' Reads the given stream and returns a list of lower case words.
        Punctuation at the start and end of a word are removed.
    '''
    all_words = []
       
    for line in file_stream:	# process each line
        line = line.strip() # strip leading and trailing white space
        word_list = line.split() # get a list of words in the line
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation) # remove punctuation
            all_words.append(word)

    return all_words

def get_bigrams(word_list):
    ''' Creates a dictionary of bigrams from the given word_list.
        The keys are tuples of words that co-occur, the values are their occurances counts.
    '''
    bigrams = {}
    previous_word = ''
    for word in word_list:
        if previous_word != '':
            bigram = (previous_word, word)
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        previous_word = word
    return bigrams


# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
    all_words = get_word_list(file_stream)
    bigrams = get_bigrams(all_words)
    sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1,0), reverse=True)
    bigrams_top_10 = [ sorted_bigrams[i] for i in range(0,10)]
    print(bigrams_top_10)