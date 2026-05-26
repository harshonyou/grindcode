package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// create a dummy head and tail
	head := &ListNode{}
	tail := head
	carry := 0

	// loop through l1 and l2, until hit nil for either or
	// add the cur val for both and track the carry
	// use full-adder
	for l1 != nil && l2 != nil {
		sum := l1.Val + l2.Val + carry
		carry = sum / 10
		sum = sum % 10
		tail.Next = l1
		tail.Next.Val = sum

		l1 = l1.Next
		l2 = l2.Next
		tail = tail.Next
	}

	// if len mismatch, then there will be one list that still contains elements
	for l1 != nil {
		sum := l1.Val + carry
		carry = sum / 10
		sum = sum % 10
		tail.Next = l1
		tail.Next.Val = sum

		l1 = l1.Next
		tail = tail.Next
	}

	for l2 != nil {
		sum := l2.Val + carry
		carry = sum / 10
		sum = sum % 10
		tail.Next = l2
		tail.Next.Val = sum

		l2 = l2.Next
		tail = tail.Next
	}

	// if carry still exists then append it to the list
	if carry > 0 {
		tail.Next = &ListNode{Val: carry}
	}

	return head.Next
}

// @leet end

