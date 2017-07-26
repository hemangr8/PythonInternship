import numpy as np
from scipy.sparse import csgraph
from scipy.spatial.distance import pdist, squareform
from scipy import sparse

word_list = open('/home/optimus-45/PycharmProjects/WordLadder/dictionary.txt').read().split()

# keep 4-letter words
word_list = filter(lambda w: len(w) == 4, word_list)
# no punctuation
word_list = filter(str.isalpha, word_list)
# no proper nouns or acronyms
word_list = filter(str.islower, word_list)

word_list = np.sort(list(word_list), axis=None)

print(word_list.shape)

# represent every word in bytes
word_bytes = np.ndarray((word_list.size, word_list.itemsize), dtype='int8', buffer=word_list.data)
print(word_bytes.shape)

hamming_dist = pdist(word_bytes, metric='hamming')
graph = sparse.csr_matrix(squareform(hamming_dist < 1.01 / word_list.itemsize))

print(graph.shape)

i1 = word_list.searchsorted("5555")
print(i1, word_list[i1])

i2 = word_list.searchsorted("2255")
print(i2, word_list[i2])

distances, predecessors = csgraph.shortest_path(graph, return_predecessors=True)
print("distance from '%s' to '%s': %i steps" % (word_list[i1], word_list[i2], distances[i1, i2]))

print(np.ma.masked_invalid(distances).max())

i = i1
while i != i2:
    print(word_list[i])
    i = predecessors[i2, i]
print(word_list[i2])

i1, i2 = np.where(distances == 16)
unique_paths = (i1 < i2)
long_list = list(zip(word_list[i1][unique_paths], word_list[i2][unique_paths]))

print(long_list)


