
corpus_raw = 'He is the king . The king is royal . She is the royal  queen '

def convert_data():


    # convert to lower case
    corpus_raw_lower = corpus_raw.lower()

    words = []

    for word in corpus_raw_lower.split():
        if word != '.': # because we don't want to treat . as a word
            words.append(word)

    words = set(words) # so that all duplicate words are removed

    word2int = {}
    int2word = {}

    vocab_size = len(words) # gives the total number of unique words

    for i,word in enumerate(words):
        word2int[word] = i
        int2word[i] = word
    return words, word2int, vocab_size