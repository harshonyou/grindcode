package main

import "fmt"

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
	// find the middle
	// split the ll in the middle
	// reverse the later middle half
	// compare if both holds the same values
	slowPtr, fastPtr := head, head

	for fastPtr != nil && fastPtr.Next != nil {
		slowPtr = slowPtr.Next
		fastPtr = fastPtr.Next.Next
	}

	var tail *ListNode = nil
	node := slowPtr
	for node != nil {
		next := node.Next
		node.Next = tail
		tail = node
		node = next
	}

	for tail != nil {
		if tail.Val != head.Val {
			return false
		}

		tail = tail.Next
		head = head.Next
	}

	return true
}

// @leet end

