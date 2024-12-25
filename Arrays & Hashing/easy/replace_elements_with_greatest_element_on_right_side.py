class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans = [-1] * len(arr)

        for idx in range(len(arr) - 1 - 1, -1, -1):
            ans[idx] = max(ans[idx + 1], arr[idx + 1])

        return ans
