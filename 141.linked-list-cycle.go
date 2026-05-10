package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	// have two ptrs: slow and fast and iter them in this manner
	// move slow ptr once while move fast ptr twice
	// if there are cycle, the fast ptr will meet slow ptr
	// if not, it will terminate just fine
	if head == nil {
		return false
	}

	slowPtr, fastPtr := head, head

	for fastPtr != nil && fastPtr.Next != nil {
		slowPtr = slowPtr.Next
		fastPtr = fastPtr.Next.Next

		// do mem comparison, since you can have iter'd to nil
		if slowPtr == fastPtr {
			return true
		}
	}

	return false
}

// @leet end

