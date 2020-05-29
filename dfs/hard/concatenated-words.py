class Solution:
    def findAllConcatenatedWordsInADict(self, words):

        d = set()

        def check_word(k, word):

            # print(word, k)

            if k == len(word):
                return True

            for i in range(k + 1, len(word) + 1):

                if word[k:i] in d and check_word(i, word):
                    return True

            return False

        result = []
        words.sort(key=lambda x: len(x))

        for word in words:

            if d and check_word(0, word):
                result.append(word)

            d.add(word)

        return result

