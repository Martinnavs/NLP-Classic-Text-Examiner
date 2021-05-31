from collections import Counter

# function that pulls chunks out of chunked sentence and finds the most common chunks
def chunk_counter(chunked_sentences, label):

    # create a list to hold chunks
    chunks = list()
    
    # for-loop through each chunked sentence to extract chunks
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == label):
            chunks.append(tuple(subtree))

    # create a Counter object
    chunk_counter = Counter()

    # for-loop through the list of chunks
    for chunk in chunks:
        # increase counter of specific chunk by 1
        chunk_counter[chunk] += 1

    # return 30 most frequent chunks
    return chunk_counter.most_common(30)