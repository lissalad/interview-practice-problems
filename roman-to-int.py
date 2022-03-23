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