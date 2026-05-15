import re
def is_valid_isbn_13(s):
  s = s.replace("-", "")
  result = 0
  if len(s) != 13:
    return False
  elif re.fullmatch(r"[0-9]+", s):
    for digit in s[::2]:
      result += int(digit)*1
    for digit in s[1::2]:
      result += int(digit)*3
  else:
    return False
  if result%10==0:
    return True
  return False

print(is_valid_isbn_13("243-434-34"))

