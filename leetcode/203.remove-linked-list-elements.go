package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	// iter nodes through ll
	// if node's holding the same val, just skip the node
	// create dummyRef, otherwise won't be able to return ptr
	dummyRef := &ListNode{Next: head}
	node := dummyRef

	for node.Next != nil {
		if node.Next.Val == val {
			node.Next = node.Next.Next
		} else {
			node = node.Next
		}
	}

	return dummyRef.Next
}

// @leet end

