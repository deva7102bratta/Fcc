def is_valid_schema(obj):
  return (
    len(obj >= 3) and isinstance(obj["username"], str) and isinstance(obj["posts"], int) and isinstance(obj["verified"], bool) 
    )
    
  
print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))