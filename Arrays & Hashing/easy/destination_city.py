class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        s = set()
        for path in paths:
            s.add(path[0])

        for path in paths:
            if path[1] not in s:
                return path[1]

        return ""
