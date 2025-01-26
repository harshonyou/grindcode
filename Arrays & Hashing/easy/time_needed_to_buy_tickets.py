class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        total = 0
        want = tickets[k]
        for n in range(len(tickets)):
            if n <= k:
                total += min(tickets[n], want)
            else:
                total += min(tickets[n], want - 1)
        return total
