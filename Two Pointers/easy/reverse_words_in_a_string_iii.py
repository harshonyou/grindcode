class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            s = list(s)
            left, right = 0, len(s) - 1

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            print(s)
            return "".join(s)

        words = s.split()
        words = [reverse(word) for word in words]
        s = " ".join(words)

        return s
