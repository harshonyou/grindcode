package main

import "weak"

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func checkSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil && subRoot == nil {
		return true
	}

	if root == nil || subRoot == nil {
		return false
	}

	if root.Val != subRoot.Val {
		return false
	}

	return checkSubtree(root.Left, subRoot.Left) && checkSubtree(root.Right, subRoot.Right)
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	// iter trees, and check if val matches
	// if it does, do a same tree test
	if root == nil {
		return false
	}

	if root.Val == subRoot.Val {
		if checkSubtree(root, subRoot) {
			return true
		}
	}

	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

// @leet end

