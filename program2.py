def decode_message( s: str, p: str) -> bool:

# write your code here
  
       def match(i, j):
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        
        if p[j] == '*':
            if match(i, j + 1):
                return True
            if i < len(s) and match(i + 1, j):
                return True
        if i < len(s) and (p[j] == s[i] or p[j] == '?'):
            return match(i + 1, j + 1)
        
        return False
    
       return match(0, 0)