package main

// @leet start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// create a dummy ll with tail ref
	// iter through list1 and list2
	// connect node that is of least val to tail
	// at the end, there will be a list with remaining elems
	// link all the items from that list to tail
	// return dummy ref's next

	dummyRef := &ListNode{}
	tail := dummyRef

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}

		tail = tail.Next
	}

	if list1 != nil {
		tail.Next = list1
	}

	if list2 != nil {
		tail.Next = list2
	}

	return dummyRef.Next
}

// @leet end

