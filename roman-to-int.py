#     https://leetcode.com/problems/roman-to-integer/

# PROBLEM: 
# given a string of roman numerals, return the integer value

# PSUEDOCODE:
# create dictionary of single character values
# create dictionary of two character subtractive values
# loop through string for subtractive values
# if found, add its value to the running sum, and remove two characters from string
# loop through remaining characters for single character values
# if found, add its value to the running sum, and remove from string
# return sum value

values = {
  "I": 1,
  "V": 5,
  "X": 10,
}

subtractive = {
  "IV": 4,
  "IX": 9
}

def roman_to_int(roman):
  sum = 0
  noSubtracts = False

## check for subtracts
  while not noSubtracts:
    for key in subtractive.keys():
      if key in roman:
        sum += subtractive[key]
        roman = roman.replace(key, "")
    noSubtracts = True

## check normal values
  for num in roman:
    sum += values[num]
  return sum

print(roman_to_int("XIX"))