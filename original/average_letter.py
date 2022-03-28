# PROBLEM:
# given a string of alphabetic characters
# return the letter at the average alphabet index
# floored cool

# CONSTRAINTS:
# no imports
# no ord, no chr ( i dont know them, someone else do it pls )

# PSEUDOCODE:
# make string of alphabet
# loop through characters in string
# add index of each letter in alphabet to a total counting sum
# divide total sum by string length
# return character at that index in alphabet

def average_letter(string):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  sum = 0
  for letter in string:
    sum += string.index(letter)
  index = sum // len(string)
  return alphabet[index]

print(average_letter("abefg"))