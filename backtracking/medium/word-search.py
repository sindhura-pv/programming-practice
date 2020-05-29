class Solution:
    def exist(self, board, word: str) -> bool:

        def find_word(board, i, j, word, num, path):

            if num == len(word) - 1:
                return True

            for x, y in {(-1, 0), (0, -1), (1, 0), (0, 1)}:

                nx, ny = i + x, j + y
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or (nx, ny) in path:
                    continue

                if board[nx][ny] == word[num + 1] and find_word(board, nx, ny, word, num + 1, path + [(i, j)]):
                    return True

            return False

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0] and find_word(board, i, j, word, 0, []):
                    return True

        return False
