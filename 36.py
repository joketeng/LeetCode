class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = 9
        map = {str(i) for i in range(1,10)}
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        print(map)
        print(cols)
        for r in range(size):
            for c in range(size):
                dight = board[r][c]
                if dight == '.':
                    continue
                if dight not in map:
                    return False
                box = (size//3) * (r//(size//3)) + c//(size//3)7
                if dight in rows[r] or dight in cols[c] or dight in boxs[box]:
                    return False
                rows[r].add(dight)
                cols[c].add(dight)
                boxs[box].add(dight)
        return True