class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, possible_anagrams):
        matches = []
        for possible_anagram in possible_anagrams:
            if sorted(self.word.lower()) == sorted(possible_anagram.lower()) and self.word.lower() != possible_anagram.lower():
                matches.append(possible_anagram)
        return matches
listen = Anagram("listen")
listen.match(['hello', 'world'])
