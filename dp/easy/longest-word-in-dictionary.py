class Solution:
    def longestWord(self, words):

        res = ""
        dp = {}

        def can_be_constructed(word, words):

            nonlocal dp
            if len(word) == 1:
                dp[word] = True if word in words else False
                return dp[word]

            if word not in words:
                dp[word] = False
                return dp[word]

            if word[:-1] in dp:
                dp[word] = dp[word[:-1]]
                return dp[word]

            return can_be_constructed(word[:-1], words)

        words.sort(key=lambda x: len(x))

        for w in words:

            is_good_word = can_be_constructed(w, set(words))
            # print(w, is_good_word, res)
            if is_good_word:
                # print(w, res)
                if len(w) > len(res) or (len(w) == len(res) and w < res):
                    res = w

        return res
