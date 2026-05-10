package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	// iter nodes through ll
	// if next node is of same value of next next node
	// just skip the next node and dont update the current node
	// otherwise, move forward the current node
	// create dummyRef, otherwise won't be able to return a ref
	dummyRef := &ListNode{Next: head}
	node := dummyRef

	for node.Next != nil && node.Next.Next != nil {
		if node.Next.Val == node.Next.Next.Val {
			node.Next = node.Next.Next
		} else {
			node = node.Next
		}
	}

	return dummyRef.Next
}

// @leet end

