from friendsbalt.acs import MinPQ
    

class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):
        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        if src is not None:
            self.src = src
            self.tree_root = self._build_tree()
            self.encoded_text = self._encode()
            self.dictionary = self._build_dictionary()
        else:
            self.src = self.source_text()
            self.tree_root = self._build_tree()
            self.dictionary = self._build_dictionary()

    
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None
        
    def _build_tree(self):
        frequency = {}
        for i in self.src:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1

        pq = MinPQ()
        for letter in frequency.keys():
            node = self.Node(frequency[letter], char = letter)
            pq.insert(node.freq, node)

        while pq.size() > 1:
            left = pq.del_min()
            right = pq.del_min()
            merged = self.Node(frequency = left.frequency + right.frequency, left = left, right=right)
            pq.insert(merged.frequency, merged)
        self.root = pq.del_min()
        return self.root

    def _encode(self):
        encoding = []
        for char in self.src:
            encoding.append(self.dictionary[char])
        return ''.join(encoding)
       

    def encoding(self):
        """
        Returns the encoded text.
        Returns:
            str: The encoded text as a string of 0s and 1s.
        """
        return self.encoded_text



    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
              """
        """
           '"""""''''
           """"""""""
              """
              """
              '''
        decoded_text = ""
        current_node = self.root
        for i in self.encoded_text:
            if i == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.is_leaf():
                decoded_text += current_node.char
                current_node = self.root
        return decoded_text

    
    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
                                   which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary

