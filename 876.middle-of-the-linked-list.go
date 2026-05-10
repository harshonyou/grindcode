package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
	// iter through the ll in this manner
	// slow ptr moves once, fast ptr moves twice
	// when the fast ptr reaches "nil", we stops
	// correctness: if n-odd elem, we at n/2-even
	// if (n+1)-even elem, we at (n+1+1)/2-even
	slowPtr, fastPtr := head, head

	for fastPtr != nil && fastPtr.Next != nil {
		slowPtr = slowPtr.Next
		fastPtr = fastPtr.Next.Next
	}

	return slowPtr
}

// @leet end

