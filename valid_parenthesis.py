#     https://leetcode.com/problems/valid-parentheses/

# PROBLEM:
# given a string containing only parenthesis like () {} [],
# determine if string is valid by if they are closed 

# PSEUDOCODE:
# create key values of opening and closing brackets
# loop through string, if character matches dictionary term
# check next term to be pair closing character
# if not, return False
# otherwise move on two steps ahead in string
# return True

def valid_parenthesis(string):
  opening = {
    "(": ")",
    "[": "]",
    "{": "}",
  }

  closing = {
    ")": "(",
    "]": "[",
    "}": "{",
  }

  opened = False

  for i in range(len(string)):

    # print(string[i])

    # is expecting a closing bracket?
    if opened:
      # is closing bracket?
      if string[i] in list(closing.keys()):
        if string[i-1] == closing[string[i]]:
          # print("close")
          opened = False
        else:
          return False
      else:
        return False

  # is opening bracket? not expecting a closing bracket?
    elif string[i] in list(opening.keys()):
      # not last character?
      if i < len(string):
        if string[i + 1] == opening[string[i]]:
          # print("open")
          opened = True
        else:
          return False
      else:
        return False

    # is neither
    else:
      print("BAD INPUT")
      return False

  return True

print(valid_parenthesis("()[[]]"))