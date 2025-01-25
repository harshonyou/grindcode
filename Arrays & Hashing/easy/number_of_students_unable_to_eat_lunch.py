from collections import Counter


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        res = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
                res -= 1
            else:
                return res

        return res
