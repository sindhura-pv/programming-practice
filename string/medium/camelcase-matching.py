class Solution:
    def camelMatch(self, queries, pattern: str):

        result = []
        for q in queries:

            i = j = 0
            match = True

            while i < len(q):

                if j < len(pattern) and q[i] == pattern[j]:
                    j += 1

                elif q[i].isupper():
                    match = False

                i += 1

            match = match and (j == len(pattern))
            result.append(match)

        return result
