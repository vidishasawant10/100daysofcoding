#Given an integer x, return true if x is a palindrome, and false otherwise.
def palindrome(n):
    if n == int(str(n)[::-1]):
        return True
    else:
        return False

print(palindrome(345))