package main

import (
	"strconv"
	"strings"
)

// @leet start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func binaryTreePaths(root *TreeNode) []string {
	// keep track of visited node and in the leaf join them together
	var result []string
	if root == nil {
		return result
	}

	var seen []string

	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}

		seen = append(seen, strconv.Itoa(node.Val))

		if node.Left == nil && node.Right == nil {
			result = append(result, strings.Join(seen, "->"))
		} else {
			dfs(node.Left)
			dfs(node.Right)
		}

		seen = seen[:len(seen)-1]
	}

	dfs(root)
	return result
}

// @leet end

