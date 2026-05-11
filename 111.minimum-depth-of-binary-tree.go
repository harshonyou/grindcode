package main

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
	// min depth is the least you can iter the tree
	// either left or right
	if root == nil {
		return 0
	}

	left := minDepth(root.Left)
	right := minDepth(root.Right)

	if root.Left == nil || root.Right == nil {
		return 1 + left + right
	}

	return 1 + min(left, right)
}

// @leet end

