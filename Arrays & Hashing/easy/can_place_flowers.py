class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 1:
                continue
            if idx == 0 or flowerbed[idx - 1] == 0:
                if idx == len(flowerbed) - 1 or flowerbed[idx + 1] == 0:
                    flowerbed[idx] = 1
                    count += 1
        return n <= count
