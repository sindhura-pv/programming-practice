class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        dp = {}

        def find_word(s, i, word, d):

            nonlocal dp
            if i in dp:
                return dp[i]

            if i == len(s):
                dp[i] = True
                return True

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in d and find_word(s, j, s[i:j], d):
                    dp[i] = True
                    return True

            dp[i] = False
            return False

        return find_word(s, 0, "", wordDict)

