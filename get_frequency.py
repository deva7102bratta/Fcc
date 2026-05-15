def get_frequency(s):
  result = {
    
  }
  for ch in set(s):
    result[ch]  = s.count(ch)
  return result

