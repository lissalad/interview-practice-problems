#   https://leetcode.com/problems/single-number/

# PROBLEM:
# given non empty array of integers where every element except for 1 appears twice,
# return the element that appears only once

# with a linear runtime complexity 
# only one constant extra space

def single_number(nums):
  counts = {}
  single = []
  
  for num in nums:
    if num in counts.keys():
      counts[num] += 1
      single.remove(num)
    else:
      counts[num] = 1
      single.append(num)
    # print(single)
  
  return single[0]

print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
print(single_number([1]))