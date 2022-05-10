#       https://leetcode.com/problems/length-of-last-word/

# PROBLEM:
# given a string with chunks separated by spaces,
# return the length of the last word not including spaces

# PSEUDOCODE:
# loop through string backwords until a non-space character
# loop from that index keep count of the non-space characters
# when space is reached, return count
 
def last_word_length(string):
  start = len(string) - 1

  while string[start] == " ":
    start -= 1
    if start == 0:
      break
  
  end = start

  while not string[end] == " " and not end == 0:
    end -= 1


  
  return start - end

print(last_word_length("cool"))
  

