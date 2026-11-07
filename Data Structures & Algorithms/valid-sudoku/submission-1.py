class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        i = 0
        for row in board:
            for col in range(9):
                if row[col] != ".":
                    if row[col] not in rows[i]:
                        rows[i].add(row[col])
                    else:
                        return False
                    if row[col] not in columns[col]:
                        columns[col].add(row[col])
                    else:
                        return False
                    if row[col] not in squares[(i // 3) * 3 + (col // 3)]:
                        squares[(i // 3) * 3 + (col // 3)].add(row[col])
                    else:
                        return False
            i+= 1
        return True

                



