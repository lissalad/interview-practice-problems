# PROBLEM: https://leetcode.com/problems/middle-of-the-linked-list/

# GIVEN: 
# the head of a singly linked list, return middle node
# if two, return second

def middle_of_the_linked_list(head):
  list = [head]
  while list[-1].next is not None:
      list.append(list[-1].next)
  middle = len(list) // 2
  return list[middle]

# not going to do anything here