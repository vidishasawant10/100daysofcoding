def anagram(s,t):
    if len(s)!= len(t):
        return False

    countS = {}
    countT ={}
    for char in s:
        if s.count(char)!= t.count(char):
            return False
    return True

s= "anagram"
t = "nagaram"
print(anagram(s,t))