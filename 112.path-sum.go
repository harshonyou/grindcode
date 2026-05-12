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
func hasPathSum(root *TreeNode, targetSum int) bool {
	// if root is nil, no summation possible
	// if root has no child (leaf), check if target sum is zero
	// if not, keep decreasing targetSum by current val
	if root == nil {
		return false
	}

	if root.Left == nil && root.Right == nil {
		return targetSum == root.Val
	}

	newSum := targetSum - root.Val
	return hasPathSum(root.Left, newSum) || hasPathSum(root.Right, newSum)
}

// @leet end

