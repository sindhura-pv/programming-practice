class Solution:
    def longestValidParentheses(self, st: str) -> int:

        if len(st) < 2:
            return 0

        def traverse(st):

            cc = oc = m = 0
            s = e = 0
            n = len(st)

            while e < n:

                if st[e] == '(':
                    oc += 1
                else:
                    cc += 1

                if cc == oc:
                    m = max(m, 2 * cc)
                if cc > oc:
                    oc = cc = 0

                e += 1

            e -= 1
            cc = oc = 0
            while e >= 0:
                if st[e] == '(':
                    oc += 1
                else:
                    cc += 1
                if cc == oc:
                    m = max(m, 2 * cc)
                if oc > cc:
                    oc = cc = 0

                e -= 1

            return m

        return traverse(st)