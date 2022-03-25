#     https://leetcode.com/problems/longest-common-prefix/

# PROBLEM:
# Given a list of strings, return the longest common prefix.
# If none, return an empty string.

# PSEUDOCODE:
# set prefix variable to be an empty string
# loop through characters in first string
# for each character and index that is equal to each of the others, add to prefix string
# if not equal to one, break loop and return string

# QUESTIONS:
# are all words the same length? should I compare to shortest word?

def longest_common_prefix(strs):
  reference = strs[0]
  prefix = ""
  maybe_matched = True

  for string in strs:
    if len(string) < len(reference):
      reference = string
  print(reference)
  
  for index in range(len(reference)):
    maybe_matched = True
    for string in strs:
      print(index)
      if not reference[index] == string[index]:
        # print(reference[index])
        # print(string[index])
        # print()
        maybe_matched = False
        break
    if maybe_matched:
      prefix += reference[index] 
    else:
      break

  return prefix

print(longest_common_prefix(["flower","flow","flight"]))
      

# FIX!!!