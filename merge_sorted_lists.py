#         https://leetcode.com/problems/merge-two-sorted-lists/

# PROBLEM:
# given two lists of integers sorted from least to greatest,
# return one sorted list including the values from both

# ASSUME:
# both lists are in non-decreasing order

# PSEUDOCODE:
# create empty list
# loop until both lists empty
# check if only one list is empty, push remaining from not empty list
# if first in second list is lesser than or equal to first in first list
# pop said int from second list and append to the new list
# else pop and append from first list
# return new list

def merge_two_sorted_lists(list1, list2):

  merged_list = []

  # while lists not empty
  while (not len(list1) == 0) or (not len(list2) == 0):

      # if just list1 empty
      if(len(list1) == 0):
        transfer = list2.pop(0)

      # if just list2 empty
      elif(len(list2) == 0):
        transfer = list1.pop(0)

      # next in list1 is smaller or equal to?
      elif list1[0] <= list2[0]:
          transfer = list1.pop(0)

        # next in list2 is smaller or equal to?
      elif list1[0] > list2[0]:
          transfer = list2.pop(0)

      else:
        print("panic")

      merged_list.append(transfer)

  return merged_list


print(merge_two_sorted_lists([1, 3, 4, 7, 8], [1, 2, 2, 4]))
