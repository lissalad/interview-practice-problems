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

# seen = { value: index }
# dictionaries FAST
# range faster than enumerate

def two_sum(nums, target):
  seen = { }

  for i, num in enumerate(nums):
    goal = target - num

    if goal in seen:
      # return goal's index and num's index
      return [seen[goal], i]
    else:
      # add new num to dictionary with its index
      seen[num] = i

print(two_sum([3, 3], 6))