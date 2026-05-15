def find_offender(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      if len(arr) < 4:
        return 0
      if arr[i] >= arr[2+i]:
        return i
      elif arr[i+1] <= arr[i-1]:
        return i+1
      else:
        return 0
    
      
      
      
    