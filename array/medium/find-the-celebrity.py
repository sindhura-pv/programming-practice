# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        celeb = 0
        i = 1

        while i < n:
            if celeb == i:
                i += 1
                continue

            if not knows(i, celeb) or knows(celeb, i):
                celeb = max(celeb + 1, i)

                if celeb == n:
                    return -1

                i = 0

            else:
                i += 1

        return celeb
