from collections import defaultdict as dd


class Solution:
    def longestStrChain(self, words) -> int:

        words.sort(key=lambda x: len(x))

        def sub_words(word):

            l = []
            for i in range(len(word) - 1):
                sub_word = word[:i] + word[(i + 1):]
                l.append(sub_word)

            l.append(word[:-1])

            return l

        dp = dd(int)
        for w in words:
            dp[w] = 1

        for w in words:
            max_sw = max([dp[sw] for sw in sub_words(w)])
            dp[w] = max(dp[w], max_sw + 1)

        return max([dp[w] for w in words])


