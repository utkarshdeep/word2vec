from converter import corpus_raw

def sentences():

    raw_sentences = corpus_raw.split('.')

    sentences = []

    for sentence in raw_sentences:
        sentences.append(sentence.split())
    return sentences