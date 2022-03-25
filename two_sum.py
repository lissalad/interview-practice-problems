#    https://leetcode.com/problems/two-sum/

# PROBLEM:
# given a list of numbers and a target number, return the list indices of
# two number in the list with a sum of that target number

# ASSUME:
# each input has exactly one solution
# each element can be used once

# PSEUDOCODE:
# create loop to repeat until target sum is reached
# loop through nums. set goal for what would create the sum
# if sum exists in nums list, and is not the same as the current num selected, return each index, break loop
# otherwise start again using next num in list


def two_sum(nums, target):
  sum = 0
  goal = 0
  targetReached = False

  while not targetReached:
    for num in nums:
      goal = target - num
      if goal in nums:
        # check to not reuse same num
        if not nums.index(num) == nums.index(goal):
          targetReached = True
          return [nums.index(num), nums.index(goal)]


print(two_sum([2, 7, 11, 15], 9))