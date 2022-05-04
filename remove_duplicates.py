#
#
# loop through list
#   store previous value in variable 
#   check if current value is same as previous
#     if so, remove current from list and append _ to list
#   otherwise set previous value to current value
# return list


def remove_duplicates(nums):
  # prev = nums[0]
  length = len(nums)
  count = 0
  print(length)
  i = 1

  while i < length-2:
    # print(nums[i-1], nums[i])
    print(nums)
    if nums[i-1] == nums[i]:
      nums.pop(i)
      nums.append("_")
      count += 1
    else:
      i += 1
      
  return count, nums

print(remove_duplicates([1, 1, 3, 5, 5, 5, 6]))

    

