"""
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
You then will need to create encoding, decoding, and sizing schemas.

For Example:

"""
import sys
import collections


class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    @staticmethod
    def fuse(node_1, node_2):
        """
        Combines two nodes together, by using then as the leafs of a new node
        """

        node = Node()

        if node_1.freq <= node_2.freq:
            node.left = node_1
            node.right = node_2
        else:
            node.left = node_2
            node.right = node_1

        node.freq = node_1.freq + node_2.freq

        return node

    def __repr__(self):
        return "Node --> character: {} | frequency: {}".format(self.char, self.freq)


class Queue(object):
    def __init__(self, string):
        letters_freq = {}
        for letter in string:
            if letter not in letters_freq:
                letters_freq[letter] = 1
            else:
                letters_freq[letter] += 1
        # letters_freq = collections.Counter(string)

        self.arr = [Node(char=letter, freq=freq)
                    for letter, freq in letters_freq.items()]
        self.sort()

    def sort(self):
        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def fuse(self):
        node_1 = self.arr.pop()
        node_2 = self.arr.pop()

        new_node = Node.fuse(node_1, node_2)
        self.arr.append(new_node)

        self.sort()


class Tree(object):
    def __init__(self, queue):

        #  Fuse on every 2 elements
        while len(queue.arr) > 1:
            queue.fuse()
        # Add as the root of the tree the first element of the array
        self.root = queue.arr[0]

    def to_binary(self):
        """
        Converts a Tree into binary, by changing Node.char information for a 1/0 value;
        """

        self.root = self.to_binary_recursive_helper(self.root)
        self.root.freq = 0

    # def __repr__(self):
    #     current = self.root
    #     return "Node of character: {} | frequency: {}".format(self.char, self.freq)

    @staticmethod
    def to_binary_recursive_helper(node):
        if node.left is None and node.right is None:
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree.to_binary_recursive_helper(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree.to_binary_recursive_helper(node.right)

        return node


class Huffman(object):
    def __init__(self, tree):
        self.encoding_table = self.create_encoding_table('', tree.root)
        #  Create encoding dictionary
        self.encoding_dict = dict()
        for element in self.encoding_table:
            self.encoding_dict[element[0]] = element[1]

        #  Create decoding dictionary
        self.decoding_dict = dict()
        for element in self.encoding_table:
            self.decoding_dict[element[1]] = element[0]

    @staticmethod
    def create_encoding_table(base_code, node):
        """
        Initializes the encoding table, for this we traverse the binary-tree
        """
        if node.left is None and node.right is None:
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        encoding_table = []

        if node.char is not None:
            encoding_table.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            encoding_table.extend(
                Huffman.create_encoding_table(current_code, node.left))

        if node.right is not None:
            encoding_table.extend(Huffman.create_encoding_table(
                current_code, node.right))

        return encoding_table

    def encode(self, string):
        coded_string = ''
        for char in string:
            coded_string += self.encoding_dict[char]

        return coded_string

    def decode(self, coded_string):
        decoded_text = ''

        while len(coded_string) > 0:
            i = 1
            while True:
                if coded_string[:i] in self.decoding_dict.keys():
                    decoded_text += self.decoding_dict[coded_string[:i]]
                    coded_string = coded_string[i:]
                    break
                i += 1

        return decoded_text


def huffman_encoding(data):
    if len(data) == 0:
        print("For Huffman encoding to work you need to pass a String with lenght > 0")
        return

    # create a queue with the data
    queue = Queue(data)  # Ok
    # Create a Tree with the queue
    tree = Tree(queue)
    # Convert the tree into a binaryze tree
    tree.to_binary()
    # Create a Huffman class and append the tree
    huffman_encoder = Huffman(tree)
    # TODO: We encode the data
    text_encoder = huffman_encoder.encode(data)

    return text_encoder, huffman_encoder


def huffman_decoding(data, encoder):
    return encoder.decode(data)


if __name__ == "__main__":
    codes = {}

    # Case 1
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000010011001110010000110100010100010001010000000000100000101100111001000110000111010100010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word

    # Edge Cases

    # Case 2
    empty_sentence = ""
    print("The content of the data is: {}\n".format(empty_sentence))
    # The content of the data is:
    huffman_encoding(empty_sentence)
    # For Huffman encoding to work you need to pass a String with lenght > 0

    # Case 3
    repeated_letters = "cccccc"
    print("The content of the data is: {}\n".format(repeated_letters))
    # The content of the data is: cccccc
    encoded_data, tree = huffman_encoding(repeated_letters)
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000000
