package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	// ll: a -> b -> c -> nil
	// create tail node
	// nil
	// nil <- a -x- b -> c -> nil
	// iter through nodes in ll
	// point node.next to tail
	// update tail to node
	// forward node to next in ll (temp var required)
	var tail *ListNode = nil

	for head != nil {
		next := head.Next
		head.Next = tail
		tail = head
		head = next
	}

	return tail
}

// @leet end

