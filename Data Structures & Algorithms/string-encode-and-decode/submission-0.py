'''
Design an algorithm to encode a list of strings to a string
    - list of str -> single str

The encoded string is then sent over the network and is decoded back to the original list of strings.
    - single str -> list of str

solution:
    - encoding: simply have number corresponding to length of the word before it with delimeter if the number more than 1 digit
    - decoding: simply read this number and jump that many indices to form the word

'''


class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word))
            s += "#"
            s += word
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        word_length = 0
        l = []

        while i < len(s):
            if s[i] != "#":
                word_length *= 10
                word_length += int(s[i])
                i += 1
            else:
                i += 1
                l.append(s[i:i + word_length])
                i += word_length
                word_length = 0
        
        return l

