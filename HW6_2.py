import heapq
from collections import Counter


t = "Jaiman"
# a) frequency_table(st)
# Input:
def frequency_table(st):
    d = {}
    for c in st:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for elem in d:
        print(str(elem) + ' : ' + str(d[elem]))

    return d

#frequency_table(t)
# Output:
# Character Frequencies:
# 'a': 1
# 'b': 2
# 'c': 3
# 'd': 4

# b) Huffman_code(st)
def Huffman_code(st):
    freq = frequency_table(st)

    h = []

    i = 0
    for c in freq:
        heapq.heappush(h, (freq[c], i, [c, None, None]))
        i+= 1


    
    while len(h) > 1:
        freq1, c1, n1 = heapq.heappop(h)
        freq2, c2, n2 = heapq.heappop(h)
        m = [None, n1, n2]
        heapq.heappush(h, (freq1 + freq2, i, m))
        i += 1

    tempFreq, tempID, root = h[0]
    codes = {}

    def dfs(node, currCode):
        if node[0] is not None:
            codes[node[0]] = currCode
        else:
            dfs(node[1], currCode + '0')
            dfs(node[2], currCode + '1')

    dfs(root, '')

    for char in sorted(codes):
        print(char + ':' + codes[char])

    return codes


# Output:
# Huffman Codes:
# 'a': 000
# 'b': 001
# 'c': 01
# 'd': 1

def Huffman_encodes(st, codes):
    new_st = ""
    for i in st:
        new_st += codes[i]
    #print(new_st)
    return new_st

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None  

def Huffman_tree(L):
    root = Node()
    for char, code in L.items():
        current = root
        for bit in code:
            if bit == '0':
                if current.left is None:
                    current.left = Node()
                current = current.left
            else:  
                if current.right is None:
                    current.right = Node()
                current = current.right
        current.data = char 
    print("returns root")
    return root

Huffman_tree(Huffman_code(t))

def Huffman_decode(bst, tree):
    node = tree
    for i in bst:
        if tree.data is not None:
            print(tree.data)
            tree = node
        if i == '0':
            tree = tree.left
        if i == '1':
            tree = tree.right
    print(tree.data)

Huffman_decode(Huffman_encodes(t,Huffman_code(t)),Huffman_tree(Huffman_code(t)))