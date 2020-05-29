from collections import deque
import numpy as np


class Solution:
    def slidingPuzzle(self, b) -> int:

        ideal = tuple((1, 2, 3, 4, 5, 0))
        start = tuple(itertools.chain(*b))
        que = deque()
        que.append([start, start.index(0), 0])
        vis = {start}

        while que:

            board, zero, level = que.popleft()
            if board == ideal:
                return level

            for i in (1, -1, -3, 3):

                # print(abs((zero+i)/3 - zero/3) + abs((zero+i)%3 - zero%3))
                if int(abs((zero + i) / 3 - zero / 3) + abs((zero + i) % 3 - zero % 3)) != 1:
                    continue

                if zero + i < 6 and zero + i >= 0:

                    new_board = [ele for ele in board]
                    new_board[zero], new_board[zero + i] = new_board[zero + i], new_board[zero]

                    if tuple(new_board) not in vis:
                        que.append([tuple(new_board), zero + i, level + 1])
                        vis.add(tuple(new_board))

        return -1