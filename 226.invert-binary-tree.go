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
func invertTree(root *TreeNode) *TreeNode {
	// swap left and right child
	if root == nil {
		return root
	}

	left := root.Left
	right := root.Right

	root.Right = left
	root.Left = right

	invertTree(root.Left)
	invertTree(root.Right)

	return root
}

// @leet end

