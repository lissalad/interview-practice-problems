#     https://leetcode.com/problems/implement-strstr/

# PROBLEM:
# Given strings needle and haystack, return the index of the first instance of needle in haystack
# if not present, return -1
# if needle is empty, return 0

# ASSUME:
# haystack is not empty

# PSEUDOCODE:
# check if needle is empty
# otherwise, loop through haystack characters
# if needle's first character is found, loop through needle to see if complete in haystack
# if so, return needle's first index 
# otherwise keep looping
# return -1

def strStr(haystack, needle):

  # empty?
  if len(needle) == 0:
    return -1

# loop through haystack
  for hayChar in range(len(haystack)):

    # found beginning of needle
    if haystack[hayChar] == needle[0]:
      index = hayChar

      # might contain needle
      contains = True

      # while matching streak is intact
      while(contains):

        # loop through needle checking for next characters in haystack
        for needChar in range(len(needle)):

          # print(len(haystack)-1)
          # print(index)

          # prevent out of range error
          if index >= len(haystack)-1:
            contains = False
            break

          # evaluate if next characters are matching, if streak continues
          if haystack[index] == needle[needChar]:

            # print("ok")
            index += 1
          else:
            # print("nope")
            contains = False
        
        # return the index if we make it through the needle's loop without breaking streak
        if contains:
          return hayChar
        
  # return -1 if we loop through with no match
  return -1

print(strStr("elissa", "ll"))
