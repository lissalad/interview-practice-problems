#     https://leetcode.com/problems/palindrome-number/

# PROBLEM:
# given integer x, return true if it is a palindrome, otherwise false

# PSEUDOCODE:
# convert x to string
# loop through digits in string
# if opposite ordered digit is equal to current digit, continue looping
# otherwise return False
# if loop finishes, return True


def palindrome(x):
  x = str(x) 
  for index, value in enumerate(x):
    if not value == x[-index-1]:
      return False
  return True

  # OR JUST
  # return x == x[::-1]


print(palindrome(32423))
print(palindrome(435634))
print(palindrome(10))
print(palindrome(1001))