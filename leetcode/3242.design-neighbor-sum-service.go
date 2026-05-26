package main

// @leet start
type NeighborSum struct {
	Grid [][]int
}

func Constructor(grid [][]int) NeighborSum {
	return NeighborSum{Grid: grid}
}

func (this *NeighborSum) getIdx(value int) (int, int) {
	for row := 0; row < len(this.Grid); row++ {
		for col := 0; col < len(this.Grid[0]); col++ {
			if this.Grid[row][col] == value {
				return row, col
			}
		}
	}

	return 0, 0
}

func (this *NeighborSum) AdjacentSum(value int) int {
	var sum int
	row, col := this.getIdx(value)
}

func (this *NeighborSum) DiagonalSum(value int) int {
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */
// @leet end

