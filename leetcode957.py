# -- coding: utf-8 --
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        saved = set()
        ordered_list = list()
        while tuple(cells) not in saved:
            N -= 1
            saved.add(tuple(cells))
            ordered_list.append(cells)
            next_cells = [0 for item in range(len(cells))]
            for j in range(1, len(cells) - 1):
                if cells[j - 1] == cells[j + 1]:
                    next_cells[j] = 1
                else:
                    next_cells[j] = 0
            cells = next_cells
            if 0 == N:
                return cells
        index = ordered_list.index(cells)
        cycle_len = len(ordered_list) - index
        displacement = N % cycle_len
        return ordered_list[index + displacement]


if __name__ == '__main__':
    s = Solution()
    print s.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
