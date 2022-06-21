# PROBLEM: https://leetcode.com/problems/sort-colors/

# given an array of digits with values of 0-2, return the list in order
# least to greatest

# LIMITS: cannot use built in sort() function

# PSEUDOCODE:
# loop through list

def sort_colors(nums):
  for index in range(len(nums)):
    if index > 0:
      while nums[index-1] < nums[index]:
        nums[index], nums[index-1] = nums[index-1], nums[index]
  return nums

print(sort_colors([0,1,2]))